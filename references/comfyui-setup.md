# ComfyUI Setup and Prompt Weighting

The files behind the Krea 2 Turbo graph, the RAW checkpoint, the optional prompt-weighting node, LoRA strength, and a troubleshooting table. Read this when wiring the graph, when a LoRA misbehaves, or when a prompt needs mechanical emphasis that words alone will not give. Sampler values are in the SKILL.md settings table.

## The pipeline

| Component | Recommended file | Note |
|---|---|---|
| Diffusion model | `krea2_turbo_fp8_scaled` (or `krea2_turbo_fp8`) | The 8-step distilled turbo checkpoint. |
| Text encoder | `qwen3vl_4b_fp8_scaled` (or `bf16`) | bf16 is higher precision and heavier on VRAM. |
| VAE | `qwen_image_vae` | The official pairing. |

The RAW (undistilled) checkpoint is a different job: 52 steps, CFG 3.5, up to 1024. Use RAW to train LoRAs and for slow exploratory variety; LoRAs trained on RAW transfer to Turbo. The guidance from the model authors is "train on RAW, run on Turbo".

**Tested long-run verdict:** pushing the turbo finetune to 50 steps / CFG 2.5 produced a noisy, texture-shredded frame instead of cleaner geometry (CFG above 1.0 doubles the forward passes per step, and the distilled schedule expects 8). Stay at 8 steps / CFG 1.0; handle multi-element scenes with one act per zone.

## Why the negative prompt is dead

At CFG 1.0 the negative term cancels out of the CFG equation, so a negative prompt has no effect. Steer through the positive prompt, or through negative weights (below).

## VAE troubleshooting

Some community workflows swap in a Wan-family 16-channel VAE. It runs, and colours or fine texture come out subtly wrong. Swap back to `qwen_image_vae` before chasing any other cause.

## Prompt weighting

Weighting is a **node feature**, absent from the base model. It comes from `Krea2PromptWeight` (ComfyUI-KJNodes), which does per-token attention-value scaling through the Qwen3-VL encoder. On the stock `CLIPTextEncode`, the `(word:1.3)` syntax shoves the entire sentence conditioning and the image falls apart past about 1.2, so install the node before relying on any of this.

**Wiring:** the node outputs both a patched `MODEL` and a `CONDITIONING`. Wire both. Feed the conditioning to the sampler but skip the patched model and the weights silently do nothing.

**Syntax:** `(keyword:number)`, parentheses and a colon. Every token starts at an implicit `1.0`.

| Range | Effect |
|---|---|
| `1.1` to `3.0` | Emphasis, increasingly forceful. `3.0` is already very strong. |
| `0.1` to `0.9` | De-emphasis without deletion. `(fog:0.4)` keeps fog subtle. |
| above `3.0` | Breaks the renderer: artifacts, blown contrast, oversaturation. |
| `-0.1` to `-5.0` | Inversion: pushes toward the opposite. |

**Negative weights are the useful part**, since the turbo path has no working negative prompt. `(anime:-2)` steers toward the photographic opposite of anime; `(face close to the lens:-4)` pushes the subject into the background; `(dark aesthetics:-3)` brightens the whole scene. Weighting inverts rather than deletes. Start at `-1`, escalate to `-3`, and treat `-5` as the practical floor.

**Global strength:** the node has a `strength` float (default `1.0`) that multiplies every weight in the prompt. Tune weights relative to each other, then dial `strength` to `0.6` to `0.8` if the whole image is over-driven. That is faster than re-tuning each weight.

**Weight sparingly.** Three to five weighted terms is a lot. Every weight added reduces the relative influence of everything unweighted, including the subject. Formatting traps: a stray or missing paren is a parse error rather than a silent skip, and weights do not nest.

## Enhancer node (experimental)

`Krea2T-Enhancer` (capitan01R) patches the text-fusion stage at runtime to raise prompt adherence. It is third-party and experimental, absent from the official pipeline, and it changes how hard all weighting bites. Bypass it to get a clean baseline before tuning anything else.

