# Krea 2 Style Index

A 289-entry index of named style directions for the `Style:` block of a Krea 2 prompt, plus four full example paragraphs and the two formulas used to write the rest.

## What's in there

The index lists **289 entries** under **285 unique names**: `Comic Européen Prestige`, `Bande Dessinée (Hergé/Goscinny Tradition)` and `Beatrix Potter Style` each appear twice with identical text, and `Film Noir` appears twice with two *different* descriptions (pick whichever reads better for your shot).

Each full entry runs 60 to 150 words and is designed to be pasted whole into the `Style:` block. The four examples below are ready to paste; the index names the rest, and the two formulas let you write any missing entry yourself. The long-form paragraph matches the "long detailed prompts yield best results" behaviour the official docs describe.

## The two authoring formulas

The library uses two templates. Learn them and you can write your own.

**Formula A, "built on" (the majority):**

> A `<3 mood adjectives>` `<medium>` style built on `<linework / mark-making>`, `<shading / tonal treatment>`, `<proportion / form logic>`, `<atmosphere or emotional register>`, and `<a summarising "X intensity/charm/gravitas that feels Y">`. **Influenced by:** `<tradition>`, `<technique>`, `<studio or school practice>`, `<method>`.

**Formula B, "characterized by" (used for the artist-anchored entries):**

> `<medium>` aesthetics characterized by `<trait>`, `<trait>`, `<trait>`, `<trait>`, and `<trait>`, blending `<A>` with `<B>` through `<mechanism>`, `<mechanism>`, and `<mechanism>`, **reminiscent of** `<Artist 1>` and `<Artist 2>`, **inspired by** `<Work 1>` and `<Work 2>`.

Both end with attribution clauses. That trailing "Influenced by / reminiscent of / inspired by" list is the strongest signal in the paragraph: Qwen3-VL knows these names and works, and the clause anchors the abstract adjectives to something concrete.

## Four entries in full

**`Backlit Portraiture`** (a representative example):
> luminous photographic aesthetics defined by strong backlighting, radiant edge illumination, subtle translucency effects, atmospheric depth, graceful tonal transitions, and a heightened sense of visual separation, creating elegant and emotionally evocative imagery through carefully controlled exposure, naturalistic light diffusion, and refined portrait craftsmanship, reminiscent of Peter Lindbergh and Paolo Roversi, inspired by Vogue editorials and In the Mood for Love.

**`Cinematic Photography`:**
> A dramatically composed photographic style built on deliberate, film-like framing that favors wide aspect ratios and purposeful negative space, controlled color-grading logic that unifies highlight and shadow into a single cohesive mood, soft, motivated lighting sources that feel narratively justified rather than purely technical, a patient, unhurried compositional stillness charged with implied story beyond the frame, and a polished, narrative-driven visual gravitas rooted in feature-film visual-language tradition. Influenced by: Roger Deakins cinematography tradition, anamorphic-lens visual technique, narrative film-lighting practice, color-grading post-production method.

**`Ghibli Style`:**
> A gentle, hand-painted animation illustration style built on soft watercolor-inspired shading that gives every plane a breathable, tender texture, meticulous naturalistic detail applied with unhurried patience, rounded, expressive proportions carrying quiet emotional sincerity, a hushed, wondrous stillness pervading even the most fantastical scenes, and a nostalgic, wholesome hand-crafted intensity that feels timeless and deeply human. Influenced by: Hayao Miyazaki, Studio Ghibli production technique, traditional cel-animation painting method, naturalist watercolor illustration tradition.

**`Golden Hour Photography`:**
> A softly directional photographic style built on a low, raking angle of natural illumination that stretches long, gentle shadows across the frame, a diffused, glowing quality softened by increased atmospheric scattering at that time of day, a flattering, low-contrast luminosity that wraps gently around form rather than casting harsh definition, an unhurried, fleeting stillness carried through the brief window of ideal light, and a nostalgic, cinematic tenderness that feels naturally soft and effortlessly atmospheric. Influenced by: natural available-light photography tradition, magic-hour cinematography technique, outdoor portrait-lighting practice, documentary golden-hour shooting method.

## Full index

Nine implicit families. The first entry of each family is a **generic base style** (`Photography`, `Painting`, `Drawing`, `3D Render` etc.), usable on its own when you want the medium without a specific voice.

<details>
<summary><b>Anime &amp; Manga (1-42)</b></summary>

