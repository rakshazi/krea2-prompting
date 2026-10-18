# Adult / NSFW Photography Reference

Prompting levers for adult glamour, boudoir, pin-up, editorial nude, and explicit photography on Krea 2 Turbo. Adult content, 18+ only. The same realism discipline as `photoreal.md` applies: name the camera, the light, and the skin. On top of that, explicit work has one governing rule, verified on Krea 2 NSFW finetunes (same-seed A/B at 1152x1536, 8 steps, CFG 1.0; base-model behavior may differ):

**The model renders exactly what is stated and hedges the rest.**

## The explicitness rule

The image contains what the prompt states, nothing more. "Clearly aroused and exposed" produces a tasteful reclining nude with the hips angled away. "Her pussy fully visible with parted labia, visibly aroused and wet" produces the shot, same seed, same light, anatomy correct. Euphemism ("womanhood", "intimate area", "barely covered") reads as an instruction to keep distance. Write like a director describing what the camera sees, in plain adult words, and state both the body's parts and their state.

## Register control

Name the register in the medium clause so the model targets it:

- **Glamour / boudoir:** suggestive, clothed or lingerie. `boudoir photography, silk lingerie, warm low light, intimate mood`.
- **Pin-up:** stylized, playful, retro. `1950s pin-up, playful pose, saturated retro palette, studio strobe`.
- **Editorial / fine-art nude:** composition-led, gallery register. `fine-art nude study, sculptural side light, matte skin, muted palette, film grain`.
- **Explicit:** say it plainly and describe anatomy and action directly. Euphemism and hinting actively pull the image back toward soft-focus.

## Vocabulary

**Anatomy, plain nouns.** Female: `vulva, labia majora, labia minora, clitoris, vaginal opening, mons pubis, perineum, anus`. Male: `penis, glans, shaft, foreskin, testicles`. Colloquial words (`pussy`, `cock`, `cum`, `asshole`) bind just as well; many NSFW LoRAs are trained on exactly those tokens. Pick one register and stay consistent inside a prompt.

**Arousal state (nude vs erotic).** Without arousal cues the face and body read neutral: `erect nipples, flushed chest and cheeks, parted lips, heavy-lidded eyes, glistening wetness on the labia, arousal slick on the inner thighs, swollen lips, trembling thighs, post-orgasm flush`. Add at least one arousal cue any time the register is above boudoir.

**Solo acts.** Name the toy, the orifice, and what the hand does; see the solo matrix for tested phrasings and their failure modes. Working starting points: `two fingers inside her pussy, knuckles visible`, `fingertips circling her swollen clitoris` (pressing still reads fine), `a thick glass dildo inside her pussy, the shaft glistening`, `a hot pink vibrator above her entrance, at the hood of her clitoris`, `a slim glass toy inserted in her tight asshole` (rear or side angle required), `grinding against the edge of the armrest`.

**Positions (partnered).** Name the position, then lock the geometry with contact points; concrete geometry is what the model renders reliably:

- Classic cowgirl: `the man lies on his back, the woman straddles his hips facing him, knees bent beside his ribs, hips pressed down, his cock fully inside her pussy with only the base visible from this angle`.
- Reverse cowgirl: same seat, `facing his feet, leaning forward on her hands, his cock visible where it enters her from below, her back arched`.
- Missionary: `she lies on her back with her legs raised and parted, he supports his weight on his forearms between her thighs, their hips flush`.
- Doggy: `she is on all fours at the edge of the bed, back arched, chest low, he kneels behind her gripping her hips, penetration from behind, her ass raised`.

State `vaginal` when the orifice could be misread. State the positive target instead of `no anal`.

The doggy block above is verified end-to-end with wardrobe, toy, and fluids stacked on top (see the translation example). Multi-person scenes hold contact points while limb placement drifts; explicit position names alone carry nothing without the geometry clauses.

