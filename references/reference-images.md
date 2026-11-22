# Krea 2 Reference Images

How to make Krea 2 Turbo keep a character, outfit or style from a reference image, plus the prompt shape that goes
with it. Two wirings, all core ComfyUI nodes, no custom packs. Read this when a brief says "same character as last
time", "keep her face", "in this style", or "use this product photo".

## Why references work at all

Krea 2 conditions its DiT on hidden states tapped from Qwen3-VL-4B. That encoder is a vision-language model, so an
image can ride inside the prompt as vision tokens, and the DiT reads the character from the same states it was trained
on. Two consequences:

- The reference is read semantically. It carries identity, outfit, proportions and art style, and it outranks any
  adjective you can stack in the prompt.
- The DiT has no reference-latent pathway of its own. VAE latents only reach it when a LoRA trained for that pathway
  is loaded (`krea2_style_reference`).

That split is the whole decision: vision tokens for identity, vision plus latents for texture and style lock.

## Files

| File | Destination | Why |
|---|---|---|
| `krea2_turbo_fp8_scaled.safetensors` (or a Turbo finetune) | `models/diffusion_models/` | the 8-step model |
| `qwen3vl_4b_fp8_scaled.safetensors` | `models/text_encoders/` | the VLM that reads the image, `CLIPLoader` type `krea2` |
| `qwen_image_vae.safetensors` | `models/vae/` | official VAE, decodes the output and feeds the latent route |
| `krea2_style_reference.safetensors` | `models/loras/` | optional, 436 MB, opens the latent route |

Official files live at `huggingface.co/Comfy-Org/Krea-2`; the LoRA also ships at
`huggingface.co/ostris/krea2_turbo_style_reference` and on CivitAI as "Krea 2 Style Reference LoRA". The encoder must
carry its vision tower. The bf16 file always does. fp8 encoded reference images fine on stock ComfyUI 0.45.4; if your
build errors on image inputs, switch the encoder to bf16.

## Route A: vision tokens, the character route

Wiring, with API-format class names:

| Node | Inputs |
|---|---|
| `CLIPLoader` | `qwen3vl_4b_fp8_scaled.safetensors`, type `krea2` |
| `TextEncodeQwenImageEditPlus` | `clip` from the loader, `prompt`, `image1` to `image3`, **`vae` left empty** |
| `ConditioningZeroOut` | the same conditioning, wired to the negative slot |
| `UNETLoader` then `ModelSamplingAuraFlow` (`shift: 1.15`) | feeds `KSampler.model` |
| `KSampler` | 8 steps, CFG 1.0, `euler` and `simple` (or `beta`), denoise 1.0 |
| `VAELoader` (`qwen_image_vae`) then `VAEDecode` | decodes the result |

The image never enters the latent space; it enters the prompt. That is why the art style stays crisp and the reference
texture does not leak into the frame.

Prompt shape:

> Keep the same catgirl from Picture 1: a white-haired catgirl with a silver bob, blue eyes, white cat ears with pink
> inner fur, one fluffy tail, a generous bust, a narrow waist, wide hips and thick thighs, in a black blazer over a
> white shirt and black thigh-high stockings. Place her in a server room at night, kneeling beside an open rack with a
> patch cable in one hand. Rendered as a crisp anime editorial illustration with clean ink linework, flat cel shading,
> a warm cream paper background, charcoal shadows and one hot orange accent.

Rules that make it hold:

- **Name every connected picture.** `Picture N` is how the encoder addresses slot N, and the core node inserts a
  `Picture N:` vision placeholder for each image in slot order. An image the prompt never mentions is usually ignored.
- **Identity first, scene second, style last.** The early steps take their layout from the text, so the scene clause
  has to stand on its own.
- **One reference per character.** Two references of the same character render her twice in the frame, often as a
  foreground close-up plus a small full figure.
- **The reference owns proportions, outfit and expression.** A slim reference renders a slim character no matter
  what the prompt says about her figure, and a grinning reference drags the grin into every scene. Silhouette
  follows the garment cut as well: a hugging mini reads as wider hips than a pencil skirt on the same body.
  Fix the reference itself; adjectives cannot override it.
- **A figure the sheet does not carry will not appear.** Two sheet-conditioned renders stayed slim against a prompt
  that asked for `a generous bust, a deep cleavage line, wide hips and thick soft thighs`. When a one-off needs a
  fuller or heavier figure than the sheet carries, render that image text-only from the identity block and leave the
  sheet out. When identity has to survive the set, rebuild the sheet at the target figure first.
