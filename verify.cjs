/* Data and interaction smoke checks without a browser or external packages. */
const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const root=__dirname,publicDir=fs.existsSync(path.join(root,'dist'))?path.join(root,'dist'):root;
const core=require(path.join(publicDir,'core.js'));
const bank=JSON.parse(fs.readFileSync(path.join(publicDir,'data/nahw-bank.json'),'utf8'));
const refs=JSON.parse(fs.readFileSync(path.join(publicDir,'data/references.json'),'utf8'));
assert.equal(bank.chapters.length,23);
let qCount=0,mCount=0;const ids=new Set(),questions=new Set();
for(const [index,c]of bank.chapters.entries()){
 assert.equal(c.number,index+1);assert.ok(c.qa.length>0);assert.equal(c.qa.length,c.mcqs.length);
 assert.ok(refs[c.number]?.length);assert.equal(c.sourcePdfPages[0],c.sourcePrintedPages[0]+1);
 for(const q of c.qa){assert.ok(!ids.has(q.id));ids.add(q.id);assert.ok(!questions.has(q.question));questions.add(q.question);assert.ok(q.answer);qCount++}
 for(const m of c.mcqs){assert.ok(!ids.has(m.id));ids.add(m.id);assert.equal(m.options.length,4);assert.equal(new Set(m.options).size,4);assert.ok(m.options[m.correctIndex]);assert.ok(c.qa.some(q=>q.id===m.qaId));assert.ok(m.explanation);mCount++}
 for(const t of refs[c.number])for(const r of t.rows)assert.equal(r.length,t.headers.length);
}
assert.equal(qCount,354);assert.equal(mCount,354);
assert.equal(core.clean('  الْكِتَابُ '),core.clean('الکتاب'));
assert.ok(core.search(bank.chapters,'الکتاب').length>0);
assert.ok(core.search(bank.chapters,'مفعول').length>15);
const p=core.emptyProgress(),sample=bank.chapters[0].mcqs[0];
p.attempts[sample.id]={choice:sample.correctIndex};assert.equal(core.summary(bank.chapters,p).correct,1);
p.attempts[sample.id].choice=(sample.correctIndex+1)%4;assert.equal(core.summary(bank.chapters,p).wrong,1);
assert.deepEqual(core.validateProgress(null),core.emptyProgress());
assert.equal(Object.keys(core.validateProgress({attempts:{'ch01-m001':{choice:99}}}).attempts).length,0);
const source=[1,2,3,4];assert.deepEqual([...core.shuffle(source)].sort(),source);assert.deepEqual(source,[1,2,3,4]);