**Fluids and mess.** `thick white cum, ropes of cum across her stomach, cum dripping down her thigh, creampie dripping out of her pussy, saliva stringing between lips, oil sheen, film of sweat, wet spot on the sheets`. Literal beats hinted: `thick cum bubbling out of her hairy pussy` renders; "a messy finish" does not. Tested explicit renders: creampie pooling (`thick white cum pooling in her vaginal opening and dripping down her perineum onto the sheets`), squirting (`mid-squirt, a stream of clear fluid spraying from her pussy onto the sheets`), grool (`thick stringy grool`, a milky opaque discharge, its own trained look), and scooping (`scooping cum out of her gaping pussy, cum stringing between her fingers`). Fluid strings need a solid anchor (toy, held object); strings to her own labia fall unrendered.

**Body hair.** The base model defaults to sanitized, hairless bodies. Command it when it matters: `completely natural untrimmed bush`, `trimmed landing strip`, `fully shaved with faint stubble`. Same for men: `natural body hair, happy trail`.

## Multi-person rules

- Describe each person individually: `The first is a pale blonde with small breasts and cropped hair. The second is a curvy brunette with a mole on her thigh.` Without this the model clones one face across both bodies.
- Give every limb an owner and a contact point: `his left hand grips her right hip, her nails drag down his back`. Unassigned limbs merge or float.
- Use whole-body geometric angles (`wide side profile shot`, `45-degree rear angle`, `overhead looking down`) and add `full bodies visible` for acts. POV framing is the fastest route to floating limbs and missing bodies.

Tested on a two-person missionary scene (side profile, per-person descriptions, per-limb contact): faces stayed distinct, both bodies whole, penetration connected. Expect contact *points* to hold while limb *placement* drifts: her legs went up over his shoulder despite the prompt, a hand landed beside its target. Iterate limb placement one clause at a time on a fixed seed.

## Camera for explicit work

Shot size controls explicitness as much as wording does: wide reads environmental, medium shows the bodies, `close-up` isolates the act or the anatomy, macro pushes texture. A close-up also crops out hands and feet, the usual anatomy failure zones.

Camera register changes the whole feel, and it must live in the opening medium clause. Tested: `cheap smartphone camera, harsh direct flash` placed at the prompt's end left the polished lamplight look intact, because the front-loaded medium clause won. Put the register first:

- `Cheap smartphone camera photograph: harsh direct flash, blown-out highlights, deep harsh shadows` -> real-amateur realism.
- `90s camcorder still frame, grainy` -> candid/leaked aesthetic.
- `85mm f/1.8, soft bedside lamplight` -> polished erotic photography.
- `35mm, environmental, candlelight` -> cinematic intimacy.

`8k, masterpiece, cinematic lighting` pushes toward the sanitized AI look.

## Prompt architecture for explicit scenes

The SKILL.md block order with four changes: name the register in the medium clause, add a per-body detail block, put act, contact points, and arousal state before decoration, and drop the restrictions clause:

```
[medium + register] + [each body: build, skin, hair] + [act: who does what, contact points]
+ [arousal state] + [camera: angle, shot, lens] + [environment] + [light] + [skin/anatomy micro-detail] + [mood]
```

Keep the one-variable-per-iteration discipline: explicit scenes have more failure modes, so lock the geometry first, then layer state and fluids.

Worked example (tested on a Krea 2 NSFW finetune at 1152x1536; fixed seed). Single-subject prompts can fold environment into the opening clause and light into the camera clause; in multi-body scenes give every block its own sentence:

```
A photorealistic boudoir photograph of a naked adult woman lying on her back on an unmade bed,
knees bent and falling open, her pussy fully visible with parted labia, visibly aroused and wet,
erect nipples, flushed chest, one hand resting on her inner thigh, the other hand in her hair,
eyes half-closed, mouth slightly open in pleasure, soft warm bedside lamplight with deep shadows,
85mm f/1.8 shallow depth of field, natural skin texture with visible pores and a light sheen of
sweat, film grain
```

## Rear-view specificity

Rear-focused scenes (camera behind the subject, ass/pussy/anus in frame, face hidden or turned away) often need a different identity block and LoRA stack than front-facing scenes. The model renders exactly what is stated in the identity block and prompt. Describing front anatomy or loading front-facing LoRAs in a rear shot invites proportion artifacts or mixed views (face plus rear body, torso plus ass).

**Identity block for rear views:** include only attributes visible from behind or at the edge of frame: hair tie height and hair length, glasses if the side of the face is visible, skin tone, hip and shoulder shape, and any rear-visible anatomy. Omit face, bust, and front-only detail. If the face is described but hidden, the model may produce artifacted face overlays or mixed front/rear views.

