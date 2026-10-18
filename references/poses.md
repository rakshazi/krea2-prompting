# Krea 2 Pose System

A structured, anatomically explicit way to specify a figure's pose across eleven named fields, credited to [@Zuanfilm](https://x.com/Zuanfilm).

## The idea

Naming a pose (`"crossed arms"`) gives the model a fuzzy prior. Krea 2's Qwen3-VL encoder can parse structured, anatomically explicit description, so you specify the pose the way a life-drawing instructor or an animator would, across eleven independent fields. The model then has no room to improvise a generic stance.

## The 11-field schema

Always in this order, one per line, each a complete sentence:

| Field | What it controls |
|---|---|
| `leg_position` | Foot placement, stance width, knee flexion |
| `arm_position` | Upper-arm and elbow geometry |
| `hand_position` | Finger detail, grip, contact points |
| `torso_orientation` | Spine, chest, shoulder line, rotation |
| `head_orientation` | Head tilt, chin level, gaze direction |
| `weight_distribution` | Which leg/limb bears load, and how much |
| `center_of_gravity` | Where mass sits relative to the support base |
| `muscle_tension` | Minimal to very high; drives visible anatomy |
| `movement_quality` | The adverbial character: "explosive", "elegant", "reserved" |
| `balance` | Static stability vs. dynamic gait |
| `silhouette` | The read at thumbnail size, the highest-leverage field |

The `Pose:` heading names the block; the eleven fields follow.

**Usage pattern:**

```
Pose: Crossed Arms

leg_position: ...
arm_position: ...
...
silhouette: ...
```

Or, to bias the whole block harder with `Krea2PromptWeight`: `(Carrying a goat Over Shoulder:1.2)` followed by the descriptors.

## Adapting a pose to your subject

A worked example takes stock pose **46 Carrying Over Shoulder** and substitutes the object:

> `(Carrying a goat Over Shoulder:1.2)`
> `arm_position: One arm supports **the goat** over the shoulder while the opposite arm balances naturally.`
> `hand_position: Firm grip securing **the goat**.`
> `silhouette: Asymmetrical silhouette emphasizing **the elevated goat**.`

Swap the noun in the two or three fields that touch it and leave the biomechanics untouched. The physics stay correct; only the referent changes.

## Which fields matter most

If you're trimming for prompt budget, keep these four:

1. **`silhouette`**: determines whether the pose reads at all.
2. **`weight_distribution`**: the difference between a figure standing and a figure *pasted* standing.
3. **`torso_orientation`**: controls the whole upper-body read.
4. **`movement_quality`**: cheap adverbial steering that colours everything else.

Drop `center_of_gravity` and `balance` first; they're the most redundant with `weight_distribution`.

## The taxonomy

The source library is organized as 30 groups of ten poses (300 total). This reference ships three of those groups:

| Group | Name | Poses |
|---|---|---|
| 1 of 30 | Fundamental Standing Poses | 1-10 |
| 2 of 30 | Locomotion & Transitional Poses | 11-20 |
| 5 of 30 | Object Interaction & Force Poses | 41-50 |

Groups 3, 4 and 6-30 (poses 21-40, 51-300) are **not included.** The three included groups live in [`pose-library.md`](pose-library.md); the rest are implied by the numbering. When you need a pose that isn't there, write it yourself against the 11-field schema; that is the whole point of the schema being explicit.

## The 30 poses

Full descriptor blocks live in [`pose-library.md`](pose-library.md). Copy-paste directly.

## Writing your own pose

Fill all 11 fields. Write each as a full declarative sentence. Two conventions from the pose library worth copying:

- **Describe state.** Write the body's configuration as a fact: "Feet parallel at shoulder width." Avoid the instruction form "place the feet at shoulder width."
- **Quantify when you can.** "Approximately 80% on the supporting leg", "elbows bent approximately ninety degrees", "hips lowered below knee level."

## Field findings from explicit-scene testing

- **Prose beats schema for explicit scenes.** All 70+ test renders used plain natural-language pose clauses; the schema's value showed up indirectly: `seen from directly behind at bed level`, `hips raised on a pillow`, and `shoulders on the bench, hips raised high` are effectively inline torso/leg fields, and they rendered precisely. When a pose must be exact and the act leaves room to improvise, use the schema; when the act pins the geometry, prose contact clauses suffice.
- **Camera height biases garment state.** A low under-table camera pulled necklines open regardless of coverage wording; state `fully buttoned` for innocent tops under upskirt cameras.
- **Pose verbs lose to equipment nouns.** `mid-squat` with no station named landed her on the wrong machine; name the station (`in a squat rack`) plus the movement phase.
- **Garment processes do not render.** `pulling up`, `rolled midway`, `bunched at the calf` all collapsed to the worn state across nine arms; renderable states are fully on, fully off, in hand.
- **Over-shoulder glances are the strongest single pose instruction.** They held identity, face, and camera relationship across a dozen scenes and registers.