Anime Style · Ghibli Style · 70s Anime · Manga Style · Akira Style · Akira Toriyama Style · Atsushi Ohkubo Style · Attack on Titan Style · Chainsaw Man Style · Jujutsu Kaisen Style · My Hero Academia Style · Berserk Manga Style · Bleach Style · Frieren Style · Boichi Style · Cinematic Anime · Classic Shojo Illustration · Euromanga Style · Watercolor Anime Illustration · Granblue Fantasy Pin-Up Style · Katsuya Terada Style · Manhwa Ultradetailed Art · Murata Hyperrealism · MidJourney Niji-Inspired Digital Illustration · Shindol Style · Solo Leveling Art · Pony 2.5D Realism · Pony/Illustrious Checkpoint Style · Yoshitaka Amano Style · Yoshitaka Amano Fine Art · Death Note Style · JoJo's Bizarre Adventure Style · One Piece Style · Sailor Moon Style · Chibi Anime · Anime Key Visual · Junji Ito Style · Anime Illustration · Ultradetailed Manga Illustration · Polished Ultrarealistic Anime Pin-Up · Thin Delicate Outline Romantic Anime-Photographic Hybrid · Cel Shading
</details>

<details>
<summary><b>Cartoon &amp; Western Animation (43-60)</b></summary>

Cartoon Style · Invader Zim Style · Nickelodeon Animation Style · Rick and Morty Style · Simpsons Style · South Park Style · Steven Universe Style · Adventure Time Style · Hanna-Barbera Style · Family Guy Style · Modern Cartoon · Rubber Hose Cartoon · Disney Ultradetailed Illustration · Classic Disney Feature Animation · Cyberpunk · Bruce Timm Noir · Arcane Animation Still · Toon Shader
</details>

<details>
<summary><b>Comics &amp; Graphic Novel (61-93)</b></summary>

Comics Style · Alex Ross Style · Alternative Comics Style · Amanda Conner Illustration · American Comic Realism · Comic Européen Prestige · American Pulp Illustration · Frank Miller Style · Bengal Illustration · Comic Européen Prestige *(dup)* · Crosshatched Graphic Novel · Graphic Novel · Franco-Belgian Ultradetailed Comics · Bande Dessinée (Hergé/Goscinny Tradition) · Frank Cho Style · Enki Bilal-Inspired Comic and Digital Painting · Hellboy Style · Archie Comics Style · Bande Dessinée (Hergé/Goscinny Tradition) *(dup)* · Mark Brooks / Manapul Style · Marvel Comics Style · Marvel Cover Art · Milo Manara Style · Psychological Thriller Pulp Digital Painting · DC Comics Style · Zenescope Illustration · Ryan Benjamin Style · Travis Charest Style · Adi Granov Style · Bold Contour Style · Clean Line Art · Moebius-Inspired Illustration · Vintage Comics
</details>

<details>
<summary><b>Drawing, Sketch &amp; Ink (94-122)</b></summary>

Drawing · Caricature · Charcoal Rendering · Hyperrealistic Colored-Pen Sketch · Jarek Kubicki Style · Playful Hand-Drawn Illustration · Chinese Ink Drawing · Sketch · Beatrix Potter Style · Children's Book Drawing · Vintage Children's Book Drawing · Gris Grimly Style · Tim Burton Style · Fashion Sketch · Loose Crosshatched Character Sketch · Wojak/Meme-Sketch Style · Ink Pen Drawing · Etching · Technical Drawing · Conté Pastel · Crayola Colored-Book Style · Bookplate Illustration · Boulet Graphic Illustration · Collector Storybook Illustration · Saul Steinbeck Art · Whimsical Illustration · Doodle · Very Simplistic Doodle · Beatrix Potter Style *(dup)*
</details>

<details>
<summary><b>Photography (123-176)</b></summary>

Photography · 35mm Photography · Adobe Lightroom Masterpiece · Analog Photography · Annie Leibovitz Portraiture · Atmospheric Matte Painting · Backlit Portraiture · Black And White Documentary · Bleach Bypass Photography · Blue Hour Cinema · Butterfly Lighting · Candid Photography · Cinematic Photography · Commercial Beauty Photography · Editorial Photography · Cross Process Photography · Cross-Processed Film Photography · Cyberpunk Photography · Fish-Eye Photography · Surveillance Camera Photo · Direct-Flash Photography · Dutch Angle Photography · Full Body Photo · GQ Photoshoot · HDR Photography · High-Key Lighting Photography · Hitchcockian Photo · Film Noir · Film Noir *(2nd variant)* · Instagram Model Glamour Photography · Art Photography · Kodachrome · National Geographic Photography · Motion Blur Photography · Natural Lighting Photography · Neon Photography · Low-Key Photography · Night Photography · Peter Lindbergh-inspired photography style · Photoshoot · Playboy / Maxim-Style Photoshoot · Hyper Synthwave · Selfie Photo · Sin City Photography · Soft Beauty-Dish Portrait Rendering · Streamer Glam Selfie Realism · Supermodel Photoshoot · LinkedIn Pro Portrait · Sitcom Still · Rembrandt-Inspired Photography · Stranger Things-Inspired Art · Vogue Magazine · Golden Hour Photography · Cinematic Tron
</details>

