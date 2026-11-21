---
name: krea2-prompting
description: >-
  Write, revise or debug image prompts and sampler settings for Krea 2 and Krea 2 Turbo in ComfyUI. Use when the user
  asks for an image prompt (Krea 2 is assumed when no model is named), only describes the picture they want, or asks
  about reference images, character consistency, pose or style blocks, speech bubbles, Krea 2 settings, or NSFW/18+
  images. Returns prompt text, settings and wiring; runs no renders.
license: CC-BY-SA-4.0. Full text in LICENSE.
compatibility: >-
  Text-only: no scripts, network, GPU, or ComfyUI endpoint required. The agent needs file-read access to load
  references/ on demand. Hosted clients with content filters may block references/adult.md, which is 18+.
metadata:
  version: "1.4.0"
  author: rakshazi
  source: https://github.com/rakshazi/krea2-prompting
  tested-on: Krea 2 Turbo, qwen3vl_4b encoder, qwen_image_vae, 8 steps, CFG 1.0, reference images on ComfyUI 0.45.4
---

# Krea 2 Turbo Prompting

Turn a visual brief, reference image, or scene idea into a copy-ready Krea 2 Turbo prompt plus ComfyUI settings. Describe what is visible, where it sits, how light hits materials, and what camera would capture it. The output is prompt text and settings; the user renders in ComfyUI.

## Mental model

Krea 2's text encoder is **Qwen3-VL, a language model** (the same family as a chat LLM, where older image models use CLIP or T5). It parses full sentences. Four consequences drive everything below:

- **Write natural-language prose.** Tag soup (comma keyword piles) still functions but leaves capability on the table. Long detailed prompts yield the best results; 5 to 20 words is fine for exploration.
- **Order carries emphasis.** Whatever comes first reads as the subject. Lead with the thing that matters most.
- **Realism comes from a photographic setup.** The model is trained against the plastic "AI look", so name the camera, lens, light and material. Stacking `ultra realistic, 8k, masterpiece` does little.
- **A reference image outranks adjectives.** The encoder is also a vision model: an attached picture supplies identity, outfit and proportions directly, and the prompt is spent on scene and style.

## Settings

Krea 2 Turbo in ComfyUI. Recommend these as defaults.

| Setting | Value | Note |
|---|---|---|
| Steps | `8` | Turbo is distilled to 8. More steps grow noisier (tested: 50 steps + CFG 2.5 shredded texture). |
| CFG | **`1.0`** | The official CLI says `0.0`; in a ComfyUI KSampler literal `0.0` is pure unconditional output and breaks the image. Above ~1.5 it oversaturates and distorts. |
| Shift (mu) | `1.15` | Timestep shift, set on the ModelSampling node. |
| Sampler / scheduler | `euler` / `simple` | The official default. `beta` also works. |
| Resolution | Native `2048`; minimum `1024`; dims divisible by 16 | Trained at 2048. Generate native; avoid gen-at-1024-then-upscale. Panoramic ratios widen the long edge past it. |
| Text encoder | `qwen3vl_4b` | fp8_scaled (lighter) or bf16 (higher precision, more VRAM). |
| VAE | `qwen_image_vae` | If colours or fine texture look subtly off, check this first. |

Aspect ratio follows the composition: `1:1` product/portrait, `16:9` cinematic/hero, `21:9` panoramic, `2:3` or `9:16` poster/phone, `4:3` broad environment. Pixel sizes per ratio are in `references/krea2-core.md`.

A community finetune may ship its own text encoder, VAE, shift and sampler: take those from its model card. The CFG value and everything about prompting still apply.

## Prompt architecture

Write one or two coherent paragraphs in this order, adjusting to the task:

```
[medium / restrained quality] + [subject and identity] + [appearance, pose, action, expression]
+ [composition and camera] + [environment and spatial relations] + [lighting and colour]
+ [materials and micro-detail] + [aesthetic and mood] + [restrictions]
```

A reliable sentence frame:

> A [medium/style] of [subject], [appearance and action], set in [environment]. The composition uses [shot, angle, lens], placing [subject] relative to [frame and other elements]. Light comes from [direction/source] with [shadow and palette]. [Materials and micro-detail] stay visible, creating a [mood] atmosphere. [Restrictions].

Make spatial relationships grammatical and explicit (left/right thirds, foreground/midground/background, contact with surfaces, what extends beyond the frame). Name a concrete medium (`editorial fashion photography`, `documentary photograph`, `architectural photography`) where a weaker prompt says `beautiful` or `nice`.

## Workflow

1. **Classify the brief.** Pick the route (photoreal, style, pose, adult, giant-scale) and pull out the hard constraints: text to render, aspect, register, number of people, what must stay fixed. Ask only when a missing detail changes the picture; otherwise state the assumption and proceed.
2. **Read one reference by route** (Routes, below). Add a second only when the brief spans two routes.
3. **Lock composition before writing.** One shot size, one angle, one crop, one aspect ratio. Wardrobe and decoration come after and must leave the framing alone.
4. **Draft in the sentence frame.** Subject first, then action, camera, environment, light, materials, mood, in full sentences.
5. **Check the draft** against every line of "Every prompt", then against each row of "When the brief contains" that matches. Fix what fails.
6. **Emit in the output shape** at the end of this file.

## Every prompt

