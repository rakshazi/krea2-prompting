# Megastructure Reference

Use this reference for colossal architecture, megacities, orbital structures, impossible buildings, and architectural masses far beyond ordinary human scale. The intended result is photorealistic cinematic or documentary photography, never a 3D render or game screenshot.

## Hard definition

A megastructure is an architectural object or connected architectural complex whose scale is far beyond ordinary perception. Establish its size with concrete, exaggerated data such as `8,000 meters tall`, `hundreds of kilometers long`, or `a 4-kilometer outward projection`. Do not rely only on `huge` or `massive`.

The surface must contain normal human-scale components: windows, doors, balconies, pipes, vents, catwalks, maintenance units, signs, stairways, or small facilities. At the total scale, these components become dense lines, honeycomb grids, dot-like windows, and micro-industrial textures.

## Composition laws

1. Make one dimension or one major section complete enough to establish scale: for example, reveal the full 8,000-meter vertical height from foundation to summit, or a complete 4-kilometer cross-section of a central sector.
2. Let another dimension continue beyond the frame. State that the horizontal length, depth, tower field, underside, or chassis `extends infinitely` and `bleeds out of the left, right, top, or bottom edges`.
3. Do not frame the entire megastructure as a small isolated object. Do not let it fill 100% of the canvas.
4. Reserve roughly 10%-40% of the frame as explicit environmental negative space: sky, ocean, wasteland, planet surface, storm, or other non-architectural context. Name its location and content.
5. Place scale references at the far base or far distance on the same extreme depth plane as the megastructure, not in the foreground. Keep them tiny, typically below 0.1%-2% of the frame. Suitable references include trucks, skyscrapers, aircraft carriers, cruise ships, trains, excavators, or ordinary infrastructure.
6. If the user requests a complete isolated building with no negative space, obey the explicit user request and mention that it conflicts with this specialist scale convention only when the conflict materially affects the result.

## Camera and perspective

Most giant-scale scenes benefit from an extreme far-distance camera and a clear lens choice:

- `400mm-800mm super telephoto` for powerful spatial compression, flattened depth, dense surface detail, and a surreal architectural collage feel.
- `10mm-24mm ultra-wide angle` only when exaggerated depth, a dramatic foreground, or a distant aerial view is more important than compression.
- Make the camera angle serve the form: ground-level or low-angle for vertical mass, elevated or bird's-eye for deep structural layers, level telephoto for wall-like scale, and an aerial ultra-wide view for cliffside or planetary structures.
- Name haze, dust, fog, volumetric beams, or atmospheric scattering when far-depth separation is important.

## Prompt skeleton

Rewrite this into natural prose rather than copying it verbatim:

```text
A photorealistic cinematic photograph of a [specific megastructure], exactly [data], occupying about [percentage] of the frame. Captured from an extreme far distance with a [lens] from [angle], the image fully reveals [one complete dimension or section], while [another dimension] extends endlessly beyond [edges]. Reserve [percentage and location] as negative space for [environment]. Its surface is a dense field of millions of normal human-scale [components], forming [honeycomb/grid/micro-texture]. At the same distant depth plane, [tiny inorganic reference] occupies less than [percentage] near the base, making the scale physically legible. [Light, haze, palette, material response, documentary mood].
```

## Material and lighting vocabulary

Choose materials that fit the architecture: `weathered rough concrete`, `rusted steel`, `dark titanium`, `brushed metal`, `reinforced glass`, `ceramic panels`, `oxidized copper`, `salt-stained infrastructure`, or `dust-covered industrial plating`. Describe how light reacts: chipped paint catches hard sun, windows become a fine glittering grid, wet surfaces mirror neon, and fog separates structural layers.

Possible atmospheres include cold amber sunset, harsh midday light, neon cyan/magenta night, storm-lit cloud, dust storm, smog, snow, or pale salt-desert daylight. Use high contrast and atmospheric perspective to retain scale, but leave the specified negative space readable.

## Reference objects

The reference object must be ordinary and visually recognizable at a distance. Say both its location and its depth relationship:

```text
At the extreme distant base, on the same far depth plane as the visible structure, a convoy of heavy industrial trucks occupies less than 0.1% of the frame and appears as tiny dark marks.
```

Do not place a close-up person or foreground object next to a telephoto megastructure and call it a scale reference; that changes the perspective logic.

## Negative prompt additions

These apply on the RAW / live-negative path. At Turbo CFG 1.0 negatives are inert; restate the target positively or use `Krea2PromptWeight` negative weights. Use only relevant items, for example:

```text
ordinary building scale, isolated full object, structure filling the entire frame,
no environmental negative space, foreground scale reference, weak spatial compression,
flat empty facade, sparse surface detail, distorted perspective, warped architecture,
cartoon, anime, 3D render, CG, game screenshot, watermark, logo
```

The `cartoon/anime/3D render/CG` additions are appropriate because this branch explicitly requires real photography. Do not add them to a user-requested anime or illustrated giant architecture task unless the user also requests photorealism.