- **Trim and small accessories are identity too, and they misbehave.** A jacket lining from the sheet got painted onto
  the blouse underneath it, and the sheet's hairpins turned up as a floating glyph beside another character's head.
  Say where an accent sits ("the hot-orange lining stays inside the open blazer") and check the accessory count and
  placement in the render.
- **Traits leak onto character-like props.** With an animal-eared reference wired, a talking paper envelope in the same
  frame grew the same ears and a fluffy tail. Keep anthropomorphic props out of frames that carry the cast, or expect
  the species to spread.
- **A face close-up replaces the full-body sheet** in close-up posts. It never joins it.
- **Three references maximum.** The core node exposes `image1` to `image3`.

### Two or more references: split the schedule

With two references the model tends to paste both of them into the frame, so a two-character scene comes back with
three characters. Let the prompt own the composition for the first quarter of the steps:

| Node | Inputs |
|---|---|
| `CLIPTextEncode` | the same prompt with the `Picture N` clauses removed, text only |
| `ConditioningSetTimestepRange` | that text-only conditioning, `start 0.0`, `end 0.25` |
| `ConditioningSetTimestepRange` | the `TextEncodeQwenImageEditPlus` conditioning, `start 0.25`, `end 1.0` |
| `ConditioningCombine` | both ranged conditionings, into `KSampler.positive` |

A `PrimitiveFloat` wired to both split fields makes it tunable; 0.25 is the tested default. With 8 steps the first
two keep the layout and the references steer identity for the remaining six. Verified on a two-character scene that
otherwise produced a duplicate of the catgirl.

Cast prompt:

> Keep the same two characters from Picture 1 and Picture 2: on the left the tired engineer in a charcoal hoodie and
> rectangular glasses, on the right the white-haired catgirl with a silver bob, cat ears and one fluffy tail. They
> stand at a whiteboard covered in DNS diagrams, the engineer pointing at a red arrow with a marker, the catgirl
> holding a paper coffee cup and smirking.

Give each character one distinct action and an explicit side. Vague "both are standing" wording invites the model to
duplicate the one it read first.

### Limits of the split

The split buys layout control; it has a hard ceiling. On crowded frames, meaning two references plus a third figure or
an anthropomorphic prop character, a duplicate survived splits of 0.25, 0.35 and 0.5, across several seeds. The fix
that worked was dropping a character from the scene so only one reference was wired: one catgirl alone at the desk,
one figure in the render. Restaging the described pose to match the sheet's stance changed nothing, and rewriting the
scene so both characters stood changed nothing either. The extra copy arrives with the conditioning, so the reliable
lever is the number of references in the graph. When both characters are non-negotiable, compose them as two separate
single-reference shots.

Raising the split has a price. At 0.5 with a single reference the identity weakened visibly: the wrong tail colour came
back, the linework flattened toward vector, and the text-only pass picked a tight crop that cut the head out of frame.
Treat 0.25 to 0.35 as the working range. When you override `layout_prompt`, state the shot size and the crop in it,
because that pass decides the framing before any reference is seen. Keep lettering out of the plan there too: the same
override flattened a large headline into invented letters.

### Three or more figures

The split does not scale to a crowd. Seven characters seated in a row, prompt-only with no references wired, came back as an even line of identical backs: the same shoulder width, the same spacing, the outer two sliced by the frame edge, and one of them rendered without clothes. Nothing in that prompt was ambiguous. The model has no notion of a crowd, so it tiles the one figure it knows.

Build the set piece as two jobs instead. Render the empty location plate with the single character who belongs in it, render every other character in her own frame, then composite. The plate holds the counter line, the light and the perspective still, and each character comes from a prompt tuned for her alone. The composite needs a silhouette that stays outside the paste zone, so keep hands and props off the surfaces that will be covered.

## Route B: reference latents, the style route

Same graph, plus the latent pathway:

| Change | Detail |
|---|---|
| `TextEncodeQwenImageEditPlus.vae` | connect `qwen_image_vae` |
| `FluxKontextMultiReferenceLatentMethod` | `reference_latents_method: index_timestep_zero`, between the encoder and the sampler |
| `LoraLoaderModelOnly` | `krea2_style_reference.safetensors`, `strength_model: 1.0`, between the UNET and the sampling node |

This is the wiring behind the official Comfy-Org "Krea 2 Int8: Image Style Reference" template. It transfers the
reference texture as well as the subject, so a halftone or grainy reference turns the whole frame halftone. Use a
clean reference or lower the LoRA strength. The payoff is a stronger style lock, which makes it the better route for
style references.