- **State what IS present.** Negation is near-inert at CFG 1.0, in the negative field and in prose alike. `no people` becomes `an empty street`; `no plastic skin` becomes `skin with visible pores and fine vellus hair`. A negated noun can backfire: the encoder may reinforce the thing you tried to ban. A short negative prompt earns its place only to suppress one specific recurring artifact.
- **Cut the quality stack.** `8k, masterpiece, best quality, ultra detailed` buys nothing and makes the image look generic. Scan the draft for it and spend those words on camera, lens, light and material.
- **Rendered text goes in double quotes, five words at most, on a flat surface facing the camera:** `a neon sign reading "OPEN LATE"`. A banner, a box or a plate letters cleanly; a curved can label or a rolled scroll comes back with invented strokes or reversed letters.
- **Count anything that must appear once.** An uncounted label or prop gets duplicated. Name the one instance, then say what the frame's other lettering is: `exactly one small brass plate on the counter's front edge reads "OMP", and the neon sign is the only other lettering in the scene`. For a person, "the only figure in the frame" is a weak hint: with a long prop list she still cloned herself, so keep the list short and re-roll.
- **Dress a character top to bottom.** Name the lower garment and the hosiery in the same clause as the top, every time, including for a character you think is fully described. A clause that stops at the hoodie renders nothing below the waist.
- **Emphasis goes in words.** `oxblood` beats `(red:1.4)`: on the stock encoder a weight shoves the whole conditioning and the image falls apart past ~1.2.
- **Revise one variable at a time.** Hold the seed and change a single field per iteration. Several changes at once make the image drift and hide which one did what.

## When the brief contains

Each row is a tested failure with its fix. The reference holds the exact wording.

| In the brief | Do this | Wording and receipts |
|---|---|---|
| A line longer than five words, or a speech bubble | Generate one blank bubble and typeset the line after the render. Ask for the bubble up front, or the head fills the top of the frame. | `references/krea2-core.md`, "Text and lettering" |
| A screen: chart, chat window, terminal or dashboard | Generate the screen area empty and paste a real screenshot over it. Rewording never fixes a whole interface. | `references/krea2-core.md`, "Text and lettering" |
| A hand holding an object | An open palm presenting it, or a cuff, handle or stick for the fist to wrap. Name the contact. A closed fist on a bare object breaks. | `references/poses.md`, "Hands and held objects" |
| A detached or uncanny prop, or a deliberate anatomy joke | Give it a material the character cannot share, and state a visible gap between prop and body. | `references/krea2-core.md`, "Staged props" |
| A recurring character, "same as last time" | Attach one clean single-pose reference and open the prompt with `Keep the same <who> from Picture 1: <identity block>.` The reference sets proportions whatever the prose says. | `references/reference-images.md` |
| Two characters from two references | One side and one distinct action each, plus the 0.25 layout split. If one keeps cloning, render two single-reference shots. | `references/reference-images.md`, "Two or more references" |
| Three or more figures | Render the location with one character, every other character alone, then composite. | `references/reference-images.md`, "Three or more figures" |
| Pale, even or matching skin tone | Swap flash for soft overcast daylight at a neutral white balance, and tie the tone to a named body part. | `references/photoreal.md`, "Skin tone" |
| A LoRA that seems to do nothing | A/B at one fixed seed up to ±3 or ±5 before writing it off. A slider reads dead at ±1.5. | `references/comfyui-setup.md`, "LoRA strength" |
| Emphasis that words cannot give | Weights and negative weights, which need the `Krea2PromptWeight` node. | `references/comfyui-setup.md`, "Prompt weighting" |

## Routes

Read the reference that matches the picture. Each loads only when read.

- **`references/photoreal.md`**: any realistic photograph (portrait, product, landscape, architecture, street, editorial). **The default for website and landing-page imagery.** Camera, lens, film and light vocabulary, skin tone, genre recipes with example prompts.
- **`references/krea2-core.md`**: posters and lettering, bubbles and screens, staged props, character replacement, the identity block for a recurring character, composition modules, negative families for a live-negative path, the resolution table, and turning a reference image into a prompt.
- **`references/reference-images.md`**: a character, outfit or style that must come from a picture. Both ComfyUI wirings (vision tokens for identity, reference latents for style), the `Picture N` prompt shape, the layout split, reference-sheet rules, a failure table.
- **`references/comfyui-setup.md`**: wiring the base graph, the RAW checkpoint, prompt weighting, LoRA strength, troubleshooting.
- **`references/poses.md`**: a pose that must be exact. The 11-field schema and how to adapt it. **`references/pose-library.md`** holds 30 ready-to-paste blocks.
- **`references/styles.md`**: locking a named aesthetic. A 289-entry style index, four full paragraphs, two authoring formulas.
- **`references/adult.md`**: adult / NSFW photography (18+). Register control, explicit vocabulary, position geometry, multi-person rules, a tested failure table, and translating a crude brief into prose.
- **Giant scale**, photoreal cinematic by default: `references/megastructure.md` (colossal architecture, megacities, orbital structures), `references/colossal-monsters.md` (kaiju, giant beasts), `references/cosmic-horror.md` (eldritch entities, dread), `references/pure-organic-monsters.md` (strictly biological giants). All four share one scale logic: concrete exaggerated dimensions, human-scale surface units, a tiny distant scale reference, and 10 to 40 percent environmental negative space.
- **`examples/README.md`**: ten topics, each written generic and with this skill, with both renders. Open one when the user asks what the skill changes or wants a style anchor.

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

Editing this skill: read `AGENTS.md` in this directory first.