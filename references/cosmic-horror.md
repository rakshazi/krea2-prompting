# Cosmic Horror Reference

Use this reference for Cthulhu-like entities, eldritch gods, cosmic horror, unknowable organisms, sanity-breaking anatomy, and vast entities whose presence creates existential dread. This route inherits colossal-monster scale logic when the entity is giant, but adds an emphasis on ambiguity, non-human structure, and psychological unease.

## Core visual direction

Define a concrete physical scale even when the entity is metaphysically strange: `8,000 meters across`, `a dorsal ridge spanning several kilometers`, or `a mass rising into the upper atmosphere`. Give viewers enough visible structure to perceive scale, then introduce anatomy that resists ordinary classification: branching tendrils, nested eyes, breathing pores, irregular limbs, fleshy labyrinths, impossible symmetry, or partly concealed organs.

Use normal-sized biological units as surface detail: eyes, pores, suckers, scales, gills, veins, bone spurs, polyps, scars, or parasitic growths. At distance, these become claustrophobic grids and patterns. Keep the horror in visible material and spatial relationships rather than exposition about a fictional mythology.

## Composition and camera

- Reserve 10%-40% of the frame as negative space for an empty storm sky, black ocean, broken planet, fog, or barren ground. The empty area should isolate the entity and make the surrounding world feel fragile.
- For a giant entity, place human, vehicle, city, ship, or other scale references in the extreme far distance on the same depth plane; keep them below 0.1%-2% of the frame. Do not rely on a close foreground reference.
- Use `400mm-800mm super telephoto` for flattened, oppressive spatial compression and a surreal documentary feel. Use `10mm-24mm ultra-wide angle` for a deep abyss, impossible foreshortening, or aerial cosmic perspective.
- Choose one camera angle and preserve readable subject placement. Bird's-eye views can reveal a dorsal ridge or ocean pattern; ground-level low angles can make limbs and tendrils tower into the sky.
- Use haze, suspended particles, spray, smoke, dust, volumetric beams, or darkness to separate layers. Do not obscure all anatomy with an undifferentiated black blob.

## Materials, light, and color

Use physically legible organic materials: `necrotic skin`, `slimy flesh`, `wet translucent membranes`, `ancient rough carapace`, `pulsating veins`, `oozing pores`, `decayed tissue`, `mucous sheen`, and `dripping tendrils`. Lighting can be cold cyan against deep blue, sickly green against black, dying amber through dust, or bioluminescent color in a lightless abyss. Specify where highlights, shadows, reflections, and atmospheric scattering fall.

Prefer dread signals such as an impossibly quiet horizon, a tiny city under a vast shadow, a perfectly reflective black sea, a fractured planet surface, or a sky with no familiar celestial order. Avoid making the entity merely a conventional monster with tentacles if the user asks for cosmic horror; include an unfamiliar spatial or anatomical relationship.

## Prompt skeleton

```text
A photorealistic cinematic [shot] of an unknowable cosmic entity, [concrete dimensions], rising from [environment]. From an extreme far distance with a [lens] at [angle], the frame reveals [readable section], while [other mass] disappears into [fog/sky/ocean/frame edge]. Reserve [percentage] as negative space for [empty environment]. Its surface is a dense and disturbing field of normal-sized [eyes/pores/tendrils/etc.], with [organic material response]. At the far base on the same depth plane, [tiny reference] is barely visible. [Light, palette, atmosphere, and existential mood].
```

## Negative prompt additions

These apply on the RAW / live-negative path. At Turbo CFG 1.0 negatives are inert; restate the target positively or use `Krea2PromptWeight` negative weights.

```text
ordinary monster design, familiar animal anatomy, no sense of scale,
no environmental negative space, foreground scale reference, clean generic skin,
random tentacle clutter, overexposed blob, messy nebula, ordinary sky,
cartoon, anime, 3D render, CG, game screenshot, watermark, logo
```

Keep `text` in the list when no text is wanted; drop it when typography is intended. For a pure-organic cosmic entity, also apply the pure-organic reference and remove any negative that conflicts with a user-requested aesthetic.