**The clitoris placement problem:** Krea 2 does not reliably localize the clitoris. A toy aimed at it tends to land at the vaginal entrance, insert into the asshole, or float above the vulva without attaching. For rear-view scenes, avoid clitoris-targeting toys; use anal toys, fingering in the pussy, or fluids instead.

## Solo matrix (tested)

Thirteen same-seed variants (1152x1536, fixed seed, 8 steps, CFG 1.0, Krea 2 NSFW finetune): one fixed subject, one variable slot per prompt. The deltas below are prompt-to-prompt observations from this matrix.

**What obeyed.** Baseline clauses held in all 13: body type, wardrobe placement, arousal cues, hand placement, framing clause (`camera directly in front of her at bed height, her body filling the frame from shoulders to knees`). Fluids are the strongest renders in the set: `thick white cum pooling in her vaginal opening and dripping down her perineum onto the sheets` and a `mid-squirt` `stream of clear fluid spraying onto the sheets` both rendered exactly, stream physics and sheet wet spots included. Scooping and stringing combos rendered web-thick fluid.

**Contact verbs place things; depth quantifiers drift.** `Two fingers of her right hand are inside her pink pussy` put the fingers at the entrance spreading the labia rather than inside, because the neighboring clause `labia spread around them` outvoted `inside`. Spread verbs hijack the hand; when the hand should penetrate, keep `spread` away from it. `A thick glass dildo is halfway inside` rendered tip-at-entrance, and `her right hand gripping its base` was ignored (hand hovered beside it). "Halfway" is a weak concept; state which part of the shaft is hidden and which visible only when that detail matters, and expect shyness toward deep insertion.

**Targets above the entrance need aim clauses.** `A hot pink vibrator is pressed against her clitoris` landed the tip at the vaginal entrance; from a supine front angle the model places the clitoris near the entrance by default. Aim it: `above her entrance, at the hood of her clitoris`. `Circling her swollen clitoris` with fingertips placed fine, but the contact read as pressing in a still; motion verbs describe state, and animation comes from the still's tension cues.

**Anal insertion fails from a front-on supine angle.** `A slim glass toy is inserted in her tight asshole` with `hips lifted slightly off the bed` produced the toy resting under her perineum against the sheets. Two fixes, both verified: give the act a rear or side angle (see the doggy block), or enumerate the geometry explicitly. In a combo prompt, `both entry points visible between her spread thighs` made the same clause that failed solo render correctly, anal toy included.

**`grool` is a trained token with its own look.** Same-seed A/B: `thick stringy grool` rendered a thick, milky, opaque discharge welling from the opening, while `thick strings of arousal` rendered a thin clear glossy sheen. The token carries the fluid's visual properties, so keep `grool` in the prompt when that look is wanted. Fluid-to-own-anatomy attachment is weak: `stretching between her fingers and her swollen labia` was ignored, strings fell downward instead. Strings bind fluid-to-solid-object: in the combo, `thick stringy grool stretching between her fingers and the glass shaft` rendered the full web, fingers to shaft to labia.

**Combos amplify obedience.** The strongest renders in the set were multi-act combos (toy + grool strings, fingers + anal toy, creampie + scooping hand + sheet pooling). Enumerate every contact when stacking; the enumeration itself is what locks the geometry.

**Body build note.** A size intensifier such as `very large` renders exactly that; if the build reads too heavy, drop the intensifier rather than the noun (`large natural breasts`).

**Position modifiers need their own sentence.** `hips thrown up off the bed` and `hips lifted slightly` were dropped in 2 of 2 attempts when a strong fluid clause shared the sentence. Give the position its own sentence when it matters.

**Deep insertion wording (tested).** `the full length of its shaft buried inside her pink pussy, only the base and her stretched labia visible` rendered the deepest insertion of the session: shaft hidden, base and grip visible. Naming what stays visible beats depth adverbs: `only the base visible` outperformed `halfway inside`. A close framing clause (`close on her pussy, hips and thighs filling the lower frame`) plus the explicit shaft state delivered a textbook deep-insertion shot.

