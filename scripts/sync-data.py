"""Synchronize JSON content into offline JS and a teacher-readable Markdown bank."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
bank=json.loads((ROOT/'data/nahw-bank.json').read_text(encoding='utf-8'))
refs=json.loads((ROOT/'data/references.json').read_text(encoding='utf-8'))
for name,value,variable in [('nahw-bank',bank,'NAHW_BANK'),('references',refs,'NAHW_REFERENCES')]:
    (ROOT/f'data/{name}.js').write_text(f'window.{variable}='+json.dumps(value,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')

text=['# علم النحو — سوال، فہم، مشق','',
 'اصل موضوعاتی ترتیب: علم النحو، مولانا مشتاق احمد چرتھاولی، مکتبۃ البشریٰ، کراچی۔',
 'یہ نئی تدریسی تدوین ہے؛ اصل کتاب کا لفظی متن نہیں۔ یہاں MCQ کے جواب استاد کی مراجعت کے لیے کھلے ہیں۔','']
mapping=['# Content coverage map','',
 'The source contains 81 PDF pages. Its instructional sequence has 23 sections, from PDF pages 6–77. Front matter, blank notes pages, and publisher advertisements are excluded.',
 '', 'Every section has newly written short answers, paired MCQs with explanations, and at least one reference table. This is a condensed educational adaptation rather than a line-by-line transcription.',
 '', '| Section | Book topic | Printed pages | PDF pages | Short answers | MCQs | Reference tables |',
 '| --- | --- | --- | --- | --- | --- | --- |']
for c in bank['chapters']:
    text += [f'## {c["number"]}. {c["title"]}','',
       f'ماخذ: مطبوعہ صفحات {c["sourcePrintedPages"][0]}–{c["sourcePrintedPages"][1]}؛ PDF صفحات {c["sourcePdfPages"][0]}–{c["sourcePdfPages"][1]}۔','',
       '### مختصر سوال و جواب','']
    for i,q in enumerate(c['qa'],1):
        text += [f'**{i}. {q["question"]}**','',q['answer'],'']
    text += ['### MCQs اور تشریح','']
    for i,m in enumerate(c['mcqs'],1):
        text += [f'**{i}. {m["question"]}**','']
        for j,opt in enumerate(m['options']): text += [f'- {"ABCD"[j]}. {opt}']
        text += ['',f'**درست جواب: {"ABCD"[m["correctIndex"]]} — {m["options"][m["correctIndex"]]}**','',m['explanation'],'']
    text += ['### قاعدے ایک نظر میں','']
    for t in refs[str(c['number'])]:
        text += [f'#### {t["title"]}','', '| '+' | '.join(t['headers'])+' |', '| '+' | '.join(['---']*len(t['headers']))+' |']
        for row in t['rows']: text += ['| '+' | '.join(str(x).replace('|','/') for x in row)+' |']
        text += ['']
        if t['note']:text += [t['note'],'']
    pages=lambda key:f'{c[key][0]}–{c[key][1]}'
    mapping.append(f'| {c["number"]} | {c["title"]} | {pages("sourcePrintedPages")} | {pages("sourcePdfPages")} | {len(c["qa"])} | {len(c["mcqs"])} | {len(refs[str(c["number"])])} |')
mapping += ['',f'**Total:** {sum(len(c["qa"]) for c in bank["chapters"])} short answers, {sum(len(c["mcqs"]) for c in bank["chapters"])} MCQs, {sum(len(v) for v in refs.values())} reference tables.',
 '', 'Interpretive notes clarify the source’s traditional classifications where meanings and grammatical operation can differ by context. A specialist teaching review remains appropriate; this package does not claim independent expert certification.']
(ROOT/'learning-bank.md').write_text('\n'.join(text),encoding='utf-8')
(ROOT/'CONTENT_MAP.md').write_text('\n'.join(mapping)+'\n',encoding='utf-8')
print('Synchronized offline data, teacher reading export, and section map.')
