# Krea 2 Core Reference

Deep prompt architecture, the negative-prompt families, poster/typography rules, composition modules, the resolution table, and reverse-engineering a reference image into a prompt. The quickstart lives in SKILL.md; this is the detail behind it.

## 1. What to describe

Write like a photographer, art director, or concept designer. Start with the subject or scene. Avoid meta openers such as `In this image`. Cover:

- **Subject:** type, count, identity, placement, scale, silhouette, visible features.
- **Action and expression:** body direction, gesture, gaze, weight, motion, emotion, visible consequences.
- **Composition and camera:** shot size, crop, angle, lens, perspective, subject placement, foreground/midground/background, negative space, leading lines.
- **Environment:** real or imagined location, spatial depth, atmospheric conditions, how the environment interacts with the subject.
- **Light and colour:** source direction, hardness, shadow behaviour, palette, contrast, haze, reflections, mood.
- **Material response:** fabric weave, wet highlights, glass reflections, brushed metal, concrete, skin, hair, paper grain, water, smoke, and other physically visible responses.
- **Medium and aesthetic:** a concrete medium such as `editorial fashion photography`, `photorealistic landscape`, `retro science-fiction poster`, `Baroque oil painting`, or `screenprint collage`.

Let composition, relationships, light, and material behaviour carry the prompt. A few quality terms at the end are fine; they cannot replace the visual information.

## 2. Input checklist

Before drafting, silently extract:

1. Main subject, count, identity, scale.
2. Appearance anchors: hair, eyes, clothing, colour, props, surface anatomy.
3. Pose, action, expression, gaze, contact, motion direction.
4. One shot size, one camera angle, one lens/perspective, crop boundary, subject placement.
5. Environment, foreground/midground/background layers, horizon or vanishing point.
6. Light source and direction, shadow/contact behaviour, palette, atmosphere.
7. Materials, textures, particles, reflections, text, medium, mood, restrictions.
8. Aspect ratio, and whether the user wants generation, reverse engineering, character replacement, or prompt-only output.

For an image reference, separate observed facts from enhancement choices. A faithful output should not invent prominent objects the reference lacks.

## 3. Prompt architecture

Order the paragraph like this, adjusting to the task:

```
[medium or restrained quality] + [subject and identity] + [appearance, pose, action, expression]
+ [composition and camera] + [environment and spatial relations] + [lighting and colour]
+ [materials and micro-detail] + [aesthetic and mood] + [restrictions]
```

Reliable sentence frame:

```
A [medium/style] of [subject], [appearance and action], set in [environment]. The composition
uses [shot, angle, lens, perspective], placing [subject] relative to [frame and other elements].
Lighting comes from [direction/source] with [shadow and palette]. [Materials and micro-detail]
remain visible, creating a [mood] atmosphere. [Restrictions].
```

Use one or two coherent paragraphs. Make spatial relationships grammatical and explicit rather than listing disconnected nouns.

## 4. Character replacement and realistic integration

When replacing a person in a reference, preserve the composition, camera, palette, light, and mood. Replace only identity, appearance, clothing, and character-specific atmosphere. State at least hair, eyes, signature clothing/colours, expression, and a relevant prop; a name alone is too thin.

For an illustrated or anime character placed in a realistic environment, include `matching light, perspective, scale, contact shadows, grounded feet, reflections where appropriate, and atmospheric haze at distance`. Add integration negatives (fake compositing, mismatched lighting, wrong scale, floating character, no contact shadow, cartoon background) if a working negative path exists.

Lock the shot before writing clothing. Do not describe off-frame wardrobe or props merely because they belong to the character's canon.

## 5. Text and poster rules

Put short exact text in double quotes:

```
The only large readable word in the image is "FIREFLY".
A small label in the lower right reads "GEOMETRY".
```

Short single words and brief titles render far more reliably than sentences. Specify placement, scale, font character, occlusion, and how the text integrates into the layout. Avoid vague `cool text`, many captions, or paragraph-length strings. For text-focused work on a live-negative path, the typography negatives are `misspelled text, random letters, unreadable typography, extra words, paragraph text, watermark, logo`.

## 6. Negative-prompt families

Krea 2 Turbo runs at CFG 1.0, where the negative branch is effectively inert, so **state preferences in the positive prompt** for turbo work. The families below matter on the RAW path (CFG 3.5) or any pipeline with a live negative branch. Build only the families relevant to the image:

- **General:** `low quality, blurry, pixelated, jpeg artifacts, muddy colours, flat lighting, bad composition, distorted perspective, watermark, logo, text`.
- **People:** `wrong character, wrong hair colour, wrong eye colour, distorted face, asymmetrical eyes, bad anatomy, extra fingers, missing fingers, broken hands, deformed limbs, cropped face`.
- **Realistic integration:** `cartoon background, fake compositing, mismatched lighting, wrong scale, floating character, no contact shadow, unrealistic perspective`.
- **Landscape:** `empty scene, no depth, weak vanishing point, distorted trees, warped buildings, bad horizon, overexposed sky, dull colours`.
- **Poster text:** `misspelled text, random letters, too much text, unreadable typography, extra words, paragraph text, watermark, logo`.
- **High saturation:** `dull colours, muted palette, low saturation, washed-out colours, gray colour grading, muddy colours`.

Drop `text` from the negative list when the user wants generated text. Keep `watermark` and `logo` unless requested otherwise.

## 7. Composition modules

Use these as ingredients, then rewrite them into the prompt's own grammar:

- **Vanishing point:** an empty road begins at bottom centre and leads to a distant central vanishing point, with tree lines, shadows, rails, and markings converging sharply.
- **Four quadrants:** four visual boundaries meet at the exact centre and divide the frame into distinct quadrants with different colour, texture, and light moods.
- **Action perspective:** an extreme low-angle wide-lens view places a huge foreshortened limb or object in the foreground while the face stays sharp near the upper third.
- **C-shaped motion:** a bright trail wraps from the lower-left foreground around the upper edge toward the right, creating a C-shaped motion path.
- **Reflection symmetry:** a centred figure or structure meets perfectly reflective water, mirroring sky and subject into symmetry.
- **Typography layout:** a single short word stretches across the background, partially occluded by the subject and integrated into a graphic poster.

## 8. Resolution table

Choose the ratio first, then the size. Krea 2 was trained at 2048; generate native.

| Use | Ratio | Typical resolution |
| --- | ---: | ---: |
| Portrait / headshot | 1:1 | 1024x1024 or 1536x1536 |
| Cinematic landscape / hero | 16:9 | 1920x1080 or 2048x1152 |
| Panoramic tension | 21:9 | 2560x1080 or 3440x1440 |
| Broad action / environment | 4:3 | 1600x1200 or 2048x1536 |
| Vertical poster / wallpaper | 2:3 | 1536x2048 or 1440x2160 |
| Phone poster | 9:16 | 1080x1920 or 1440x2560 |

Keep dimensions divisible by 16. The 2048 training size is a per-side reference; the panoramic rows intentionally exceed it on the long edge. A larger canvas helps dense giant-scale or typography compositions; resolution alone cannot rescue a weak prompt.

## 9. Reverse-engineering a reference into a prompt

When the user supplies an image to match:

1. **Analyse the visible facts.** Subject, count, composition, camera and lens feel, light direction and quality, palette, materials, medium, mood, aspect ratio. Record only what is visible.
2. **Write a faithful version.** A prompt that reproduces the visible facts, no invented objects.
3. **Optionally write an enhanced version.** Same locked composition, with stronger camera, light, material, and mood language. Do not change the framing.
4. **State the settings** (resolution, aspect ratio, 8 steps, CFG 1.0, shift 1.15).

Never claim the reproduction was tested unless it was.

## 10. Character consistency across scenes

For a recurring character, build a reusable identity block: two or three sentences that name visible, checkable attributes such as hair, eyes, face shape, skin tone, build, signature clothing, and one countable marker (a scar, freckle patch, or tattoo). Reuse the block verbatim and change only the scene clauses.

- Place the block immediately after the medium clause, before scene content.
- Pin attributes that drift. State the tie height, parting, or mark location in full; an unpinned feature wanders.
- Keep scene state out of the block. Expression, flush, sweat, wetness, and lighting belong to the scene; a scene without its own state clause renders neutral.
- Use the same block and same seed for a continuity series; use the same block with a new seed for the same character in a fresh shoot.
- Nouns bind; intensifiers amplify. If a feature reads too strong, drop the intensifier before dropping the noun.
- Wardrobe continuity: name garment colors in every prompt; describe worn states (fully on, fully off, in hand) as fixed states; long garments crossing a folded joint are fragile.

Keep the block factual and visual. A name, a personality trait, or a backstory clause gives the model nothing to render.
