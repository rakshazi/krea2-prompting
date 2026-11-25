# Krea 2 Core Reference

What a prompt should cover, text and lettering, staged props, figures and furniture, sorting a defect by seed sweep, character replacement, the identity block, composition modules, negative families, the resolution table, and turning a reference image into a prompt. Block order and the sentence frame are in SKILL.md.

## What to describe

Write like a photographer, art director, or concept designer. Start with the subject or scene. Avoid meta openers such as `In this image`. Before drafting, settle the aspect ratio and the task (generation, reverse engineering, character replacement, or prompt-only output), then pull these out of the brief:

- **Subject:** type, count, identity, placement, scale, silhouette, and the appearance anchors: hair, eyes, clothing, colour, props, surface anatomy.
- **Action and expression:** body direction, gesture, gaze, weight, contact, motion direction, emotion, visible consequences.
- **Composition and camera:** one shot size, one angle, one lens, the crop boundary, perspective, subject placement, foreground/midground/background, horizon or vanishing point, negative space, leading lines.
- **Environment:** real or imagined location, spatial depth, atmospheric conditions, how the environment interacts with the subject.
- **Light and colour:** source direction, hardness, shadow and contact behaviour, palette, contrast, haze, reflections, mood.
- **Material response:** particles, text, fabric weave, wet highlights, glass reflections, brushed metal, concrete, skin, hair, paper grain, water, smoke, and other physically visible responses.
- **Medium and aesthetic:** a concrete medium such as `editorial fashion photography`, `photorealistic landscape`, `retro science-fiction poster`, `Baroque oil painting`, or `screenprint collage`.

Let composition, relationships, light, and material behaviour carry the prompt. A few quality terms at the end are fine; they cannot replace the visual information.

## Character replacement and realistic integration

When replacing a person in a reference, preserve the composition, camera, palette, light, and mood. Replace only identity, appearance, clothing, and character-specific atmosphere. State at least hair, eyes, signature clothing/colours, expression, and a relevant prop; a name alone is too thin.

For an illustrated or anime character placed in a realistic environment, include `matching light, perspective, scale, contact shadows, grounded feet, reflections where appropriate, and atmospheric haze at distance`. Add integration negatives (fake compositing, mismatched lighting, wrong scale, floating character, no contact shadow, cartoon background) if a working negative path exists.

Do not describe off-frame wardrobe or props merely because they belong to the character's canon.

## Text and lettering

Two forms that letter cleanly:

```
The only large readable word in the image is "FIREFLY".
A small label in the lower right reads "GEOMETRY".
```

Short single words and brief titles render far more reliably than sentences. Specify placement, scale, font character, occlusion, and how the text integrates into the layout. Avoid vague `cool text`, many captions, or paragraph-length strings. Keep the picture or the joke readable without the lettering, because some renders will fail it: one can label came back as "SPAIM", mirrored and with extra strokes, as curved and angled surfaces do.

A label with no count comes back twice. `a small brass plate screwed to the counter reads "OMP"` rendered the plate on both ends of the counter, and `a small stitched patch on her apron reads "PI"` came back twice on the same apron. Both held once the prompt said `exactly one` and named the frame's other lettering.

A count holds the label and leaves its neighbours open. With both labels counted and the frame's lettering listed, "SHRED" still printed once on the lip of a blank card holder beside the shredder (1 of 18 renders), and tally strokes written for one card appeared on a second card in 2 of 8. Keep blank plates, placards and spare cards out of a frame that carries a label, or keep a seed without the copy.

A prop that carries a word is drawn large enough to letter it. `the stamp head as wide as her palm` came back as wide as her head in 8 of 8 renders once its face was turned square to the camera, so plan the composition around a large lettered prop.

**Speech bubbles.** A bubble is a text surface with the same limits: a few words letter cleanly, a full sentence does not. For a longer line, generate an empty bubble and set the text afterwards.

- Ask for the bubble in the composition: `one large blank cream speech bubble with a crisp charcoal outline hangs in the top quarter of the frame, its interior entirely empty with no lettering`. Drop that clause and the model fills the top of the frame with the character's head, leaving nowhere for a bubble.
- Fit the line to the bubble as drawn. Set the type at four to five percent of the image's long edge, two short lines for a wide bubble, with generous margins and a centred block.
- The tail is the fragile part. One seed draws a clean wedge, the next draws two isolated strokes with a gap, and a bubble crossing a hair or an ear can lose its edge. When the tail has to look right, redraw the bubble: a rounded rectangle plus a tail polygon between two base points, strokes on the two long sides only, and a fill a shade lighter than the paper so the tail reads as a solid shape.