<details>
<summary><b>Graphic Design, Flat &amp; Vector (177-195)</b></summary>

Design · Butcher Billy Style · Corporate Memphis · 8-Bit Style · Kintsugi-Inspired Digital Art · Soviet Propaganda Poster · Minecraft Style · Funko Pop Style · Hyper-Stylized Illustration · Graphic Flat-Vector Travel Poster Illustration · Ornamental Patterns Hyperrealism Portrait · Flat Illustration · Vector Art · Bauhaus · Poster Art · Minimalist Line Art · Minimalism · Gradients · Origami
</details>

<details>
<summary><b>3D, Craft &amp; Physical Media (196-218)</b></summary>

3D Render · Pixar Animation · Cinematic Final Fantasy 3D Render · Marble Sculpture · Playful Retro Pop · Low Poly · LEGO Minifigure · Paper Cutout · Collage · Claymation · Mixed Media · Wallace and Gromit Style · Muppets Style · Zelda Wind Waker Style · PS1 Graphics · Woodcut · Contemporary Lithography · Variable-Size Ben-Day Dots Illustration · Contemporary Ukiyo-E · Mosaic Art · Stained Glass Flat Art · Isometric 3D Graphic · Quilling
</details>

<details>
<summary><b>Digital Painting &amp; Concept Art (219-252)</b></summary>

Digital Painting · Castlevania Concept Art · Sakimichan Style · Scribble Fine Art · Gris Grimly-Inspired Hyperrealism · Absolute Painterly Style · Artgerm Style · ArtStation Masterpiece · Bastien Lecouffe-Deharme Fantasy · Bernie Wrightson Gothic · Blacklight Style · X-Ray Style · Brassaï Night Photography · Character Design Illustration · Charlie Bowater Style · Contemporary Fantasy Art · Cosmic Horror Illustration · Contemporary Commercial Illustration · Editorial Illustration · Cover Art · Interplay of Shadow and Light · Kekai Kotaki Style · Robin Eley Style · Dark Fantasy Illustration · GTA V Polished Cover Art · Expressive Character Illustration · Splatterpunk Horror Illustration · James Jean Style · Victo Ngai Style · Kay Nielsen Style · Hyper-Stylized Digital Painting · Movie Digital Art · RossDraws Style · Loish Ultrarealism
</details>

<details>
<summary><b>Painting &amp; Fine Art (253-289)</b></summary>

Painting · Abstract Expressionism · Academic Precision Realism · Acrylic Dreamscape · Adventure Illustration · Agnes Cecile Style · Airbrush Fantasy · Van Gogh Style · Monet Style · Wet-on-Wet Watercolor Ink Painting · Alphonse Mucha Masterwork · Anato Finnstark Style · Rembrandt Painting · Art Deco Gold Highlights · Ashley Wood Illustration · Tenebrism · Chiaroscuro · Bill Sienkiewicz Expressionism · Graffiti Painting · Boris Vallejo Style · Brushwork Emphasis · Pin-Up · 2020s Pin-Up · Hyperrealism · Ultrarealism · Casey Baugh Style · Commercial Illustration · Giallo Poster Art · Grindhouse Poster Illustration · Cubism · Carne Griffiths Style · Jackson Pollock Style · Watercolor Painting · Contemporary Oil Painting · Pop Art · Thick Brushstrokes Painting · Impasto
</details>

## Using styles well

- **One per prompt.** Two style paragraphs = ~200 words of competing surface description.
- **Match the style family to the subject.** A pose block written in anatomical prose plus `8-Bit Style` will fight itself; the pose detail has nowhere to go at that resolution.
- **Weight only the style's opening phrase, with `Krea2PromptWeight` installed.** `(luminous photographic aesthetics:2)` works on the first few words. Weighting a full 120-word block does nothing.
- **Trim before you add.** If an entry mentions an element you don't want (e.g. `Backlit Portraiture`'s "subtle translucency effects"), delete that clause rather than negating it.
- **Artist names are the strongest signal.** The "reminiscent of / inspired by" clause is often the strongest signal in the paragraph. If a style isn't landing, that clause is the first thing to strengthen.

## Source

The index and the four sample paragraphs were assembled from public Krea 2 workflow notes. The pose system in `poses.md` is credited to [@Zuanfilm](https://x.com/Zuanfilm).