**Anal angles (tested, two geometries).** Both rear-angle geometries delivered true insertion on the tested finetune: all-fours with `seen from directly behind at bed level, her full body visible from head to knees` and prone with `lying flat on her stomach, legs together, a pillow under her hips`. In both, `clearly visible between her cheeks` placed the toy and the pussy-below clause completed the anatomy. Combined with the front-angle failures earlier: anal renders when the camera sees the orifice, and `seen from directly behind at bed level` is the reliable supine-alternative camera for it.

**Orgasm faces (tested, three states).** `eyes squeezed shut, brows drawn together, mouth wide open in a moan` rendered a full face-contorted orgasm expression. `eyes rolled back showing the whites, mouth open with her tongue out` rendered a clean ahegao. `post-orgasm afterglow: heavy-lidded dazed half-open eyes, flush from cheeks to chest, sweat beading on her brow, thighs still trembling` rendered the dazed aftermath. The expression clause needs an unobstructed face (a turned-over-shoulder face went soft-focus); keep the face clause adjacent to the camera clause, and note that strong face states coexist fine with hand placement clauses.

## Settings

Same as any Turbo work: 8 steps, CFG 1.0, `euler`/`simple` (`beta` also works), native resolution. `3:4` (1152x1536) and `2:3` (1088x1632) are the workhorse ratios for single subjects; wide acts and side profiles want `3:2` (1632x1088) or `16:9`. Squeezing a width-hungry act into a tall frame invites artifacts; match the ratio to the geometry of the act.

Findings marked tested come from Krea 2 NSFW finetunes; base-model and other finetune behavior may differ. In the failure table, KNP means the `Krea2PromptWeight` node from `comfyui-setup.md`.

## Failure table