**Screens and app UI.** A screen is the bubble problem one order of magnitude larger: a generated chat window, dashboard or terminal invents lettering, splits bubble tails, scatters stray labels and duplicates widgets, and rewording does nothing for the interface as a whole. Generate the scene with the screen area empty, then paste a real screenshot over it.

- Empty has to be spelled out as content. `a smooth plain charcoal header bar carrying no lettering`, `a message area that is completely empty warm cream from side to side and top to bottom, a single flat empty plane with no bubbles, no text, no avatars and no icons`, `a thin empty input bar lying along the window's bottom edge`. Drop those clauses and the panel comes back filled with the model's own bubbles.
- Keep the silhouette out of the paste zone. A hand resting on the panel's edge is covered by the screenshot and reads as a clipped limb. Leave a strip of bare paper between her and the window, and put her hands at her sides or on a prop outside the rect.
- Light theme prints into the paper: multiply the screenshot over the paper colour of the panel. White backgrounds vanish, grey bubbles read as ink, a colour accent survives as a tint. Flatten the panel to its paper colour first, otherwise the illustration's drawn bubbles show through the screenshot's white areas.
- Dark theme stays opaque and reads as a screen inside the drawn bezel: multiplied onto paper, a dark terminal turns to mud and its light text disappears.
- Rebuild the chrome the model cannot letter: a flat header band, the product pill, an empty input box with a send dot, drawn in the panel's own colours.

## Negative-prompt families

For the RAW path (CFG 3.5) or any pipeline with a live negative branch. On Turbo at CFG 1.0 they do nothing. Build only the families relevant to the image:

- **General:** `low quality, blurry, pixelated, jpeg artifacts, muddy colours, flat lighting, bad composition, distorted perspective, watermark, logo, text`.
- **People:** `wrong character, wrong hair colour, wrong eye colour, distorted face, asymmetrical eyes, bad anatomy, extra fingers, missing fingers, broken hands, deformed limbs, cropped face`.
- **Realistic integration:** `cartoon background, fake compositing, mismatched lighting, wrong scale, floating character, no contact shadow, unrealistic perspective`.
- **Landscape:** `empty scene, no depth, weak vanishing point, distorted trees, warped buildings, bad horizon, overexposed sky, dull colours`.
- **Poster text:** `misspelled text, random letters, too much text, unreadable typography, extra words, paragraph text, watermark, logo`.
- **High saturation:** `dull colours, muted palette, low saturation, washed-out colours, gray colour grading, muddy colours`.

Drop `text` from the negative list when the user wants generated text. Keep `watermark` and `logo` unless requested otherwise.

## Composition modules

Use these as ingredients, then rewrite them into the prompt's own grammar:

- **Vanishing point:** an empty road begins at bottom centre and leads to a distant central vanishing point, with tree lines, shadows, rails, and markings converging sharply.
- **Four quadrants:** four visual boundaries meet at the exact centre and divide the frame into distinct quadrants with different colour, texture, and light moods.
- **Action perspective:** an extreme low-angle wide-lens view places a huge foreshortened limb or object in the foreground while the face stays sharp near the upper third.
- **C-shaped motion:** a bright trail wraps from the lower-left foreground around the upper edge toward the right, creating a C-shaped motion path.
- **Reflection symmetry:** a centred figure or structure meets perfectly reflective water, mirroring sky and subject into symmetry.
- **Typography layout:** a single short word stretches across the background, partially occluded by the subject and integrated into a graphic poster.

## Resolution table

Choose the ratio first, then the size.

| Use | Ratio | Typical resolution |
| --- | ---: | ---: |
| Portrait / headshot | 1:1 | 1024x1024 or 1536x1536 |
| Cinematic landscape / hero | 16:9 | 1920x1080 or 2048x1152 |
| Panoramic tension | 21:9 | 2560x1080 or 3440x1440 |
| Broad action / environment | 4:3 | 1600x1200 or 2048x1536 |
| Vertical poster / wallpaper | 2:3 | 1536x2048 or 1440x2160 |
| Phone poster | 9:16 | 1080x1920 or 1440x2560 |

