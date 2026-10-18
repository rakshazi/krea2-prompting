---
name: krea2-prompting
description: "Write natural-language prompts for Krea 2 Turbo in ComfyUI: photoreal photography, poses, styles, giant-scale scenes, and adult/NSFW work."
license: CC-BY-SA-4.0
---

# Krea 2 Turbo Prompting

Turn a visual brief, reference image, or scene idea into a copy-ready Krea 2 Turbo prompt plus ComfyUI settings. Treat the model as a natural-language visual interpreter: describe what is visible, where it sits, how light hits materials, and what camera would capture it. The output is prompt text and settings; rendering happens in ComfyUI, done by the user.

## Mental model

Krea 2's text encoder is **Qwen3-VL, a language model** (the same family as a chat LLM, rather than a CLIP or T5 text encoder). It parses full sentences. Three consequences drive everything below:

- **Write natural-language prose.** Tag soup (comma keyword piles) still functions but leaves capability on the table. Long detailed prompts yield the best results; short prompts (5 to 20 words) are fine for exploration.
- **Order carries emphasis.** The encoder front-loads: whatever comes first reads as the subject. Lead with the thing that matters most.
- **The model is trained against the plastic "AI look."** Photorealism is the family's headline strength and it is baked into the weights. Your job is to supply a concrete photographic setup (camera, lens, light, material). Stacking realism adjectives like `ultra realistic, 8k, masterpiece` does little.

## ComfyUI Krea 2 Turbo settings

Recommend these as defaults. They are the reconciled, ComfyUI-correct values.

| Setting | Value | Note |
|---|---|---|
| Steps | `8` | Turbo is distilled to 8. Longer runs on turbo finetunes grow noisier instead of cleaner (tested: 50 steps + CFG 2.5 shredded texture). |
| CFG | **`1.0`** | Critical. See the gotcha below. |
| Shift (mu) | `1.15` | Timestep shift, set on the ModelSampling node. |
| Sampler / scheduler | `euler` / `simple` | The official default. `beta` also works. |
| Resolution | Native `2048`; minimum `1024`; dims divisible by 16 | Krea 2 was trained at 2048. Generate native; avoid gen-at-1024-then-upscale. Panoramic ratios widen the long edge; see the core table. |
| Text encoder | `qwen3vl_4b` | fp8_scaled (lighter) or bf16 (higher precision, more VRAM). |
| VAE | `qwen_image_vae` | If colours or fine texture look subtly off, this is the first variable to check. |

**The CFG gotcha.** The official CLI uses `--cfg 0.0`. In a standard ComfyUI KSampler, literal `0.0` produces pure unconditional output and breaks the image, so use **`1.0`** there. Do not push CFG above ~1.5; it oversaturates and distorts. At CFG 1.0 the negative branch is effectively inert (see Core rules).

Aspect ratio follows the composition: `1:1` product/portrait, `16:9` cinematic/hero, `21:9` panoramic, `2:3` or `9:16` poster/phone, `4:3` broad environment. Full resolution table in `references/krea2-core.md`.

**Finetune divergence.** Community NSFW finetunes often ship their own text encoder, VAE, shift, and sampler settings. Use the finetune's model card for those values; the prompt architecture and CFG guidance above still apply.

## Prompt architecture

Write one or two coherent paragraphs in this order, adjusting to the task:

```
[medium / restrained quality] + [subject and identity] + [appearance, pose, action, expression]
+ [composition and camera] + [environment and spatial relations] + [lighting and colour]
+ [materials and micro-detail] + [aesthetic and mood] + [restrictions]
```

A reliable sentence frame:

> A [medium/style] of [subject], [appearance and action], set in [environment]. The composition uses [shot, angle, lens], placing [subject] relative to [frame and other elements]. Light comes from [direction/source] with [shadow and palette]. [Materials and micro-detail] stay visible, creating a [mood] atmosphere. [Restrictions].