Simpler single-reference variants exist: `ReferenceLatent` (core) attached to the same conditioning, or Ostris's
`ComfyUI-Krea2-Ostris-Edit` pack for edit LoRAs trained with ai-toolkit. Both feed the same latent pathway; only the
wiring above is verified in this guide.

## Reference images that work

Make the sheet first. Generate the character text-only, one view, plain background, canonical outfit, 1024 to 1536 on
the long side. When you need a face sheet and a full-body sheet, generate the face first, then generate the body
with the face sheet as Picture 1: identity, hair clip, expression and colours transfer as one package. Count small
accessories explicitly (two parallel pins, one clip) and crop the sheet at 3x to check them; a thumbnail hides the
third pin. Review the sheet before it becomes canon: face, hair, ears, outfit, garment edges and proportions are
now the identity contract, and a skin-coloured patch where a blouse meets the chest becomes canon too. When a
feature drifts, edit the sheet instead of stacking more identity adjectives into every scene.

- One character, one pose, facing the camera. Full body for scenes, head and shoulders for a face sheet.
- Plain, empty background. Text, logos, other characters and clutter leak into the render.
- Even flat light. Dramatic shadows become part of the identity.
- The canonical outfit, or the closest one you want repeated. Separate dark garments that touch: a black jacket over
  a black skirt reads as one oversized mass. Crop the jacket at the waist or show a shirt band, a buckle or a light
  trim, and the silhouette stays honest.
- 1024 to 1536 on the long side is plenty: references are read at roughly one megapixel.
- No character sheets. Multi-view sheets teach the model to clone the extra views.

## Failure table

| Symptom | Cause | Fix |
|---|---|---|
| A blocky grid of patches in the frame | latent route running without `krea2_style_reference` | load the LoRA at 1.0, or drop the `vae` input for Route A |
| Whole frame turns grainy or halftone | latent route copying a textured reference | use a clean reference or lower the LoRA strength |
| Muddy colours and soft texture on the latent route | Wan-family VAE | connect `qwen_image_vae` |
| The character appears twice | two refs of one character, or two refs without the split | one ref per character, plus the 0.25 split; if it persists, drop a character so one reference stays wired |
| A prop character grows the cast's ears or tail | species traits leaking from the reference | wire only the references the frame needs, and keep anthropomorphic props out of it |
| A small accessory floats beside a head | sheet accessories detaching from the design | re-seed, and state where the accessory sits |
| An outfit accent lands on the wrong garment | the sheet's trim colour read as a separate piece | say where the accent sits, e.g. the lining stays inside the open jacket |
| Wrong hair or tail colour, flatter linework, tight unexpected crop | layout split pushed to 0.5 | keep the split at 0.25 to 0.35, and state the shot in `layout_prompt` when you use it |
| Reference ignored | the prompt never names it | add `Picture N` for every connected image |
| References pasted side by side like a collage | busy reference backgrounds, or no layout split | clean single-pose refs, split the schedule |
| Face drifts between scenes | reference too small, or a thin identity block | tighter full-body sheet, concrete identity nouns, face sheet for close-ups |

## Other reference stacks

| Project | What it adds | Caveats |
|---|---|---|
| `conradlocke/krea2-identity-edit` with `lbouaraba/comfyui-krea2edit` | identity restaging with `ref_boost`, grounding resolution and per-reference placement | trained on photoreal SFW people; V2 weights are personal-use only; needs the custom node pack |
| `KonokoAz/ComfyUI-Krea2-Reference` | up to four references with `characterN` and `styleN` roles, patch shuffle for style-only slots, layout split | the companion reference LoRA has no public download, so it runs zero-shot |
| `kgilper/krea-reference` | guide cards for subject, style, pose, palette and anti-text, encoded as conditioning | training-free, many knobs, explicitly not an identity guarantee |

## What is verified, and on what

ComfyUI 0.45.4, a Krea 2 Turbo finetune (Lustify v10), `qwen3-vl-4b-heretic` fp8 encoder, `qwen_image_vae`, 8 steps,
CFG 1.0, shift 1.15 and 4.0 both verified with `simple` and `beta`, 2048x1152 output, references at 1024 to 1728 on
the long side.

Two passes stand behind the rules above: three seeds with one and two references across different scenes, then 20
scenes at 2048x1152 with two references on the vision route. Identity held across both. Both fp8 encoders encoded
vision tokens.
