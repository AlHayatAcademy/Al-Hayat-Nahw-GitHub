# Design revision — Ilm al-Nahw

Reference: https://bsarabic.insha.drimranhayat.com/ (the user’s Al-Insha al-Arabi course site).

The reference homepage, its version-3 stylesheet, and its first lesson page were retrieved directly. The existing site’s visible HTML structure and CSS definitions informed this revision. No reference-course lessons or question data were imported.

| Pattern from reference | Ilm Nahw implementation |
| --- | --- |
| Burgundy header and gold identity | Shared brand colours, round letter mark, gold header rule |
| Course homepage | Burgundy hero, course statistics, study and catalogue buttons |
| Six lesson accents | Burgundy, rose, indigo, amber, forest, plum in repeating book order |
| Colourful topic tiles | All 23 book sections with real Q&A, MCQ and table counts |
| Desktop lesson sidebar | White scrollable lesson list, current lesson marker, chapter search |
| Sticky lesson tabs | Short answers, explained MCQs, revision cards, rule tables |
| Question cards | White rounded cards, coloured rule border, numbered question badge |
| MCQ feedback | Green correct and red incorrect choices, followed by explanation |
| Phone navigation | Five-item bottom bar plus an accessible lesson drawer |
| Typography | Bundled Nastaliq Urdu and Amiri Arabic fonts |
| Footer | Al-Hayat branding and Dr. Imran Hayat attribution |

`reference-theme.css` preserves the reference design system. `styles.css` adapts it to the existing Nahw learning components. The data JSON files, question IDs, 354 Q&As, 354 MCQs, 31 reference tables, progress storage key and scoring engine are preserved.

The local font files are unmodified copies from the reference site’s font paths (Nafees Nastaleeq and Amiri). Their authors retain all font rights. The content is still an educational adaptation of Ilm al-Nahw, with the same source attribution as the preceding release.

Validation: data checks, all-chapter interaction checks, new home/catalogue navigation checks, asset checks and JavaScript syntax checks pass. Visual browser QA was unavailable, so rendering has not been independently screenshot-verified.

## Study-companion identity revision

The homepage and about panel now present the resource as **علم النحو: فہم و مشق**, prepared by Dr. Imran Hayat. The former lengthy publication disclaimer has been replaced by a positive description of the teaching contribution and a concise source acknowledgement. The book metadata, page mappings and question bank are retained.

## Reading and learning release

The mixed-script formatter now tokenizes complete Unicode words (including combining marks and join controls), applies the Arabic font only to complete marked Arabic tokens, and escapes all source text. Previously, a narrow character range could wrap the first letter of a following Urdu word; that formatter is removed. Search excerpts also stop at word boundaries.

Homepage changes retain the burgundy/gold identity with a split hero, a clearly analysed Arabic example, automatic progress/resume cards, a four-step study path and quieter, readable topic cards. All 23 sections have an original worked-example introduction with an Urdu translation, grammatical roles and a common-confusion note. Selected answers and distractors have been clarified; stable IDs and answer positions are retained.

The manual save button and manual transfer controls are removed. Local progress still saves automatically. Header measurement after font loading helps sticky tabs avoid the variable-height Urdu header. Cache-busted asset URLs ensure deployed browsers request the revised formatter.

Whole-word regression tests check 8,088 content strings. These checks establish safe markup and intact text boundaries, not a claim of pixel-level visual perfection; browser screenshot QA remains unavailable.

## Bilingual glossary

The new **الفاظ و اصطلاحات** tab contains 211 unique entries (129 grammar terms and 82 example words) mapped to all 23 lessons. Its locally rendered semantic SVG icons use six restrained colour families. Urdu and English meanings occupy separate language-tagged bands; examples expand on demand. Local filters distinguish terminology from ordinary example words. Chapter and whole-book search support all three languages, and chapter links such as `#ch05/vocabulary` can be shared or bookmarked.

The glossary is editorially selected for the lessons. Its chapter-link counts include repeated terms where pedagogically relevant, and should not be represented as additional unique vocabulary. New data and icon validation checks cover complete bilingual fields, example translations, valid mappings, semantic icon names, local filtering, search, and vocabulary routes.