Keep dimensions divisible by 16. The 2048 training size is a per-side reference; the panoramic rows intentionally exceed it on the long edge. A larger canvas helps dense giant-scale or typography compositions; resolution alone cannot rescue a weak prompt.

## Reverse-engineering a reference into a prompt

When the user supplies an image to match:

1. **Analyse the visible facts.** Subject, count, composition, camera and lens feel, light direction and quality, palette, materials, medium, mood, aspect ratio. Record only what is visible.
2. **Write a faithful version.** A prompt that reproduces the visible facts, no invented objects.
3. **Optionally write an enhanced version.** Same locked composition, with stronger camera, light, material, and mood language. Do not change the framing.
4. **State the settings** in the SKILL.md output shape, with the resolution matched to the reference's aspect ratio.

## Character consistency across scenes

For a recurring character, build a reusable identity block: two or three sentences that name visible, checkable attributes such as hair, eyes, face shape, skin tone, build, signature clothing, and one countable marker (a scar, freckle patch, or tattoo). Reuse the block verbatim and change only the scene clauses.

- Place the block immediately after the medium clause, before scene content.
- Pin attributes that drift. State the tie height and its anchor point, the parting, or the mark's exact location in full. An unpinned hair tie rides low or morphs; an unpinned facial mark appears, vanishes, or moves.
- Keep scene state out of the block. Expression, flush, sweat, wetness, and lighting belong to the scene; a scene without its own state clause renders neutral.
- Use the same block and same seed for a continuity series; use the same block with a new seed for the same character in a fresh shoot.
- Nouns bind; intensifiers amplify. If a feature reads too strong, drop the intensifier before dropping the noun.
- Wardrobe continuity: name garment colors in every prompt, because a dropped colour word drifts (olive instead of black). Describe worn states (fully on, fully off, in hand) as fixed states. Long garments crossing a folded joint are fragile: stockings dissolve below the knee, a continuity clause helps, and knee-bent rear views stay fragile.
- The lower half needs naming: `a black hoodie with the sleeves pushed to the elbow over a white t-shirt` came back with an exposed hip and no bottoms at all.
- The garment decides the silhouette. An apron bib, a closed tunic or a buttoned coat across the torso flattens a curvy figure into a rectangle whatever the body clause says. A waist-tied apron, an open jacket or a fitted top keeps it. Name what hangs open and what sits close to the body.
- Framing carries build as much as words do. One identity block read as a slim generic girl when she stood small in a wide frame, and read as the canonical adult figure once she filled half the frame from ears to thigh.

Keep the block factual and visual. A name, a personality trait, or a backstory clause gives the model nothing to render.

## Staged props and deliberate artifacts

A prop that shares material with the character reads as anatomy. A detached hand in her own skin tone came back as her own hand or as an amputation, and the same hand in grey-green zombie skin with stitches and a torn cuff read as a prop on the first render.

- Give the prop a cue the character cannot share: wood, stone, grey-green zombie skin, stitches, a torn cuff, a handle.
- State the separation as something visible: `no arm above the cuff`, `a clear strip of cream paper between the cuff and her sleeve`.
- Keep the character's own anatomy counted and explicit: `her shoulders carry exactly one arm each`, `five fingers on the prop hand`.
- Keep the palette: one cool prop in a warm cream frame pulls the eye straight to the joke.
- The hand on the prop is the weak point. The ranked fixes are in `references/poses.md`, "Hands and held objects".
- **One object, one clause.** `a plain charcoal hand-cart on two small wheels, loaded with a tall leaning stack of cream paper scrolls` renders as one cart. Giving the handle its own clause (`with a tall upright handle at its back`) split the same cart into a thin trolley plus a separate box of scrolls on 3 of 5 seeds, and the single clause kept the cart whole in the 8 later renders reviewed. A prop with a body, a handle and a load is three chances to draw a second object: name the whole thing in one clause and let the render place its parts.
- **Paper props change shape.** `cream paper scrolls` renders either as tubes standing in a cart or as a stack of loose sheets, and neither reads as a rolled document. The loose end is the fragile part: spilled toward the camera it reads as a tongue hanging out of the cart, while the same paper hanging down a vertical side reads as a sheet. Keep one stack and at most one loose end, hung down a side rather than forward.

## Figures and furniture

A figure standing behind a table, desk, counter or bench that crosses the frame comes back fused with it. Whatever trails behind her (a tail, long hair, a coat hem) is drawn lying on the tabletop in front of her, or the top edge cuts her at the hip while her legs show on the near side.

