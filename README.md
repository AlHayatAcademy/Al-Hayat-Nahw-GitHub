# Al-Hayat · Ilm al-Nahw: Understanding & Practice

A buildless, Urdu-first Arabic grammar learning website prepared for GitHub Pages.

The revised presentation follows the user-owned reference course at https://bsarabic.insha.drimranhayat.com/: burgundy and gold branding, six rotating lesson colours, a full-width course homepage, white lesson sidebar, sticky segmented lesson tabs, and mobile bottom navigation. See `DESIGN_NOTES.md`.

- **23 sections**, in the uploaded book's topic sequence.
- **354 short questions and answers**.
- **354 four-option MCQs**, each with a correct answer and explanatory feedback.
- **211 unique bilingual entries**: 129 grammar terms and 82 example-vocabulary items, linked to all 23 lessons.
- **31 reference tables**, including the 14 pronoun forms, noun declension, exceptions, and verb endings.
- Chapter practice, a random 30-question mixed practice, and retries of mistakes.
- Active recall cards, remembered and difficult markers, full-book search, and larger text.
- Progress saves automatically in this browser. No manual save button, accounts or server required.
- Relative asset paths: compatible with a GitHub project Pages URL.
- Works by opening `index.html` directly as well as through a web server. No CDN dependency.

## Publish on GitHub Pages

1. Create a GitHub repository.
2. Extract the ZIP and upload its **contents** so that `index.html` is at the repository root.
3. Open **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Choose **main** and **/ (root)**, then save.
6. Wait for GitHub's Pages deployment and open the URL shown there.

No npm install, framework build, API key, paid hosting, or database is needed.

## Open locally

Double-click `index.html`. For a local HTTP server, run:

```sh
python -m http.server 8000
```

Then open `http://localhost:8000`. Progress belongs to the browser and origin; progress on a local file URL will not automatically appear on the published Pages URL. Progress does not transfer automatically between devices or origins.

## Edit the content

The authoritative data files are:

- `data/nahw-bank.json`: sections, source page ranges, short answers, MCQs, answers, and explanations.
- `data/references.json`: reference tables.

Each short answer and MCQ has a stable ID. Preserve IDs when correcting existing items; use new IDs for new items. `correctIndex` is zero-based, from 0 to 3.

After editing JSON, regenerate the offline JavaScript copies and the reading export:

```sh
python scripts/sync-data.py
node verify.cjs
node verify-typography.cjs
```

The generated `.js` copies let the site load without `fetch`, including from a local file URL. Keep the JSON and JavaScript copies in sync. `learning-bank.md` provides the entire question bank in a readable text format; its MCQ answers are visible for teacher review.

## Bilingual vocabulary tab

**الفاظ و اصطلاحات** is the fifth lesson mode. Each entry has an Arabic heading, a local semantic SVG icon, an Urdu meaning, an English meaning, a brief Urdu clarification, and an expandable Arabic example with Urdu translation. The green Urdu band and blue English band keep the two scripts visually distinct.

Use **نحوی اصطلاحات** for technical grammar terms or **مثالوں کے الفاظ** for ordinary words from the worked examples. Search accepts Arabic, Urdu, and English. The main book search also includes the glossary, and each result opens the relevant lesson card. The same entry may be relevant to several lessons: 211 is the unique-entry count, rather than the sum of chapter links. This is a selected learning glossary, not a claim to list every word in the source book.

`data/vocabulary.json` is the editable glossary; `icons.js` contains the dependency-free SVG icon set. `scripts/build-vocabulary.py` holds the initial authored definitions and lesson mappings. Run it only when changing that source; after normal JSON edits use `scripts/sync-data.py`.

## Latest reading and learning improvements

- Fixed the whole-word formatter: Arabic font spans never split Urdu words.
- Removed letter-based partial matches and mid-word search excerpts.
- Matched mixed Urdu/Arabic text sizing and allowed normal whole-word wrapping.
- Removed clipped topic descriptions; cards now use concise, authored lesson summaries.
- Added 23 translated worked examples with word roles and common-confusion notes.
- Refined selected rules and distractors without changing question IDs or correct-answer positions.
- Added a personal resume card, real progress summary and four-step learning path.
- Replaced saturated lesson tiles with white cards and restrained colour accents.
- Measured the header after font loading to keep sticky tabs clear at different zoom levels.
- Removed the manual save control; progress remains automatic.
- Versioned CSS/JS URLs to prevent an old cached formatter from surviving deployment.

## Learning flow

1. Read a question and recall an answer before opening it.
2. Compare the explanation and Arabic example.
3. Mark remembered items or flag difficult ones.
4. Solve the paired MCQ or chapter practice.
5. Read feedback after each attempt, including correct attempts.
6. Retry mistakes and use the comparison tables for revision.

The displayed MCQ accuracy is based on the **latest recorded answer for each attempted question**, rather than all historical clicks. A practice-session score counts only that session. Remembered short answers are self-assessed separately.

## Teaching contribution and source

The public identity is **علم النحو: فہم و مشق**, an interactive study companion prepared by Dr. Imran Hayat. The homepage, sidebar and about panel foreground the educational compilation, question design, explanatory approach and interactive presentation. The about panel retains a brief acknowledgement of the book used for the sequence and core topics. This credit describes the pedagogical contribution; it does not claim authorship of the source book or permission from its publisher.

