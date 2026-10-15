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

The local font files are unmodified copies from the reference site’s font paths and the Jameel Noori CDN font used by its stylesheet. Their authors retain all font rights. The content is still an educational adaptation of Ilm al-Nahw, with the same source attribution as the preceding release.

Validation: data checks, all-chapter interaction checks, new home/catalogue navigation checks, asset checks and JavaScript syntax checks pass. Visual browser QA was unavailable, so rendering has not been independently screenshot-verified.
