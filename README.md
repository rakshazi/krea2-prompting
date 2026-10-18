# krea2-prompting

I can run Krea 2 Turbo on my local hardware now, so I did the obvious thing: spent a stupid amount of time generating images and writing down what actually happened.

I ran it locally because paying a cloud provider by the hour to find out whether one adjective changes the anatomy is a bad business model.

This repo is the result. It is an agent skill for Krea 2 Turbo in ComfyUI: prompts, settings, pose blocks, style names, and a pile of "this wording works, this wording produces tasteful garbage" notes.

Prompting only. No models, no weights, no ComfyUI graph. Bring your own checkpoint.

To be clear: my day job is Go backend development. I don't have a Hugo Award in Prompt Engineering, and I'm not trying to win one. I just want the image to match the prompt.

## The take

Krea 2's text encoder is Qwen3-VL, so it reads sentences like a language model. Most prompt guides still hand you `masterpiece, best quality, 8k, ultra detailed`, then act surprised when the output looks like a stock photo from 2023.

This skill goes the other way: write what the camera sees, name the light, name the material, and stop stacking adjectives.

## About the AI thing

Yes, an AI wrote most of this. No, that doesn't make it another confident pile of prompt folklore. Fair question, though.

**Every "tested" claim comes from my own runs on my own hardware.** I ran Krea 2 Turbo locally, generated the images, compared seeds, and wrote down what broke. The skill documents actual behavior. A model's idea of what should happen doesn't make the cut. If something is untested, it says so. If you find a claim that smells like a hallucination, open an issue and bring a seed.

## How the tests worked

Same checkpoint, same seed, one variable per prompt. If a clause changed the image, it stayed. If the model ignored it, it went into the failure table with the exact wording that failed. That's the whole method. (Yes, it is slower than asking a chatbot. That's the point.) No vibes, no "I asked another model and it agreed with me".

## Examples

Ten topics, two passes by DeepSeek v4.1 Flash: one with only this README and the list of files as context, one with the entire skill loaded. [The examples gallery](./examples/README.md) has both renders side by side and both prompts for every topic. It is the fastest way to see what the skill actually changes.

## What's inside

Everything except `SKILL.md` lives in `references/`.

| File | What it does |
|---|---|
| `SKILL.md` | The entrypoint. Mental model, ComfyUI defaults, prompt order, core rules. Start here. |
| `photoreal.md` | Camera, lens, film, light, texture. Portraits, products, landscapes, architecture, heroes. |
| `krea2-core.md` | Deep architecture, negative families, poster text, composition modules, resolution table, reference reverse-engineering, character consistency. |
| `comfyui-setup.md` | Pipeline, the CFG 1.0 trap, `Krea2PromptWeight`, the enhancer, troubleshooting. |
| `poses.md` | The 11-field pose schema, usage, taxonomy, and the field findings. |
| `pose-library.md` | 30 ready-to-paste pose blocks. Copy, paste, stop inventing poses from scratch. |
| `styles.md` | 289 style names, four full examples, two authoring formulas. |
| `adult.md` | 18+. The explicit one. You know why you're here. |
| `megastructure.md` | Colossal architecture, megacities, orbital structures. |
| `colossal-monsters.md` | Kaiju, giant beasts, alien fauna. |
| `cosmic-horror.md` | Eldritch entities, impossible anatomy, dread. |
| `pure-organic-monsters.md` | Strictly biological giants. No metal, no mineral, no cheating. |

## The adult one

Let's get this out of the way: `references/adult.md` is the reason half of you are here. Spoiler: it is also the most tested part of the repo, because of course it is.

It is 18+, blunt, and explicit. Register control, plain anatomy, arousal, fluids, position geometry, per-limb contact, a 13-variant solo matrix, multi-person scenes, and a failure table for what Krea 2 actually renders versus what it politely ignores. It covers glamour and boudoir too, if you want the soft version. If you want the other thing, it doesn't blink.

The rule of the whole file: the model renders what you state and hedges the rest. Euphemism makes the image tasteful. Plain words make the image correct. That's the trade, and yes, it is exactly as awkward as it sounds when you write it down.

## The style index is an index

The `styles.md` file is 289 style names, four full paragraphs, and two formulas. The full 289-paragraph library lives in a workflow JSON on my machine, and I'm not going to pretend the repo contains text it doesn't. Use the names, steal the formulas, write the paragraph yourself.

## Install

Clone it into your agent's skills directory.

Claude Code:

```bash
git clone https://github.com/rakshazi/krea2-prompting.git ~/.claude/skills/krea2-prompting
```

omp:

```bash
git clone https://github.com/rakshazi/krea2-prompting.git ~/.omp/agent/skills/krea2-prompting
```

Any runtime that loads `SKILL.md` folders works. Drop the folder in, restart the session, done. You've installed harder things.

## Use

Ask for what you want:

- "Make a Krea 2 prompt for a rain-slicked neon alley at night, 16:9 hero crop."
- "Turn this reference photo into a prompt, keep the composition."
- "Give me a pose block for a figure carrying a goat over one shoulder."
- "Write an adult scene with the tested position geometry." (18+)

The skill gives you a positive prompt and settings. Your ComfyUI still has to render it; I can't do that part from a README. Add a negative prompt only when one specific artifact needs suppressing. At CFG 1.0 the negative branch is decorative.

## The short version

- Write sentences. Tag soup is a waste of Qwen3-VL.
- Lead with the subject. Order carries emphasis.
- Name the camera, lens, light, and material. `8k masterpiece` tells the model nothing about the light.
- CFG `1.0` in ComfyUI. The CLI's `0.0` will hand you noise.
- At 1.0 the negative branch is inert. State what you want.
- Change one variable per iteration, or you'll learn nothing.

## Credits, because none of this is mine

Krea 2 by [Krea AI](https://www.krea.ai/).
ComfyUI by the [ComfyUI project](https://comfy.org).
The basis for the skill is [buxinzi2233/krea2-prompting](https://github.com/buxinzi2233/krea2-prompting) (MIT).
The pose system is [@Zuanfilm](https://x.com/Zuanfilm)'s.
The style index came from public Krea 2 workflow notes.

I just ran the tests and wrote down what happened.

## License

Everything in this repo is [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The full text is in [`LICENSE`](LICENSE).

I don't care what you do with the skill. Run it, fork it, sell it, feed it to an agent, print it out and frame it. But I have opinions about open source, so SA it is. If you repackage it, the text stays open.

Generated images are yours. The license covers only the skill texts, while the output is outside its scope.

## TL;DR

- It is a Krea 2 Turbo prompting skill for ComfyUI.
- The adult file is explicit, tested, and 18+.
- Every "tested" claim is an actual local run. The AI wrote the prose; I generated the evidence.
- Clone it, ask for a prompt, stop guessing.