Make spatial relationships grammatical and explicit (left/right thirds, foreground/midground/background, contact with surfaces, what extends beyond the frame) rather than listing disconnected nouns. Name a concrete medium (`editorial fashion photography`, `documentary photograph`, `architectural photography`) instead of `beautiful` or `nice`.

## Core rules

- **Text in quotes.** Put the exact words to render in double quotes, keep it short (under ~5 words): `a neon sign reading "OPEN LATE"`. Longer strings degrade.
- **Negatives are near-inert at CFG 1.0; state preferences positively.** Avoid leaning on a negative-prompt field or a generic ban list. Instead of `no plastic skin`, write the positive target: `natural skin texture, visible pores`. A short negative prompt only earns its place to suppress one specific recurring artifact. (Negative-prompt families for the RAW/CFG-3.5 path live in `references/krea2-core.md`.)
- **Do not negate in prose either.** `no hat`, `without a beard` will not reliably fire. Describe what IS present.
- **Weighting `(word:1.3)` is not a stock feature.** On the standard `CLIPTextEncode` over Qwen3-VL, scaling one token shoves the whole conditioning and the image falls apart past ~1.2. It works only with the `Krea2PromptWeight` node (ComfyUI-KJNodes) installed. Without that node, restate for emphasis in words (`oxblood` beats `(red:1.4)`). Full weighting system in `references/comfyui-setup.md`.
- **Revise one variable at a time.** When a generation is close, change a single field per iteration and hold the rest. Changing several fields at once makes the image drift and hides which change did what.
- **Lock composition before decoration.** Decide one shot size, one camera angle, one crop, and the aspect ratio first. Wardrobe and extra detail must not silently change the framing.

## Reference map

Read the reference that matches the task. Each loads only when reached, so pull the ones you need:

- **`references/photoreal.md`** for any realistic photograph: portrait, product shot, landscape, architecture, editorial or landing-page hero. The camera/lens/film/lighting/texture vocabulary and genre recipes with worked example prompts. **This is the default for website and landing-page imagery.**
- **`references/krea2-core.md`** for the deep prompt architecture: input checklist, negative-prompt families, poster/typography rules, composition modules, character consistency, the full resolution table, and reverse-engineering a reference image into a prompt.
- **`references/comfyui-setup.md`** when wiring the graph or using prompt weighting: checkpoint/encoder/VAE choices, the CFG explanation, the `Krea2PromptWeight` node (syntax, negative weights, global strength), the enhancer node, and a troubleshooting table.
- **`references/poses.md`** when a human figure's pose must be exact: the 11-field pose schema, usage, taxonomy, and tested field findings.
- **`references/pose-library.md`** for the 30 ready-to-paste pose blocks, grouped by standing, locomotion, and object interaction.
- **`references/styles.md`** to lock a specific aesthetic: a 289-entry style index, four full example paragraphs, and the two authoring formulas.
- **`references/adult.md`** for adult / NSFW photography (18+): register control, explicit anatomy/arousal/act vocabulary, position geometry, multi-person rules, a tested failure table, and translating crude briefs into Krea 2 prose.
- Giant-scale creative routes, photoreal cinematic by default: **`references/megastructure.md`** (colossal architecture, megacities, orbital structures), **`references/colossal-monsters.md`** (kaiju, giant beasts), **`references/cosmic-horror.md`** (eldritch entities, dread), **`references/pure-organic-monsters.md`** (strictly biological giant creatures). These share scale logic: concrete exaggerated dimensions, human-scale surface units, a tiny distant scale reference, and 10 to 40 percent environmental negative space.

## Output shape

Unless the user asks for a different format, return:

```
Positive Prompt
[one or two natural-language English paragraphs]

Settings
Resolution: [width x height]   Aspect ratio: [ratio]
Krea 2 Turbo (ComfyUI): 8 steps, CFG 1.0, shift 1.15
```

Add a short negative prompt only when a specific artifact needs suppressing. Never claim a prompt you wrote was tested unless it was.