| Symptom | Cause | Fix |
|---|---|---|
| Tasteful result despite explicit intent | euphemism or "tasteful/artistic" phrasing | plain nouns + what the camera sees |
| Genitals missing in an open pose | anatomy named vaguely ("between her legs") | name the vulva/labia/pussy and its state |
| Act shows bodies but nothing connects | contact point unstated | name what enters what, and how much is visible |
| Cloned faces with 2+ people | no per-person description | "The first is..., The second is..." |
| Floating or merged limbs | POV framing, unassigned limbs | geometric angle, `full bodies visible`, per-limb contact |
| Hair ties ride low or morph | tie height unpinned | name the tie height and anchor point |
| A small facial mark appears, vanishes, or moves | mark location unpinned | name the mark and its exact location |
| Deep insertion comes out shallow | depth adverb (`halfway`) | `full length buried inside, only the base visible` |
| Anal toy uninserted from the front | camera cannot see the orifice | `seen from directly behind at bed level`, or the prone geometry |
| Face state ignored | face turned away or soft-focus in frame | unobstructed face, expression clause next to the camera clause |
| Genitals dry despite an erotic scene | fluid clause missing from the prompt | add the fluid clause every time; unstated fluid renders absent |
| Rubber skin in explicit close-ups | no texture cues | pores, body hair, sweat sheen, flush |
| Correct anatomy but unerotic mood | no arousal state | erect nipples, flush, parted lips, wetness |
| Mosaic-style censor bars | phrasing drifted into stock-JAV look | keep plain Western phrasing, reroll seed |
| A feature droops despite a size LoRA | `heavy`/`sag` wording in the identity block | use a neutral size noun plus the desired shape; drop the droop adjective |
| Inner lips render despite "closed" intent | majora stated, minora state unstated | add `inner lips hidden`; a closed-labia (innie) LoRA at low strength adds fullness |
| Hands or legs land beside their target | limb placement over-constrained in multi-body scenes | fix one limb clause per iteration on a fixed seed; contact points hold, placement drifts |
| Register ignored, polished look persists | camera register buried at the prompt's end | move the register into the opening medium clause |
| Bust reads macromastia in side views | size LoRAs push hardest on profile cameras | lower stacked size-LoRA strength to about 0.4 for side views, or use a front/three-quarter camera |
| Garment color drifts (olive instead of black) | color word dropped from the wardrobe clause | name garment colors in every scene prompt |
| Stockings dissolve below the knee | long garment across a folded-pose boundary | continuity clause helps; knee-bent rear views stay fragile |
| SFW clothes render topless/nude | a nude-anatomy LoRA in a clothed register | a clothed-anatomy LoRA, positive coverage clauses, and no arousal clause |
| Glasses doubled (face and head) | glasses restated in scene clause after being pushed up | state glasses once, one location |
| Fingers land spreading instead of inside | `spread` clause paired with penetration clause | drop the `spread` clause, keep `inside` + knuckles visible |
| Nipple breaks through clothing | a nude-anatomy LoRA in a clothed register | a clothed-anatomy LoRA; nude-anatomy LoRAs leak nude bias through fabric |
| SFW lower half strips despite coverage wording | a closed-labia LoRA in the stack during a clothed register | drop the closed-labia LoRA for SFW; use the clothed-anatomy LoRA alone |
| Toy at the entrance instead of inside | "halfway" quantifier, shy deep insertion | state hidden vs visible shaft portions; expect tip-at-entrance bias |
| Vibrator misses the clitoris | supine front angle lacks clitoris localization | aim clause: `above her entrance, at the hood of her clitoris` |
| Anal toy resting under her instead of inside | front-on supine angle, anal clause solo | rear/side angle for the act, or enumerate `both entry points visible` |
| Strings fell downward, unattached | fluid-to-own-anatomy stringing | anchor strings to a solid object (toy, fingers holding it) |
| Hand belongs to the wrong person in two-body scenes | shared clause like "a hand" without a possessive | per-person possessives every time: `her hand`, `his hand` |
| Fine contact clause (fingers inside) outvoted under KNP | KNP amplifies register/fluids but drops micro-placement | state the contact twice (once in the act clause, once in a short KNP-style sentence) or drop KNP for that arm |
| Body-position modifier ignored | shares a sentence with a strong fluid clause | give the position its own sentence |
| Toy floats or lands wrong in a hidden-zone scene | toy geometry under clothing at 8-step turbo | drop the toy; acts with toys need the toy fully in frame (untested whether placement survives) |
| Fluid painted on knees or stocking tops instead of the pussy (condensed-milk look) | fluids render on surfaces, never through clothing | make the filth visible to the camera, or use the aftermath-only recipe |
| A cum LoRA changes nothing in aftermath-only scenes | no act in frame for it to render | skip the cum LoRA unless the act itself is in frame |
| Strong KNP weighting in a tight upskirt crop loses the character | weighting taxes identity and the crop cuts identifying features | re-pin the identity clauses visible in the crop |
| Majora flattened to prominent minora in KNP arms | KNP outvotes the puffy-majora clause even re-pinned | drop KNP for closed-labia targets; a closed-labia LoRA at low strength renders the puffy-closed look, at the cost of thinner fluid |
| Blouse drifts open in under-table camera shots | low camera looking up biases the neckline open | state `fully buttoned` explicitly for an innocent top under an upskirt camera |

## Translating crude briefs into Krea 2 prose

The model is detail-hungry and obeys exactly what is stated, so a crude tag-style brief converts cleanly: every tag becomes a visual clause in the architecture above, crude nouns survive the translation (`pussy`, `cock`, `cum`, and niche trained tokens like `grool` carry straight over; see the solo matrix for what `grool` renders), and modifiers attach to material language. Example brief: `woman, doggy style, mini-skirt and thigh high stockings, stuffs toy in her anus, pussy full of soaking grool, fat thick pussy` becomes:

```
A photorealistic amateur-style photograph of a naked adult woman on all fours on a bed, seen from
a 45-degree rear angle with her full body visible. A pleated mini-skirt is pushed up over her hips
and black thigh-high stockings frame her thighs. Her fat thick pussy is soaking wet, arousal
dripping down her inner thighs, and a glass toy is inserted in her ass. Her back is deeply arched,
her face turned toward the camera over her shoulder with a flushed, pleasured expression.
Harsh direct flash with deep shadows, natural skin texture with visible pores and a sheen of
sweat, film grain.
```

Then iterate one variable at a time.

## Reference-image note

If the user supplies a reference photo to match a look, follow the reverse-engineering flow in `krea2-core.md`: the reference carries identity and style, the prompt still carries the content, including the explicit register you want, or the look match will quietly sanitize the scene.