- **Delete the furniture.** Move its props into her hands or onto the floor: a card held up at chest height, a box standing on the floor at his hip. Standing her beside the furniture is untested.
- **Wording that rendered clean:** `both characters standing side by side on a plain cream floor, cropped at the knees and fully clear of any furniture`, in a prompt that no longer named the bench anywhere.
- **Depth wording buys nothing.** Naming the camera side and placing the bench top in front of her hips left the fault on 4 of 4 seeds.
- **When the furniture has to stay,** sweep seeds and keep a clean one: the bench staging was clean in 3 of its first 6 renders.
- **Check the render at full size** wherever a figure meets furniture. A thumbnail hides the fault, and three fused renders passed a first review.

Receipt: a two-character illustration with a workbench across the lower third and both figures behind it. Fused in 3 of 6 renders, then in 4 of 4 with depth wording added, then clean in 8 of 8 once the bench was deleted and both props were hand-held.

**A doorway needs its door, its frame and its step.** `one tall rectangular doorway with one closed cream door in it, the door's face square to the camera and a small charcoal round knob at its right edge, a thin cream step across the threshold at its foot` reads as a building entrance. Named as a bare opening with a plate above it, the same gate came back as a plain wall with a sign on it, which reads as nothing at all. A window needs its inside too: a frame alone came back as an empty rectangle on 3 of the first 5 renders, and `a flat pale grey pane with a single vertical mullion` filled it in the 8 later renders. An awning described in prose rendered as a box bolted over the door on 2 of 2, so the step and the door frame carry the entrance on their own.

## Sorting a defect: prompt or seed

Render one prompt on four seeds before rewording it, then count the renders that carry the defect.

| The defect shows on | It belongs to | Fix |
|---|---|---|
| three or four seeds | the prompt | delete or restage the element that causes it |
| one or two seeds | the seed | keep a clean seed and leave the prompt alone |
| every seed, as a different wrong object each time | the model has no concept of that object | name a familiar object with the same job, or add the real tool in post: "When the object itself is missing", below |

What one eighteen-render illustration showed:

- Six single-seed rounds with one wording change each settled nothing. Each round traded one defect for another, and a seed-level defect was blamed on that round's edit, which was then reverted. Three four-seed batches settled the picture.
- Rewording lost both times it was tried against a defect that showed on most seeds: depth wording against fused furniture ("Figures and furniture", above), and `in the empty space between the two characters` against a wall stripe, which still crossed a head on 4 of 4 seeds.
- Seed-level in that set: a stray accessory mark from the reference sheet (5 of 12), marks copied onto a second card (2 of 8), a label copied onto a blank holder (1 of 18).
- A full-width background stripe lands at head height. `high on the wall`, with a halftone band `along the top edge of the frame`, moved it into the corners on 6 of 8 seeds.

## When the object itself is missing

A defect that comes back as a different wrong object on every seed is not a wording problem. The model is reaching for the nearest thing it has, and the thing the brief asks for is not in there, so a reworded tool moves the failure from a hammer head to a spear head to a walking cane without ever settling.

- **The tell:** one slot in an otherwise clean frame, an invented object in it every render, while the count, the grip and the placement clauses are all obeyed. Two or three different descriptions of the same object change which wrong shape appears and never produce the right one.
- **The fix:** name a familiar object that does the same job in the same place, and let the face, the pose and the setting carry the specific meaning. A hypodermic syringe, a chef's knife and a wooden spoon all exist for the model; a named specialty instrument usually does not.
- **When nothing familiar fits,** drop the prop and add the real object in post, exactly as a screen or a bubble is filled by hand. A prop the model cannot draw is a compositing job, and the prompt is the wrong tool for it.
- **Do not stack synonyms for the missing concept.** Three descriptions of the same unfamiliar tool in one prompt (`a lobotomy pick, an orbitoclast, a transorbital probe`) give it three anchors to blend, and the render mixes parts of all three.

Receipt: a lobotomy pick, wanted as a long slim steel rod with a small T-handle, on a comical doctor. Two wordings over sixteen renders produced a hammer-headed shaft, a harpoon with a bracket grip, a walking cane in two renders, a spade-tipped rod, a rod floating clear of the fist, a detached crossbar, a giant T-cane and a spear across the chest, and no render repeated a wrong shape. Re-prompted at the same seed, pose and hand with `one oversized hypodermic syringe`, the object read correctly on the first render.