## LoRA strength

Slider-style LoRAs (the kind exported by slider training tools) behave differently from concept LoRAs, and that trips up the first test. Five things learned the hard way, at one fixed seed each:

**A slider's declared range describes its training scale, and the working band is narrower.** Metadata usually carries `slider_public_min`, `slider_public_max` and a scale factor, commonly ±5 with 0.6. Nudged to ±1 or ±1.5 the render comes back unchanged, which reads as a dead file. Push to ±3 or ±5 first to confirm the slider responds and which direction it moves, then settle back into the band that looks right. One measured pair: invisible at ±1.5, unmistakable at ±5. A rain-scene A/B then put the usable middle at +2.5, well short of the flood at +5.

**Test a LoRA in the scene it was trained for.** A wetness slider trained on rain and sweat does nothing in a dry bedroom, and floods the whole frame once pushed hard. The filename is a hint about the training set; the A/B is what tells you what the weights do.

**Colour bias scales with strength.** A concept LoRA near the top of its band drags its own palette in with it: anatomy that comes back flushed pink at 0.9 can match the surrounding skin at 0.7. Treat strength as a colour lever as well as a shape lever, and judge colour apart from form. When colour drifts warm as a LoRA is pushed, drop the strength and add the light and tone anchors from `references/photoreal.md`, "Skin tone and light temperature".

**Extremes move more than the target.** At the top of a slider range the framing, the crop and the pose can drift along with the attribute: one measured -5 run pulled the camera back and closed the legs halfway, on a seed where the ±5 pair for a different slider held the composition still. Score framing and the target attribute as two separate questions.

**Stacking two LoRAs pointed at the same trait adds little.** A concept LoRA at 0.9 beat the same LoRA at 0.6 plus a slider at -3. Two sources of the same instruction compete, and the sum reads flatter than either one at full strength.

Same seed is the instrument for all of this. With the seed fixed, composition holds still and only the changed variable moves, so a one-field change is readable. Queue the whole matrix up front, look at all of it together, then decide.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Image is pure noise or washed out | CFG at literal `0.0` in a standard KSampler | set CFG `1.0` |
| Oversaturated, distorted | CFG above ~1.5 | lower to `1.0` |
| Weights do nothing | patched `MODEL` output not wired to the sampler | wire both node outputs |
| Weights do nothing (part 2) | global `strength` too low | raise toward `1.0` |
| Artifacts, blown contrast | a weight above `3.0` | cap emphasis at `3.0`; work in `1.5` to `2.5` |
| Prompt parse error | stray or nested paren, missing colon | one level, colon required: `(word:1.5)` |
| `no X` in the prompt does nothing | no working negative branch at CFG 1.0 | use `(X:-2)` with the weighting node, or describe the positive target |
| Colours or texture subtly off | non-standard VAE | switch to `qwen_image_vae` |
| Soft, mushy detail | too few steps, or `simple` when the brief wants small detail | confirm 8 steps, and switch the scheduler to `beta` for illustration |

## Sources

- Official: [krea-ai/krea-2](https://github.com/krea-ai/krea-2) (natural language, long prompts, quoted text, Turbo 8/CFG 0/mu 1.15, RAW 52/CFG 3.5), [ComfyUI Krea 2 tutorial](https://docs.comfy.org/tutorials/image/krea/krea-2).
- Nodes: [Krea2PromptWeight (ComfyUI-KJNodes)](https://comfyai.run/documentation/Krea2PromptWeight), [SwarmUI issue #1441](https://github.com/mcmonkeyprojects/SwarmUI/issues/1441) (attention-value scaling, negative weighting without CFG), [capitan01R/ComfyUI-Krea2T-Enhancer](https://github.com/capitan01R/ComfyUI-Krea2T-Enhancer).
- Community: InstaSD and Civitai on the Qwen3-VL encoder, the CFG-1.0-in-ComfyUI fix, and weak negatives on the turbo path.