## Source and editorial approach

Source: **علم النحو**, Maulana Mushtaq Ahmad Charthawali, Maktabat al-Bushra, Karachi, as supplied in `ILM UN NAHW.pdf` (81 PDF pages).

The 23 instructional sections span printed pages 5–76, corresponding to PDF pages 6–77. Their topic sequence is preserved. The source PDF itself is not bundled. Front matter, blank notes pages, and publisher advertisements are excluded from the learning bank.

This is an original instructional adaptation, not a verbatim transcription. Explanations, questions, and many examples have been rewritten. Standard grammar terms and paradigms are retained where precision requires them. Longer source passages and tables are condensed into questions and comparison aids. This is not a certified sentence-by-sentence extraction.

Context-dependent and traditional classifications are identified where needed. In particular, not every occurrence of `أن`, `ما`, `لا`, `حتى`, or `واو` has the same operation. The source's grouping of masdari particles in the final chapter is accompanied by a clarification that `أن` and `أنّ` can still be grammatical operators. Other teaching notes distinguish grammatical case, building, and case position.

Changing wording alone does not establish permission to reproduce a protected work. Attribution is retained; no license to the source book is asserted. Review the educational adaptation and any applicable publication rights before public distribution. No broad open-source license is applied to the source book.

## Typography and access

The interface is right-to-left. Arabic examples use bundled Amiri with `lang="ar"` spans. Urdu uses bundled Nafees Nastaleeq (148 KB). No font installation or remote font request is needed. The compact Urdu font is preloaded; `font-display: swap` keeps text readable while it loads. The supplied font files are unmodified; font authors retain their rights.

The home page shows all 23 lesson tiles in the original order. The navigation opens the lesson catalogue, short answers, MCQs, and recall cards. Lesson pages use a sticky desktop sidebar and a mobile drawer; primary navigation becomes a fixed bottom bar on phones. Chapter URLs such as `#ch05/reference` can be bookmarked.

The layout includes mobile navigation, responsive cards, horizontally scrollable tables, keyboard tabs, visible focus styles, reduced-motion support, a skip link, and answer feedback with text indicators. Automated checks do not establish full accessibility conformance.

## Verification

`node verify.cjs` checks:

- All 23 chapters and their source-page mappings.
- Unique IDs and short-answer questions.
- Four unique options per MCQ, valid answer positions, explanations, and valid Q&A links.
- Reference-table column consistency and all required asset paths.
- Arabic/Urdu-normalized search and scoring functions.
- Home/catalogue/lesson navigation, the 23 topic tiles, topic filtering, and reusable chapter URLs.
- App state transitions using a minimal DOM harness: all chapters, reference views, locked answers, mixed-session scoring, mistake retry, revision cards, progress updates, and search.

`node verify-typography.cjs` additionally checks 8,088 content strings for preserved text and intact word boundaries, including the sentence from the reported screenshot.

JavaScript syntax and these data/interaction checks passed for the delivered version. **Visual browser QA was not available in this environment.** The DOM harness does not test actual browser rendering or layout. Inspect the published page on your phone and desktop, and obtain an Arabic-grammar teacher's review before treating the material as a final examination bank.

## Files

```text
index.html
reference-theme.css
styles.css
fonts/
core.js
icons.js
app.js
data/nahw-bank.json
data/nahw-bank.js
data/references.json
data/references.js
data/lesson-guides.json
data/lesson-guides.js
data/vocabulary.json
data/vocabulary.js
scripts/build-vocabulary.py
scripts/build-guides.py
scripts/sync-data.py
verify.cjs
verify-typography.cjs
learning-bank.md
CONTENT_MAP.md
DESIGN_NOTES.md
README.md
.nojekyll
```

No telemetry, analytics, external services, or uploaded student responses are used. Clearing browser storage removes local progress.


### Faster loading release

The 9.8 MB Jameel font download has been replaced with the bundled 148 KB Nafees Nastaleeq font. Amiri remains in use for Arabic examples. All fonts use `font-display: swap`; no remote fonts or icon services are required. All scripts defer execution until HTML parsing finishes and retain their dependency order.

The homepage no longer builds hidden lesson panels. Lesson navigation and search no longer regenerate the hidden homepage, and repeated searches reuse normalized indexes. Initial deep links render once. All lesson data, progress storage keys and existing chapter URLs are retained.

Replace the repository files with this release, including the updated HTML/CSS/scripts. Remove the old unused `fonts/JameelNooriNastaleeq.woff2` if it remains in your repository. Asset URLs have a new version so returning visitors receive the fixes. This is a source ZIP; upload it to GitHub Pages to update the live site.


### Stable header fix

Removed the ResizeObserver/font-ready/resize measurement feedback loop. It measured the outer header including its 2px decorative rule, then wrote that measurement into the inner header minimum height. Each observation therefore grew the header again. CSS now owns the complete header height (80px desktop, 78px mobile), with the inner row reserving 2px for the decorative rule. Sticky tabs and sidebar offsets continue to share the same CSS variable. No header height is written by JavaScript.
