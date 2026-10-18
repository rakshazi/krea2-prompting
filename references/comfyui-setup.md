# ComfyUI Setup and Prompt Weighting

The ComfyUI pipeline for Krea 2 Turbo, the CFG explanation, the optional prompt-weighting node, and a troubleshooting table. Read this when wiring the graph or when a prompt needs mechanical emphasis that words alone will not give.

## The pipeline

| Component | Recommended file | Note |
|---|---|---|
| Diffusion model | `krea2_turbo_fp8_scaled` (or `krea2_turbo_fp8`) | The 8-step distilled turbo checkpoint. |
| Text encoder | `qwen3vl_4b_fp8_scaled` (or `bf16`) | bf16 is higher precision and heavier on VRAM. |
| VAE | `qwen_image_vae` | The official pairing. |
| Sampler / scheduler | `euler` / `simple` | Official default. |
| Steps | `8` | Turbo is distilled to 8. |
| CFG | `1.0` | See below. |
| Shift (mu) | `1.15` | Set on the ModelSampling node (timestep shift). |
| Resolution | Native 2048; minimum 1024; divisible by 16 | Panoramic ratios widen the long edge. |

The RAW (undistilled) checkpoint is a different job: 52 steps, CFG 3.5, up to 1024. Use RAW to train LoRAs and for slow exploratory variety; LoRAs trained on RAW transfer to Turbo. The guidance from the model authors is "train on RAW, run on Turbo".

**Tested long-run verdict:** pushing the turbo finetune to 50 steps / CFG 2.5 produced a noisy, texture-shredded frame instead of cleaner geometry (CFG above 1.0 doubles the forward passes per step, and the distilled schedule expects 8). Stay at 8 steps / CFG 1.0; handle multi-element scenes with one act per zone.

## The CFG value

The official command-line inference uses `--cfg 0.0`. A standard ComfyUI KSampler treats literal `0.0` as pure unconditional output, which breaks the image, so in ComfyUI set **CFG `1.0`**. Above roughly `1.5` the image oversaturates and distorts. At CFG 1.0 the negative term cancels out of the CFG equation, so a negative prompt has no effect; steer through the positive prompt, or through negative weights (below).

## VAE troubleshooting

If colours or fine texture look subtly wrong versus a reference, the VAE is the cheapest variable to check first. Some community workflows swap in a Wan-family 16-channel VAE; it runs, but the official pairing is the Qwen-Image VAE. Swap back to `qwen_image_vae` before chasing any other cause.

## Prompt weighting (optional node)

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
| Soft, mushy detail | too few steps or wrong scheduler | confirm 8 steps, `euler`/`simple`, shift `1.15` |

## Quick reference card

```
TURBO (ComfyUI)   8 steps · CFG 1.0 · shift(mu) 1.15 · euler/simple · 1024-2048px
RAW               52 steps · CFG 3.5 · <=1024px · train LoRAs here, run on Turbo
FILES             krea2_turbo_fp8_scaled · qwen3vl_4b · qwen_image_vae
TEXT              put words to render in "quotes", keep short
NEGATIVES         near-inert at CFG 1.0 · steer positive, or use negative weights
WEIGHTS (node)    (kw:1.1-3) emphasize · (kw:0.1-0.9) soften · (kw:-1..-5) invert
                  >3.0 breaks · wire BOTH model + conditioning · strength = master gain
```

## Sources

- Official: [krea-ai/krea-2](https://github.com/krea-ai/krea-2) (natural language, long prompts, quoted text, Turbo 8/CFG 0/mu 1.15, RAW 52/CFG 3.5), [ComfyUI Krea 2 tutorial](https://docs.comfy.org/tutorials/image/krea/krea-2).
- Nodes: [Krea2PromptWeight (ComfyUI-KJNodes)](https://comfyai.run/documentation/Krea2PromptWeight), [SwarmUI issue #1441](https://github.com/mcmonkeyprojects/SwarmUI/issues/1441) (attention-value scaling, negative weighting without CFG), [capitan01R/ComfyUI-Krea2T-Enhancer](https://github.com/capitan01R/ComfyUI-Krea2T-Enhancer).
- Community: InstaSD and Civitai on the Qwen3-VL encoder, the CFG-1.0-in-ComfyUI fix, and weak negatives on the turbo path.