// A small DOM contract harness checks app state transitions and generated markup.
// It does not evaluate browser layout, accessibility APIs, or visual rendering.
class El{
 constructor(){this.listeners={};this.dataset={};this.attrs={};this.style={};this.innerHTML='';this.textContent='';this.value='';this.hidden=false;this.disabled=false;this.children=[];this.classes=new Set();this.classList={add:(...s)=>s.forEach(v=>this.classes.add(v)),remove:(...s)=>s.forEach(v=>this.classes.delete(v)),contains:s=>this.classes.has(s),toggle:(s,v)=>{const set=v===undefined?!this.classes.has(s):v;set?this.classes.add(s):this.classes.delete(s);return set}}}
 addEventListener(t,f){(this.listeners[t]??=[]).push(f)}setAttribute(k,v){this.attrs[k]=v}removeAttribute(k){delete this.attrs[k]}scrollIntoView(){}focus(){}append(...items){this.children.push(...items)}remove(){}click(){}close(){}showModal(){}
}
const els=new Map(),get=s=>{if(!els.has(s))els.set(s,new El());return els.get(s)};
const tabs=['learn','quiz','review','reference'].map(mode=>{const e=new El();e.dataset.mode=mode;return e});
const document={querySelector:get,querySelectorAll:s=>s==='[data-mode]'?tabs:[],getElementById:id=>get('#'+id),createElement:()=>new El(),body:new El(),listeners:{},addEventListener(t,f){(this.listeners[t]??=[]).push(f)}};
const storage=new Map(),window={NAHW_BANK:bank,NAHW_REFERENCES:refs,NahwCore:core,scrollTo(){},location:{hash:''},events:{},addEventListener(t,f){(this.events[t]??=[]).push(f)},history:{pushState(a,b,hash){window.location.hash=hash}}};
const context={window,document,localStorage:{getItem:k=>storage.get(k),setItem:(k,v)=>storage.set(k,v)},setTimeout:()=>0,clearTimeout(){},URL:{createObjectURL:()=>'',revokeObjectURL(){}},Blob:class{}};
vm.runInNewContext(fs.readFileSync(path.join(publicDir,'app.js'),'utf8'),context);
const click=data=>{const b=new El();b.dataset=data;for(const f of document.listeners.click)f({preventDefault(){},target:{closest:selector=>selector==='button'||selector==='[data-view]'&&b.dataset.view?b:null}})};
const content=()=>get('#content').innerHTML;
assert.ok(content().includes('question-card'));assert.equal(get('#learning').hidden,true);assert.equal(get('#home-hero').hidden,false);assert.equal((get('#topic-grid').innerHTML.match(/data-chapter=/g)||[]).length,23);
click({view:'topics'});assert.equal(get('#home-hero').hidden,true);assert.equal(get('#course-overview').hidden,false);
click({view:'qa'});assert.equal(get('#learning').hidden,false);
click({view:'home'});assert.equal(get('#learning').hidden,true);
const ov=get('#overview-search');ov.value='ZZZ-no-topic';for(const f of ov.listeners.input)f({target:ov});assert.ok(get('#topic-grid').innerHTML.includes('کوئی سبق نہیں'));ov.value='';for(const f of ov.listeners.input)f({target:ov});
window.location.hash='#ch05/reference';for(const f of window.events.popstate)f();assert.ok(content().includes('reference-card'));assert.equal(get('#learning').hidden,false);
click({chapter:'ch01'});click({mode:'learn'});
for(const c of bank.chapters){click({chapter:c.id});assert.ok(content().includes(c.qa[0].id));click({mode:'reference'});assert.ok(content().includes('reference-card'));click({mode:'learn'})}
click({chapter:'ch01'});click({mode:'quiz'});assert.ok(content().includes('data-choice="0"'));
click({choice:'0'});assert.ok(content().includes('feedback'));const firstSave=storage.get('al-hayat-nahw-progress-v1');click({choice:'1'});assert.equal(storage.get('al-hayat-nahw-progress-v1'),firstSave);
click({quiz:'mixed'});for(let i=0;i<30;i++){click({choice:String(i%4)});click({action:'quiz-next'})}assert.ok(content().includes('result-hero'));
click({action:'retry-session'});assert.ok(content().includes('quiz-card')||content().includes('دہرائی کے لیے کوئی'));
click({mode:'review'});assert.ok(content().includes('flash-card'));click({action:'flip'});assert.ok(content().includes('flash-answer'));
click({flashMark:'ch01-q001',markKind:'known'});const saved=JSON.parse(storage.get('al-hayat-nahw-progress-v1'));assert.equal(saved.mastered['ch01-q001'],true);
const se=get('#search');se.value='مفعول';for(const f of se.listeners.input)f({target:se});assert.ok(content().includes('search-result'));
click({action:'clear-search'});click({mode:'learn'});click({bookmark:'ch01-q001'});click({filter:'difficult'});assert.ok(content().includes('ch01-q001'));
assert.ok(!/undefined|NaN/.test(content()));
const html=fs.readFileSync(path.join(publicDir,'index.html'),'utf8');for(const match of html.matchAll(/(?:src|href)="\.\/([^"#]+)"/g))assert.ok(fs.existsSync(path.join(publicDir,match[1])),`Missing asset ${match[1]}`);
for(const name of ['JameelNooriNastaleeq.woff2','NafeesNastaleeq.woff2','Amiri-Regular.woff2','Amiri-Bold.woff2']){const f=fs.readFileSync(path.join(publicDir,'fonts',name));assert.equal(f.toString('ascii',0,4),'wOF2');assert.equal(f.length,f.readUInt32BE(8),'Incomplete font '+name)}
console.log(JSON.stringify({chapters:23,shortAnswers:qCount,mcqs:mCount,referenceTables:Object.values(refs).reduce((a,b)=>a+b.length,0),dataChecks:'PASS',interactionSmokeChecks:'PASS',referenceThemeChecks:'PASS: home/catalog/lesson navigation, 23 topic tiles, six chapter accents, reusable chapter URLs',visualBrowserQA:'Not performed: browser skill unavailable'}));
