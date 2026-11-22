# Krea 2 Inpainting and Masked Edits

A masked edit on Krea 2 runs through an edit LoRA and the Ostris edit encoder, and the mask is painted into the reference image as a black fill. That design choice drives the rest of this file: the model sees the whole frame with a hole in it, so the prompt describes the whole finished picture while the size of the hole says how much of that picture may move.

## The stack that works

| Piece | What it is | Why it is required |
|---|---|---|
| `krea2_inpaint_edit_v2_17500.safetensors` | adapter trained for masked edits, ai-toolkit, on Hugging Face | without it the edit encoder repaints the frame instead of the region |
| `Krea2OstrisEditModelPatch` | wraps the model, `kv_cache: true` | the encoder feeds the reference at the first timestep only |
| `TextEncodeKrea2OstrisEdit` | takes `clip`, `vae`, `image1` (the black-filled image) and the prompt | this is the conditioning the sampler reads |
| negative branch | the same edit encoder, or `ConditioningZeroOut` off the positive | a bare `CLIPTextEncode` there breaks the pairing |
| sampler | 8 steps, CFG 1.0, denoise 1.0 | see Settings in `SKILL.md` |

Two constraints are easy to miss: the target size equals the source, and it stays at or under one megapixel for the edit pass. A resolution that disagrees with the source either rescales the picture or shrinks the region.

`SetLatentNoiseMask` with a stock Krea 2 checkpoint is the obvious alternative and it does not work: partial denoise returned plaster texture and collapsed forms on both flat-colour and photoreal input. Skip it and use the adapter.

## The rule that governs everything

**The prompt is global, the mask only frees pixels.** Every clause in the sentence applies to the whole canvas. The black area says where repainting is allowed, nothing more.

Ask for more volume than the hole can hold and the difference shows up outside it. Ask for something that fits inside the hole and it stays there. So write the finished picture, then choose the box:

- Change one structure: cover that whole structure, both sides of a symmetric feature, with a few pixels to spare.
- Change one small motif: a box around the motif holds, because the change fits inside it.
- The same sentence with a wider box produces a bigger change at the same seed. Box size behaves as a magnitude dial.

Prompt deltas ("add a tattoo") behave worse than descriptions of the finished frame ("a small black cat tattoo on her left hip, everything else as in the reference").

## Removal

Removal works, with one hard condition: **the prompt must not mention the object at all.** At CFG 1.0 the negative is dead (see `references/comfyui-setup.md`), so "no choker, no necklace" carries no weight, and a leftover mention of the choker in the base description will actively put it back. Write the finished picture without the object, keep every other clause intact, and cover the whole object with the box.

## Contradictions resolve toward the mention

Two clauses that disagree settle in favour of the one that names the thing. "Black choker" in the identity block plus "her neck is bare" in the change sentence returns the choker. When an edit refuses to take, re-read the prompt for the object before changing anything else.

## What a mask can and cannot do

- **It re-renders in place.** Asking for a new hand gesture returns the hand in the same place with different fingers. Nothing in the frame moves to accommodate the request.
- **Moving anatomy needs a whole-frame regeneration.** A pose change means blackening the entire frame, writing a fresh prompt, and accepting a new generation; identity then comes from the prompt, because the reference is gone.
- **Two separate regions work in one pass.** Two boxes, one sentence describing both changes, no bleeding between them.
- **Flat graphics land, hardware does not.** Tattoos, prints, and text-free silhouettes come out clean. Barbells, piercings, buckles and straps come out as stray beads or invented shapes. Leave jewellery out of a masked edit, or expect to fix it.

## Framing the black fill

The fill is content, so it bleeds at the frame border. A box that runs to the edge of the canvas comes back as a dark rounded rectangle hugging the subject. Two ways out:

- Keep a real margin of untouched pixels on all four sides. Photographs with a background make this easy.
- For whole-figure work, blacken the entire frame so no internal boundary exists.

Feather is for blending, kept small, roughly 2 to 9 px. A large feather turns the fill into a gradient and the model paints the gradient.

## Where detail comes from: crop, re-render, composite

One pass at one megapixel gives a region roughly 40 px of room at full-body scale, which reads as a patch. For detail, work in three steps:

1. Crop the region to a 3:4 or 2:3 window, giving it most of the frame, and upscale it to the edit size.
2. Run the masked edit on the crop, with the mask inset from the crop edges.
3. Paste the result back into the parent image at the crop rectangle, **through the mask**, so the crop border never shows.

At three to four times the pixel density the same prompt invents detail the full-body pass cannot. This is the standard route for faces, eyes, hands and explicit anatomy, and the pasted result ends up denser than the parent frame.

A zoomed face is where the model's own beauty prior takes over: big glossy eyes, airbrushed skin. The photography anchors in `references/photoreal.md` are what pull it back toward a real face.

## Photoreal and explicit work

- **Structure survives, texture flattens.** Enlarging a form or removing a garment keeps lighting, tone and colour. The repainted area comes back smoother than the photograph, with grain and pore detail gone. Adding grain and pore cues to the sentence about that area helps a little; masking a smaller region helps more.
- **Fine texture additions fail.** Chest hair, stubble, freckles and small scars are beyond one pass at this scale.
- **Explicit anatomy needs the frame.** Breasts read correctly inside a full-body frame. Genitals at that scale come back as a smooth patch, so put them in a crop and let them fill it. Once the region is the frame, the render is stable across seeds.
- **Explicit detail pulls the style toward airbrush.** Say the style out loud in the prompt, and keep saying it, or the region drifts away from the rest of the picture.
- **Garments have to be masked too.** A mask over the torso leaves the sleeves standing on bare shoulders: darken every part of the outfit that has to go.

## Failure table

| Symptom | Cause | Fix |
|---|---|---|
| The change is bigger or smaller than asked | box size against a global sentence | cover the structure you want changed; keep unrelated subjects out of the sentence |
| The object is still there after removal | a mention survived in the prompt, or the box left part of it visible | drop every mention, cover the whole object |
| Something appeared in the wrong place | the change was written as a delta | describe the finished frame with the detail in it |
| The region looks flatter than the photograph | full repaint at denoise 1.0 | smaller box, grain and pore cues, or accept it |
| Big glassy eyes after a face crop | the model's beauty prior | photography anchors from `references/photoreal.md` |
| Jewellery, buckles or straps come out wrong | hardware is a weak class | flat graphics and fabric instead, or drop it |
| A dark rounded frame around the edit | the fill touched the frame border | margin on all sides, or fill the whole frame |
| Two subjects in the frame and both changed | the sentence named both | one subject per sentence, one box per change |

## Related

- `references/reference-images.md` for the edit encoder, reference wiring and the layout split.
- `references/photoreal.md` for skin, grain and the anti-plastic anchors.
- `references/adult.md` for explicit content in general.
- `references/comfyui-setup.md` for why the negative prompt is dead and how LoRA strength behaves.
