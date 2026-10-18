# Colossal Monsters Reference

Use this reference for colossal fictional creatures, kaiju, giant beasts, alien fauna, mythic creatures, and enormous biological entities that are not necessarily subject to the strict pure-organic branch. Keep the visual language photorealistic and cinematic when this route is selected.

## Hard definition

A colossal monster is a non-ordinary creature whose scale is far beyond familiar biological size. Define it with concrete data such as `6,000 meters tall`, `8,000 meters wide`, or `a tail spanning several kilometers`. Give its anatomy a readable form: central torso, limbs, head, dorsal structures, wings, tail, fins, tendrils, or other major masses.

At least one surface system should be made of normal-sized biological units: scales, hairs, feathers, pores, barnacles, chitin plates, muscles, veins, bone spurs, glowing nodes, or respiratory openings. At colossal distance those units form dense honeycomb grids, lines, pores, and organic micro-textures.

## Composition laws

- The creature may be fully visible or shown as a major partial body section, according to the requested shot. If fully visible, preserve a readable silhouette and enough environment to prove scale.
- Never let the creature occupy every pixel. Reserve 10%-40% of the canvas as environmental negative space and specify its location: storm sky, ocean, snowfield, wasteland, deep sea, or alien terrain.
- Put scale references in the far distance or at the distant base on the same depth plane as the creature. Keep them tiny, normally below 0.1%-2% of the frame. Use people, vehicles, cities, skyscrapers, aircraft carriers, ships, or ordinary animals when the pure-organic branch is not active.
- Make the reference relationship explicit: `flattened against the distant base by lens compression`, `tiny marks beside the foot`, or `a miniature city at the far shoreline`. Never use a close foreground reference that makes the creature appear large only through ordinary perspective.

## Camera and perspective

- Use `400mm-800mm super telephoto` from an extreme far distance for spatial compression, flattened dread, and a monumental documentary feel.
- Use `10mm-24mm ultra-wide angle` for an aerial view, extreme foreshortening, or an exaggerated depth corridor when the composition calls for it.
- Select a coherent camera angle: ground-level or low-angle for towering limbs and silhouette, elevated/bird's-eye for dorsal ridges or ocean bodies, level telephoto for flattened scale, and dutch angle only when instability is specifically useful.
- Use atmospheric depth: dust, fog, spray, snow, suspended deep-sea particles, smoke, or volumetric light. Keep the negative-space region visible rather than burying the whole frame in effects.

## Prompt skeleton

```text
A photorealistic cinematic [shot] of a colossal [specific fictional creature], [specific dimensions], occupying about [percentage] of the frame. From an extreme far distance with a [lens] at [camera angle], the image reveals [complete form or major section], while [tail/limb/body] extends toward [horizon/edge]. Reserve [percentage and location] as negative space for [environment]. Its surface is a hyper-dense biological landscape of millions of normal-sized [scales/hairs/pores/etc.], with [material response]. At the distant base on the same depth plane, [tiny scale reference] occupies less than [percentage]. [Light, atmosphere, color, documentary mood].
```

## Material and mood choices

Use concrete physical responses: `rugged obsidian scales`, `thick coarse fur`, `scarred leathery hide`, `wet translucent membrane`, `ancient chitin`, `pulsating veins`, `bioluminescent nodes`, `mucous highlights`, `exposed porous bone`, or `steam from respiratory openings`. Match the palette to the mood: harsh amber apocalypse, cyan/deep-blue abyss, pale blizzard, red storm, or luminous warm daylight.

Avoid presenting a normal animal photograph as colossal unless the user explicitly wants a real animal enlarged. A giant creature should have an unmistakable fictional anatomy or otherworldly scale signal.

## Negative prompt additions

These apply on the RAW / live-negative path. At Turbo CFG 1.0 negatives are inert; restate the target positively or use `Krea2PromptWeight` negative weights. Select relevant terms:

```text
ordinary animal scale, no sense of scale, creature filling the entire frame,
no environmental negative space, foreground scale reference, weak anatomy,
flat skin, sparse surface texture, plastic skin, muddy silhouette, distorted perspective,
cartoon, anime, 3D render, CG, game screenshot, watermark, logo
```

Remove the style negatives when the user explicitly requests an illustrated, anime, or rendered monster. Keep scale and composition negatives if those remain desired.
