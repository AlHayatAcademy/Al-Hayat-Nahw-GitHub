/* Regression for the reported split-word/font-span bug. No browser needed. */
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const root=__dirname,C=require('./core.js');
const b=JSON.parse(fs.readFileSync(path.join(root,'data/nahw-bank.json'),'utf8'));
const refs=JSON.parse(fs.readFileSync(path.join(root,'data/references.json'),'utf8'));
const guides=JSON.parse(fs.readFileSync(path.join(root,'data/lesson-guides.json'),'utf8'));
const strings=[];
function visit(value){if(typeof value==='string')strings.push(value);else if(Array.isArray(value))value.forEach(visit);else if(value&&typeof value==='object')Object.values(value).forEach(visit)}
visit(b);visit(refs);visit(guides);visit(JSON.parse(fs.readFileSync(path.join(root,'data/vocabulary.json'),'utf8')));
const wordChar='[\\p{L}\\p{M}\\u200c\\u200d]';
const brokenEnd=new RegExp(wordChar+'<\\/span>'+wordChar,'u');
const brokenStart=new RegExp(wordChar+'<span[^>]*>'+wordChar,'u');
for(const s of strings){
 const output=C.richText(s);
 assert.equal(output.replace(/<\/?span\b[^>]*>/g,''),C.escapeHTML(s),'Text was lost or changed');
 assert.ok(!brokenEnd.test(output),'Font span splits a word at its end: '+s);
 assert.ok(!brokenStart.test(output),'Font span splits a word at its start: '+s);
}
const examples=[
 ['وَصَلَ الضَّيْفُ میں مسند الیہ کون ہے؟','میں'],
 ['يَكْتُبُ کے بعد اردو لفظ ہے۔','کے'],
 ['أَنْ لکھیں، پھر لفظ سمجھیں۔','لکھیں'],
 ['كِتَابٌ کی مثال دیکھیں۔','کی'],
 ['قَرَأَ مُعَلِّمٌ نے نہیں کہا۔','نے'],
 ['تعلیمِ نحو میں پیش رفت','تعلیمِ'],
 ['عِلْمٌ بے‌ضرر لفظ کے ساتھ','بے‌ضرر']
];
for(const [text,intact]of examples){const output=C.richText(text);assert.ok(output.includes(intact));assert.ok(!brokenStart.test(output)&&!brokenEnd.test(output))}
assert.equal(C.richText('وَصَلَ الضَّيْفُ میں مسند الیہ کون ہے؟'),'<span class="arabic" lang="ar">وَصَلَ الضَّيْفُ</span> میں مسند الیہ کون ہے؟');
assert.equal(C.richText('<script>alert(1)</script> وَصَلَ میں').includes('<script>'),false);
assert.equal(Object.keys(guides).length,23);
for(const c of b.chapters){const g=guides[c.number];assert.ok(g.goal&&g.summary&&g.translation&&g.example&&g.remember);assert.ok(g.analysis.length>=2)}
const old=JSON.parse(fs.readFileSync(path.join(root,'data/nahw-bank.json'),'utf8'));
assert.equal(old.chapters.reduce((n,c)=>n+c.qa.length,0),354);
const css=fs.readFileSync(path.join(root,'styles.css'),'utf8');
assert.ok(css.includes('word-break:normal'));
assert.ok(css.includes('hyphens:none'));
assert.ok(css.includes('.arabic{display:inline;'));
assert.ok(css.includes('-webkit-line-clamp:unset'));
const html=fs.readFileSync(path.join(root,'index.html'),'utf8');
assert.ok(html.includes('lesson-guides.js?v='));
assert.ok(!html.includes('progress-export'));
console.log(JSON.stringify({textStringsChecked:strings.length,wholeWordFontBoundaries:'PASS',reportedScreenshotSentence:'PASS',escaping:'PASS',lessonGuides:23,visualRendering:'Not browser-verified'}));
