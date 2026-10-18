# Pure Organic Monsters Reference

Use this reference only when the user explicitly requires a 100% biological, purely organic, or non-mineral/non-mechanical giant monster. It is stricter than the ordinary colossal-monster route.

## Non-negotiable constraints

1. The subject is entirely biological and fictional. Use flesh, muscle, skin, keratin, bone, hair, scales, chitin, mucous, glands, vessels, pores, membranes, cartilage, and other organic tissue.
2. Do not use names of known real animal species anywhere in the monster description, analogy, or scale reference. Avoid species-based comparisons and use morphology instead: `multi-limbed`, `heavily furred`, `chitin-plated`, `many-eyed`, `long-bodied`, `winged`, `tendril-covered`, or `vertebrate-like` only if the wording does not introduce a concrete species.
3. The monster body must not contain metal, rock, soil, crystal, magma, machinery, concrete, glass, vehicles, architecture, or other inorganic materials. The environment may contain them; the body may not.
4. Use an inorganic scale reference only: vehicles, trains, excavators, skyscrapers, ships, aircraft carriers, industrial equipment, or other built objects. Place it at the far base/on the same extreme depth plane and keep it below 0.1%-2% of the frame.
5. Reserve 10%-40% of the frame as environmental negative space. The monster can be fully visible or shown as a major section, but it must not fill every pixel.
6. Put the monster in the far scene and use large-perspective language. Make the camera angle and lens serve scale rather than using a close-up that turns the subject into an ordinary creature.
7. The output is fluent English prose and uses real photographic/cinematic language. Do not use `anime`, `3D`, `CG`, `render`, `UE5`, or renderer terms for this branch.

## Scale and biological density

Give exact exaggerated dimensions such as `6,000 meters tall`, `8,000 meters long`, or `a central mass several kilometers across`. Build micro-scale density from ordinary non-specific units: millions of aligned scales, dense follicles, interwoven vessels, respiratory pores, keratin plates, oozing glands, scar tissue, exposed bone structures, and viscous membranes. These small units should read as a vast biological terrain at a distance.

Do not confuse a pure-organic monster with an organic-looking building or a mechanical creature with flesh accents. Every described part of the body must remain biological, even when the surrounding environment is industrial, urban, maritime, or planetary.

## Prompt skeleton

```text
A photorealistic cinematic [shot] of a colossal purely biological entity, [specific morphology and dimensions], occupying about [percentage] of the frame. Captured from an extreme far distance with a [lens] at [angle], the image reveals [complete form or major organic section], while [other body dimension] extends beyond [edges]. Reserve [percentage and location] as negative space for [environment]. Its body is made entirely of [organic tissues], with millions of normal-sized [biological units] forming a dense honeycomb of [surface texture]. At the distant base on the same far depth plane, [inorganic reference object] occupies less than [percentage] and appears microscopic. [Light, atmosphere, color, material response, documentary mood].
```

## Allowed environment wording

The restriction applies to the monster body, not the setting. The scene may include `concrete ruins`, `rocky ground`, `metal infrastructure`, `a city skyline`, `an aircraft carrier`, `ocean water`, `snow`, or `dust`, provided each is clearly environmental or a distant inorganic reference object. Keep the grammar unambiguous: `the creature stands above the concrete plain` is acceptable; `concrete plates cover its body` is not.

## Negative prompt additions

These apply on the RAW / live-negative path. At Turbo CFG 1.0 negatives are inert; restate the target positively or use `Krea2PromptWeight` negative weights.

```text
known animal species, recognizable real animal, animal comparison,
inorganic body material, metal anatomy, stone anatomy, mechanical parts,
crystalline body, magma body, monster made of machinery, ordinary creature scale,
creature filling the entire frame, no environmental negative space,
biological scale reference, foreground scale reference, close-up monster,
cartoon, anime, 3D render, CG, game screenshot, watermark, logo
```

If a user's requested monster necessarily names a real species or uses a real animal as the reference, explain that it conflicts with the pure-organic branch and either generalize the morphology or switch to `colossal-monsters.md`. Do not silently keep the forbidden species name while claiming strict compliance.

## Overlap with cosmic horror

A pure-organic cosmic-horror entity inherits the organic ban, inorganic reference-object rule, far-distance composition, and photography-only style. It may also use eldritch anatomy, nested eyes, tendrils, pores, impossible symmetry, and existential dread from `cosmic-horror.md`, as long as the subject remains entirely biological and no forbidden real species names appear.
