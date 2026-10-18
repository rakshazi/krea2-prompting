# Photorealism Reference

The default reference for a realistic photograph: portrait, product, landscape, architecture, street, editorial, or landing-page hero. Krea 2 is trained to avoid the oversaturated plastic "AI look", so realism is already in the weights. The prompt's job is to describe a concrete photographic setup. Piling on realism adjectives adds little.

## The governing principle

Light and material language beat quality adjectives. `photorealistic` alone is weak: it names a preference and gives the model no setup to render. A prompt that names the camera, the lens, the light source and direction, and the actual surface materials will read as photographed. A prompt that stacks `ultra realistic, hyperdetailed, 8k, masterpiece` will look generic. Describe the shoot, and the realism follows.

## Vocabulary that pushes toward photography

**Shot size and angle:** extreme close-up, close-up, portrait, three-quarter, half-body, full body, wide establishing shot; low angle, high angle, eye level, top-down, dutch tilt.

**Lens feel:** `35mm environmental`, `50mm natural`, `85mm portrait`, `f/1.4`, `f/2`, `shallow depth of field`, `deep focus`, `creamy bokeh`, `long-lens compression`, `macro`.

**Film stock (palette control):** `shot on Kodak Portra 400` pushes a warm film palette; `Kodak Gold`, `Fuji Pro 400H`, `Cinestill 800T` (tungsten night look), `Ilford HP5` (black and white). `film grain` nudges the whole frame toward an analog editorial feel.

**Lighting:** soft diffused light, hard directional key light, golden hour, blue hour, overcast, rim light, backlight, side light, top light, practical light (a named in-scene source: a window, a lamp, neon), low-key, high-key, warm tungsten, cool daylight, motivated lighting (light that has a visible source in the scene).

**Texture and imperfection (the anti-plastic cues):** natural skin texture, visible pores, vellus hair, fabric weave, wet highlights, condensation, dust in the light beam, micro-reflections, wet pavement reflections, scuffed surfaces, worn edges, fingerprints on glass. For portraits, character detail helps: `weathered skin, deep wrinkles, freckles, stray hairs`.

**Real-camera grounding (strong on candid/portrait):** `candid, in the moment`, `authentic skin texture`, `natural facial features`, `taken on a phone camera` for a casual snapshot register.

**Candid amateur register (tested on Krea 2 NSFW finetunes).** `amateur photo` as the opening medium clause plus `harsh direct flash`, `natural skin texture with visible pores`, and `film grain` is the workhorse register: it holds identity, produces warm candid color, and cooperates with explicit content. The register clause goes FIRST: a register buried at the prompt's end is ignored and the polished editorial look returns. Skin realism cue that survives every scene: `film grain` plus one named imperfection family (pores, sweat sheen, flush); stacked realism adjectives still do nothing.

State imperfection positively. Write `natural skin texture with visible pores`; avoid `no plastic skin` (negation is weak here, and the encoder may reinforce the noun you tried to ban).

## Genre recipes

Each recipe is a template plus a worked example prompt. Copy the example, swap the subject, keep the structure.

### Portrait

Template: `A [shot size] portrait of [subject] in [wardrobe], [setting], [lighting], [lens feel], [skin/material detail], [colour grade], [crop].`

Examples:

```
A calm editorial portrait of a young woman at golden hour, soft rim light, shallow depth of field, pastel wardrobe, natural skin texture with catchlights in the eyes, 3:4 crop
```

```
A cinematic golden-hour portrait of a man in his forties, shot on 85mm f/1.4, soft warm rim lighting, shallow depth of field, creamy bokeh, editorial magazine styling, ultra-detailed skin texture, natural colour grade, 4:5 crop
```

```
A moody cinematic portrait of a weathered older fisherman, golden hour backlight, shallow depth of field, 85mm, film grain, photorealistic
```

### Product / still life

Name the surfaces explicitly. Concrete materials (`wet black stone`, `matte ceramic`, `brushed aluminium`) give the model something physical to render.

```
A matte ceramic skincare jar on a sculpted stone plinth, continuous warm-grey sweep backdrop, soft directional key light with a gentle rim highlight, 4:3 hero crop
```

```
A luxury perfume bottle on wet black stone, studio lighting, water droplets, glossy reflections, subtle rim light, shallow depth of field, hyperreal product photography
```

### Landscape / environment

Template: `Establishing view of [place], [weather], [light path], [scale cue], [lens], [palette], [crop].`

```
A towering rust-orange suspension bridge stretches across deep blue-green water beneath a bright sky, photographed from a low vantage point, long-lens compression, crisp midday light, 16:9
```

### Architecture

Formula: Building type + materials + context + lighting + medium.

```
Modern residential house, white stucco facade, large glass windows, concrete base, surrounded by mature trees and green lawn, warm late-afternoon sunlight, architectural photography, photorealistic
```

### Street / candid

```
Candid street photograph of a courier walking through a rain-slicked city on an overcast day, 35mm f/2, documentary realism, muted desaturated tones, soft diffused light, wet pavement reflections, motion in the background crowd, film grain, photojournalistic composition
```

### Editorial / landing-page hero

The key website use case. Two rules make an image usable as a hero:

1. **Reserve a quiet zone.** Add explicit negative space where the headline and call-to-action will sit: `wide empty sky on the left third for overlaid title text`. The model fills every region unless told to leave one calm.
2. **Set the crop up front.** Decide `16:9` (wide hero) or the target ratio in the prompt itself, before styling. Deciding the crop after the look is locked gives the wrong crop family.

```
A rain-slicked city alley at night, neon reflections on wet asphalt, low camera angle, cinematic wide shot, generous dark sky in the upper third left clear for a headline, 16:9
```

Workflow for heroes: draft on Turbo to nail composition fast, iterate one field at a time, and reserve the text zone from the first draft rather than cropping it in later.

## Photoreal failure table

| Symptom | Cause | Fix |
|---|---|---|
| Pretty but empty image | style adjectives front-loaded over the subject | rewrite subject-first |
| Flat, un-photographed look | no light language | name the source, direction, and quality of the light |
| Plastic or dead skin | asked for realism with adjectives | name pore texture, vellus hair, catchlights; name the film stock |
| Materials look fake | surfaces unnamed | state each material (`wet stone`, `brushed steel`, `linen weave`) |
| Wrong crop | ratio chosen after styling | set the aspect ratio in the initial prompt |
| No room for the headline | no reserved negative space | add an explicit quiet zone for overlaid text |
| Register ignored, polished look persists | medium clause placed at the prompt's end | open with the medium clause (`amateur photo, ...`) |
| One element of a three-element scene missing | attention dilution at 8-step turbo | keep one act per zone; split three-element scenes into a series at 8 steps / CFG 1.0 |
| Two adjacent objects merge into one | simultaneous adjacent items in the same zone | separate the zones spatially, or give each object its own sentence and a color contrast |
| Second character renders as a stranger | cameo described by name only | full description (hair, eyes, build, clothes) in every prompt; composition order (`in the foreground`, `slightly behind her`) controls frame share |
| Blurred background people render mangled | too many named background figures | keep two or three background people, faces soft-focus |
| Drift after an edit | several fields changed at once | lock the subject, change one variable per iteration |

## Note on other Krea models

Settings here assume **Krea 2 Turbo in ComfyUI** (8 steps, CFG 1.0, shift 1.15). Do not paste in settings from FLUX.1 Krea [dev] (guidance 4.5, ~28 steps) or Krea 1 (hosted); they are different models and the numbers do not transfer. The prompting philosophy (natural language, concrete photography, anti-plastic) is shared across the family; the numeric settings differ per model.
