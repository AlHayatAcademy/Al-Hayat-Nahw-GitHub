# Al-Hayat · Ilm al-Nahw: Understanding & Practice

A buildless, Urdu-first Arabic grammar learning website prepared for GitHub Pages.

The revised presentation follows the user-owned reference course at https://bsarabic.insha.drimranhayat.com/: burgundy and gold branding, six rotating lesson colours, a full-width course homepage, white lesson sidebar, sticky segmented lesson tabs, and mobile bottom navigation. See `DESIGN_NOTES.md`.

- **23 sections**, in the uploaded book's topic sequence.
- **354 short questions and answers**.
- **354 four-option MCQs**, each with a correct answer and explanatory feedback.
- **31 reference tables**, including the 14 pronoun forms, noun declension, exceptions, and verb endings.
- Chapter practice, a random 30-question mixed practice, and retries of mistakes.
- Active recall cards, remembered and difficult markers, full-book search, and larger text.
- Browser-local progress with JSON export and restore. No accounts or server required.
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

Then open `http://localhost:8000`. Progress belongs to the browser and origin; progress on a local file URL will not automatically appear on the published Pages URL. Use export/restore to transfer it.

## Edit the content

The authoritative data files are:

- `data/nahw-bank.json`: sections, source page ranges, short answers, MCQs, answers, and explanations.
- `data/references.json`: reference tables.

Each short answer and MCQ has a stable ID. Preserve IDs when correcting existing items; use new IDs for new items. `correctIndex` is zero-based, from 0 to 3.

After editing JSON, regenerate the offline JavaScript copies and the reading export:

```sh
python scripts/sync-data.py
node verify.cjs
```

The generated `.js` copies let the site load without `fetch`, including from a local file URL. Keep the JSON and JavaScript copies in sync. `learning-bank.md` provides the entire question bank in a readable text format; its MCQ answers are visible for teacher review.

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

The interface is right-to-left. Arabic examples use bundled Amiri with `lang="ar"` spans. Urdu uses bundled Jameel Noori Nastaleeq with Nafees Nastaleeq as a local fallback. No font installation or remote font request is needed. The supplied font files are unmodified; font authors retain their rights.

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

JavaScript syntax and these data/interaction checks passed for the delivered version. **Visual browser QA was not available in this environment.** The DOM harness does not test actual browser rendering or layout. Inspect the published page on your phone and desktop, and obtain an Arabic-grammar teacher's review before treating the material as a final examination bank.

## Files

```text
index.html
reference-theme.css
styles.css
fonts/
core.js
app.js
data/nahw-bank.json
data/nahw-bank.js
data/references.json
data/references.js
scripts/sync-data.py
verify.cjs
learning-bank.md
CONTENT_MAP.md
DESIGN_NOTES.md
README.md
.nojekyll
```

No telemetry, analytics, external services, or uploaded student responses are used. Clearing browser storage removes local progress; export it first if you need a backup.
