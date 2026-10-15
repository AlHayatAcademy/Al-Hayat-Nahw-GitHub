"""Build an authored bilingual glossary linked to the 23 grammar lessons."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
entries=[]
def add(kind,source):
 for line in source.strip().splitlines():
  fields=line.strip().split('|')
  assert len(fields)==8,(len(fields),line)
  key,arabic,ur,en,note,example,translation,icon=fields
  entries.append(dict(id=key,kind=kind,arabic=arabic,meaningUr=ur,meaningEn=en,explanationUr=note,example=dict(arabic=example,urdu=translation),icon=icon))
add('term','''
nahw|النَّحْوُ|عربی جملے کی ساخت و اعراب کا علم|Arabic syntax and grammatical inflection|یہ علم بتاتا ہے کہ لفظ جملے میں کیا کام کرتا ہے اور اس کا آخری اعراب کیا ہوگا۔|الْعِلْمُ نُورٌ.|علم روشنی ہے۔|book
word|الْكَلِمَةُ|بامعنی مفرد لفظ|Word|اسم، فعل اور حرف کلمے کی بنیادی نحوی قسمیں ہیں۔|قَلَمٌ، كَتَبَ، فِي.|قلم، اس نے لکھا، میں۔|letters
noun|الِاسْمُ|اسم؛ زمانے کے بغیر معنی بتانے والا کلمہ|Noun|نام، چیز، صفت یا معنی کا لفظ جو اپنی وضع میں فعل کی طرح زمانہ شامل نہ کرے۔|هٰذَا قَلَمٌ.|یہ قلم ہے۔|tag
verb|الْفِعْلُ|کام یا حالت اور زمانہ بتانے والا کلمہ|Verb|ماضی، مضارع اور امر کی صورتوں میں فعل پہچانا جاتا ہے۔|كَتَبَ الطَّالِبُ.|طالب علم نے لکھا۔|bolt
particle|الْحَرْفُ|دوسرے لفظ سے معنوی تعلق قائم کرنے والا کلمہ|Particle|یہاں حرف سے نحوی کلمہ مراد ہے، حروفِ تہجی کا الگ مفہوم نہیں۔|الْكِتَابُ فِي الْحَقِيبَةِ.|کتاب بستے میں ہے۔|link
sentence|الْجُمْلَةُ|جملہ؛ اسنادی ترکیب|Clause or sentence|فعل و فاعل یا مبتدا و خبر کے تعلق سے جملہ بنتا ہے۔|حَضَرَ الْمُعَلِّمُ.|استاد حاضر ہوا۔|chat
speech|الْكَلَامُ|مکمل مفید بات|Complete meaningful speech|سننے والے کو مکمل بات سمجھ آئے تو اسے کلام کہتے ہیں۔|الْجَوُّ جَمِيلٌ.|موسم خوش گوار ہے۔|chat
compound|الْمُرَكَّبُ|دو یا زیادہ کلمات کی ترکیب|Compound expression|مرکب مکمل جملہ بھی ہو سکتا ہے اور ادھوری نسبت بھی۔|بَابُ الْمَدْرَسَةِ.|مدرسے کا دروازہ۔|blocks
nominal|الْجُمْلَةُ الِاسْمِيَّةُ|اسمی جملہ|Nominal sentence|اس کی بنیادی نسبت مبتدا اور خبر سے قائم ہوتی ہے۔|الطَّالِبُ مُجْتَهِدٌ.|طالب علم محنتی ہے۔|chat
verbal|الْجُمْلَةُ الْفِعْلِيَّةُ|فعلی جملہ|Verbal sentence|اس کی بنیادی نسبت فعل اور فاعل یا نائب فاعل سے قائم ہوتی ہے۔|قَرَأَ الطَّالِبُ.|طالب علم نے پڑھا۔|bolt
topic|الْمُبْتَدَأُ|اسمی جملے کا موضوع|Subject or topic of a nominal sentence|جس کے بارے میں خبر دی جائے؛ اصل حالت میں مرفوع ہوتا ہے۔|الطَّالِبُ حَاضِرٌ.|طالب علم حاضر ہے؛ الطالب مبتدا ہے۔|person
predicate|الْخَبَرُ|مبتدا کے بارے میں خبر|Predicate|خبر مفرد، جملہ یا شبہ جملہ کی صورت میں آ سکتی ہے۔|الْعِلْمُ نَافِعٌ.|علم فائدہ مند ہے؛ نافع خبر ہے۔|chat
predicand|الْمُسْنَدُ إِلَيْهِ|جس کی طرف بات منسوب ہو|Subject of predication|اسمی جملے میں مبتدا، اور بنیادی فعلی جملے میں فاعل اس کی مثال ہے۔|وَصَلَ الضَّيْفُ.|مہمان پہنچا؛ مہمان مسند الیہ ہے۔|person
predication|الْمُسْنَدُ|منسوب کی جانے والی بات|Predicate in predication|اسمی جملے میں خبر اور فعلی جملے میں فعل مسند ہوتا ہے۔|وَصَلَ الضَّيْفُ.|مہمان پہنچا؛ پہنچنے کا فعل مسند ہے۔|chat
declarative|الْخَبَرِيَّةُ|خبر دینے والی ساخت|Declarative construction|جس میں کسی واقعے یا نسبت کی خبر ہو۔|حَضَرَ خَالِدٌ.|خالد حاضر ہوا۔|chat
performative|الْإِنْشَاءُ|طلب یا کسی معنی کا انشاء|Non-declarative or performative expression|امر، نہی، سوال، ندا اور تعجب اس کے معروف اسالیب ہیں۔|اِقْرَأْ.|پڑھو۔|spark
question|الِاسْتِفْهَامُ|پوچھنا؛ سوال کرنا|Interrogation|ہمزہ، هل اور استفہامی اسماء سے سوال بنایا جاتا ہے۔|هَلْ فَهِمْتَ؟|کیا تم سمجھ گئے؟|question
prohibition|النَّهْيُ|کام سے روکنا|Prohibition|لا ناہیہ کے بعد مضارع مجزوم ہوتا ہے۔|لَا تَكْذِبْ.|جھوٹ نہ بولو۔|shield
command|الْأَمْرُ|کام کا حکم یا طلب|Command or imperative|اُكْتُبْ میں لکھنے کا مطالبہ ہے۔|اُكْتُبْ رِسَالَةً.|ایک خط لکھو۔|bolt
wish|التَّمَنِّي|خواہش ظاہر کرنا|Wish|لیت کا استعمال خواہش کے اظہار کے لیے معروف ہے۔|لَيْتَ الْوَقْتَ طَوِيلٌ.|کاش وقت زیادہ ہوتا۔|star
hope|التَّرَجِّي|امید ظاہر کرنا|Hope or expectation|لعل کے ذریعے کسی بات کی امید ظاہر کی جاتی ہے۔|لَعَلَّ الْمَرِيضَ قَرِيبٌ مِنَ الشِّفَاءِ.|امید ہے مریض صحت یابی کے قریب ہے۔|sun
vocative|النِّدَاءُ|پکارنا؛ متوجہ کرنا|Address or calling|یا اور دوسرے حروف ندا سے مخاطب کو متوجہ کیا جاتا ہے۔|يَا صَدِيقُ!|اے دوست!|speaker
exclamation|التَّعَجُّبُ|حیرت یا غیر معمول کیفیت کا اظہار|Exclamation of wonder|ما أفعله اور أفعل به اس کے دو معروف قیاسی اسلوب ہیں۔|مَا أَجْمَلَ الْحَدِيقَةَ!|باغ کتنا خوب صورت ہے!|spark
conditional|الشَّرْطُ|ایک بات کو دوسری پر موقوف کرنا|Condition|فعل شرط اور جواب شرط کا تعلق سمجھنا ضروری ہے۔|إِنْ تَجْتَهِدْ تَنْجَحْ.|اگر محنت کرو گے تو کامیاب ہوگے۔|branch
answer-condition|جَوَابُ الشَّرْطِ|شرط کا نتیجہ|Result clause of a condition|یہ بتاتا ہے کہ شرط پوری ہونے پر کیا ہوگا۔|إِنْ تَقْرَأْ تَفْهَمْ.|اگر پڑھو گے تو سمجھو گے؛ تفهم جواب ہے۔|branch
cause-clause|الْمُعَلِّلَةُ|علت بیان کرنے والا جملہ|Causal explanatory clause|پچھلی بات کی وجہ واضح کرتا ہے۔|لَا تُهْمِلْ؛ فَإِنَّ الْعِلْمَ نَافِعٌ.|غفلت نہ کرو، کیونکہ علم فائدہ مند ہے۔|lamp
parenthesis|الْمُعْتَرِضَةُ|درمیان آنے والا ضمنی جملہ|Parenthetical clause|اسے الگ کرنے پر اصل کلام کی بنیادی ساخت قائم رہتی ہے۔|جَاءَ خَالِدٌ، حَفِظَهُ اللّٰهُ، مُبْتَسِمًا.|خالد، اللہ اسے محفوظ رکھے، مسکراتا ہوا آیا۔|brackets
case|الْإِعْرَابُ|عامل کے لحاظ سے آخری کیفیت|Grammatical inflection|لفظ کے کردار کے مطابق اعراب اور اس کی علامت پہچانی جاتی ہے۔|جَاءَ زَيْدٌ؛ رَأَيْتُ زَيْدًا.|زید آیا؛ میں نے زید کو دیکھا۔|scales
inflectable|الْمُعْرَبُ|اعراب قبول کرنے والا لفظ|Inflectable word|عامل بدلنے سے اس کے آخری اعراب میں تبدیلی آ سکتی ہے۔|الطَّالِبُ، الطَّالِبَ، الطَّالِبِ.|طالب کا رفع، نصب اور جر میں استعمال۔|scales
indeclinable|الْمَبْنِيُّ|مقرر بنا رکھنے والا لفظ|Indeclinable word|عامل بدلنے پر بھی آخری بنا قائم رہتی ہے؛ محل بدل سکتا ہے۔|جَاءَ هٰذَا؛ رَأَيْتُ هٰذَا.|یہ آیا؛ میں نے اسے دیکھا۔|lock
agent|الْعَامِلُ|اعراب کا سبب بننے والا عنصر|Grammatical governor|حرف، فعل، اسم یا معنوی سبب عامل ہو سکتا ہے۔|فِي الْفَصْلِ.|کلاس میں؛ في حرف جر عامل ہے۔|gear
governed|الْمَعْمُولُ|عامل کا اثر قبول کرنے والا لفظ|Governed word|اعرابی اثر جس لفظ پر آئے وہ معمول ہے۔|فِي الْفَصْلِ.|کلاس میں؛ الفصل مجرور معمول ہے۔|target
position|الْمَحَلُّ الْإِعْرَابِيُّ|جملے میں اعرابی مقام|Syntactic case position|مبنی لفظ کی بنا وہی رہتے ہوئے محل رفع یا نصب وغیرہ ہو سکتا ہے۔|رَأَيْتُ هٰذَا.|میں نے اسے دیکھا؛ هذا محل نصب میں ہے۔|pin
pronoun|الضَّمِيرُ|متکلم، مخاطب یا غائب کا اسم|Pronoun|ضمیر کس کی طرف لوٹ رہی ہے، یہ اس کے مرجع سے واضح ہوتا ہے۔|هُوَ مُعَلِّمٌ.|وہ استاد ہے۔|person
attached|الْمُتَّصِلُ|دوسرے لفظ سے جڑا ہوا|Attached form|ضمیر متصل الگ نہیں لکھی جاتی، جیسے کتابه کی ہاء۔|كِتَابُهُ جَدِيدٌ.|اس کی کتاب نئی ہے۔|link
detached|الْمُنْفَصِلُ|الگ آنے والا|Independent form|ضمیر منفصل الگ لفظ کے طور پر آتی ہے۔|أَنَا طَالِبٌ.|میں طالب علم ہوں۔|blocks
implicit|الْمُسْتَتِرُ|لفظاً ظاہر نہ ہونے والا|Implicit or concealed|مستتر ضمیر صیغے اور سیاق سے سمجھی جاتی ہے۔|اُكْتُبْ.|لکھو؛ فاعل أنت مستتر ہے۔|eye
demonstrative|اسْمُ الْإِشَارَةِ|اشارہ کرنے والا اسم|Demonstrative|قریب، بعید، جنس اور عدد کے مطابق صورتیں الگ ہوتی ہیں۔|هٰذَا كِتَابٌ.|یہ کتاب ہے۔|pin
relative|الِاسْمُ الْمَوْصُولُ|صلے سے معنی مکمل کرنے والا اسم|Relative pronoun|الذي اور التي کے بعد وضاحتی صلہ آتا ہے۔|جَاءَ الَّذِي سَاعَدَنِي.|وہ آیا جس نے میری مدد کی۔|link
relative-clause|الصِّلَةُ|موصول کے بعد وضاحتی جملہ|Relative clause|اسم موصول کا مفہوم مکمل کرتا ہے۔|جَاءَ الَّذِي سَاعَدَنِي.|اس نے میری مدد کی: موصول کا صلہ۔|link
antecedent|الْمَرْجِعُ|ضمیر سے مراد شخص یا چیز|Antecedent or referent|ضمیر کا صحیح معنی اس کے مرجع سے متعین ہوتا ہے۔|جَاءَ خَالِدٌ وَمَعَهُ كِتَابٌ.|خالد آیا اور اس کے ساتھ کتاب تھی؛ ہاء خالد کی طرف ہے۔|target
verb-noun|اسْمُ الْفِعْلِ|فعل کے معنی و عمل والا اسم|Verb-like noun|یہ ظاہری فعل نہیں مگر کسی فعل کے معنی اور عمل پر آتا ہے۔|صَهْ!|خاموش ہو جاؤ!|speaker
sound-noun|اسْمُ الصَّوْتِ|آواز کی نقل یا صوتی خطاب|Sound word or sound-name|آواز کی نقل کو فعل کے حکم یا خبر سے الگ سمجھیں۔|غَاقِ.|کوّے کی آواز کی نقل۔|speaker
nisba|الِاسْمُ الْمَنْسُوبُ|تعلق ظاہر کرنے والا اسم|Relational adjective or nisba|یائے نسبت کسی جگہ، فن یا گروہ سے تعلق ظاہر کرتی ہے۔|عَالِمٌ مَكِّيٌّ.|مکہ سے نسبت رکھنے والا عالم۔|pin
diminutive|التَّصْغِيرُ|چھوٹا پن یا قربت بتانے والی ساخت|Diminution|چھوٹا پن، محبت یا تحقیر کا صحیح پہلو سیاق بتاتا ہے۔|كُتَيِّبٌ.|چھوٹی کتاب یا کتابچہ۔|zoom
definite|الْمَعْرِفَةُ|متعین اسم|Definite noun|کسی مخصوص یا معلوم فرد یا چیز کی طرف اشارہ کرتا ہے۔|الْكِتَابُ جَدِيدٌ.|کتاب نئی ہے؛ الکتاب متعین ہے۔|target
indefinite|النَّكِرَةُ|غیر متعین اسم|Indefinite noun|کسی ایک غیر متعین فرد یا جنس کا معنی دیتا ہے۔|عِنْدِي قَلَمٌ.|میرے پاس ایک قلم ہے۔|question
proper|الْعَلَمُ|مخصوص نام|Proper name|کسی مخصوص شخص یا جگہ کا مقرر نام ہے۔|حَضَرَ خَالِدٌ.|خالد حاضر ہوا۔|tag
masculine|الْمُذَكَّرُ|مذکر|Masculine|نحوی جنس کی ایک قسم؛ ظاہری معنی کے ساتھ لغوی استعمال بھی دیکھیں۔|طَالِبٌ مُجْتَهِدٌ.|محنتی طالب علم۔|person
feminine|الْمُؤَنَّثُ|مؤنث|Feminine|ظاہری علامت یا سماعی استعمال سے تانیث معلوم ہوتی ہے۔|طَالِبَةٌ مُجْتَهِدَةٌ.|محنتی طالبہ۔|person
singular|الْمُفْرَدُ|واحد؛ ایک فرد کی صورت|Singular|عدد کے باب میں ایک فرد مراد ہے؛ بعض دوسرے ابواب میں مفرد کی اصطلاح مختلف ہے۔|كِتَابٌ.|ایک کتاب۔|one
dual|الْمُثَنَّى|تثنیہ؛ دو کی صورت|Dual|رفع میں الف اور نصب و جر میں یاء اس کی نمایاں علامتیں ہیں۔|كِتَابَانِ.|دو کتابیں۔|two
plural|الْجَمْعُ|جمع؛ تین یا زیادہ کی صورت|Plural|سالم اور مکسر کی صورتیں الگ پہچانی جاتی ہیں۔|كُتُبٌ.|کتابیں۔|group
sound-plural|الْجَمْعُ السَّالِمُ|اصل ساخت محفوظ رکھنے والی جمع|Sound plural|جمع بنانے میں آخر کی علامت بڑھتی ہے اور بنیادی ساخت عموماً محفوظ رہتی ہے۔|مُعَلِّمُونَ؛ مُعَلِّمَاتٌ.|استاد؛ معلمات۔|group
broken-plural|جَمْعُ التَّكْسِيرِ|اندرونی وزن بدلنے والی جمع|Broken plural|واحد کی ساخت بدلتی ہے، جیسے کتاب سے کتب۔|كِتَابٌ؛ كُتُبٌ.|کتاب؛ کتابیں۔|blocks
pattern|الْوَزْنُ|لفظ کی ساخت کا پیمانہ|Morphological pattern|ف، ع اور ل کے ذریعے حروف کی ساخت کا تقابل کیا جاتا ہے۔|كَاتِبٌ عَلَى وَزْنِ فَاعِلٍ.|کاتب کا وزن فاعل ہے۔|scales
triptote|الْمُنْصَرِفُ|تنوین اور عام حرکی اعراب لینے والا اسم|Triptote|عام حالت میں رفع ضمہ، نصب فتحہ اور جر کسرہ سے ہوتا ہے۔|زَيْدٌ، زَيْدًا، زَيْدٍ.|زید کے تین اعرابی استعمال۔|scales
diptote|غَيْرُ الْمُنْصَرِفِ|عام حالت میں تنوین نہ لینے والا اسم|Diptote|ال اور اضافت نہ ہوں تو جر میں بھی فتحہ آتا ہے؛ یہ مبنی نہیں۔|مَرَرْتُ بِأَحْمَدَ.|میں احمد کے پاس سے گزرا۔|lock
nominative|الرَّفْعُ|حالت رفع|Nominative case|فاعل، مبتدا اور خبر جیسے کرداروں کا بنیادی اعراب ہے؛ علامت اسم کے مطابق بدلتی ہے۔|جَاءَ الطَّالِبُ.|طالب علم آیا۔|up
accusative|النَّصْبُ|حالت نصب|Accusative case|مفعول بہ، حال اور تمییز جیسے کرداروں میں آتی ہے۔|رَأَيْتُ الطَّالِبَ.|میں نے طالب علم کو دیکھا۔|target
genitive|الْجَرُّ|حالت جر|Genitive case|اسم پر حرف جر یا اضافت کا تعلق ہو تو جر آتا ہے۔|مَرَرْتُ بِالطَّالِبِ.|میں طالب علم کے پاس سے گزرا۔|link
jussive|الْجَزْمُ|مضارع کی حالت جزم|Jussive mood|جازم کے بعد معرب مضارع کا حکم؛ فعل کی نوع کے مطابق علامت بدلتی ہے۔|لَمْ يَكْتُبْ.|اس نے نہیں لکھا۔|shield
damma|الضَّمَّةُ|پیش|Damma vowel mark|عام مفرد منصرف میں رفع کی علامت ہے؛ ہر ضمہ کو بلا سیاق رفع نہ کہیں۔|الطَّالِبُ.|طالب کے آخر پر ضمہ۔|marks
fatha|الْفَتْحَةُ|زبر|Fatha vowel mark|عام مفرد منصرف میں نصب کی علامت ہے؛ دوسرے استعمال بھی ہوتے ہیں۔|الطَّالِبَ.|طالب کے آخر پر فتحہ۔|marks
kasra|الْكَسْرَةُ|زیر|Kasra vowel mark|عام مفرد منصرف میں جر، مگر جمع مؤنث سالم میں نصب کی بھی علامت ہے۔|بِالطَّالِبِ.|طالب کے آخر پر کسرہ۔|marks
sukun|السُّكُونُ|سکون؛ حرکت کا نہ ہونا|Sukun mark|صحیح الآخر مضارع کے جزم میں سکون ظاہر ہو سکتا ہے۔|لَمْ يَكْتُبْ.|یکتب کے آخر پر سکون۔|marks
tanwin|التَّنْوِينُ|لفظ کے آخر کی نون ساکن کی آواز|Nunation|عموماً دو حرکات سے لکھی جاتی ہے؛ اس کی نحوی قسمیں الگ ہیں۔|كِتَابٌ.|آخر میں تنوین کے ساتھ کتاب۔|marks
subject|الْفَاعِلُ|فعل کی نسبت والا اسم یا ضمیر|Subject of an active verb|فعل کے ساتھ مرفوع کردار؛ صرف جملے کا پہلا اسم دیکھ کر فیصلہ نہ کریں۔|قَرَأَ الطَّالِبُ.|طالب علم نے پڑھا؛ الطالب فاعل ہے۔|person
passive-subject|نَائِبُ الْفَاعِلِ|مجہول فعل کا مرفوع قائم مقام|Subject of a passive verb|اصل فاعل مذکور نہ ہو تو مفعول اس جگہ مرفوع آ سکتا ہے۔|فُتِحَ الْبَابُ.|دروازہ کھولا گیا۔|swap
active|الْمَعْرُوفُ|فاعل کی نسبت ظاہر کرنے والی فعلی ساخت|Active voice|فعل کے ساتھ فاعل مذکور یا صیغے سے معلوم ہوتا ہے۔|فَتَحَ خَالِدٌ الْبَابَ.|خالد نے دروازہ کھولا۔|person
passive|الْمَجْهُولُ|فاعل کو ذکر کیے بغیر کام کی ساخت|Passive voice|مجہول کا مطلب یہ نہیں کہ اصل کرنے والا حقیقت میں کسی کو معلوم ہی نہیں۔|فُتِحَ الْبَابُ.|دروازہ کھولا گیا۔|swap
object|الْمَفْعُولُ بِهِ|جس پر فعل کا اثر واقع ہو|Direct object|متعدی فعل کے اثر کو قبول کرنے والا اسم یا ضمیر ہے۔|قَرَأْتُ الْكِتَابَ.|میں نے کتاب پڑھی۔|book
absolute|الْمَفْعُولُ الْمُطْلَقُ|فعل کی تاکید، نوع یا تعداد بتانے والا مصدر|Cognate accusative|فعل کے معنی کا مصدر آتا ہے؛ اسے ہر منصوب سے الگ پہچانیں۔|قَرَأْتُ قِرَاءَةً جَيِّدَةً.|میں نے اچھی طرح پڑھا۔|bolt
purpose|الْمَفْعُولُ لَهُ|کام کی غرض یا علت بتانے والا مصدر|Accusative of purpose or cause|متعلقہ شرائط کے ساتھ مصدر بتاتا ہے کہ کام کیوں ہوا۔|قُمْتُ احْتِرَامًا لِلْمُعَلِّمِ.|میں استاد کے احترام میں کھڑا ہوا۔|lamp
accompaniment|الْمَفْعُولُ مَعَهُ|واو معیت کے بعد ساتھ کا منصوب اسم|Accusative of accompaniment|واو کے معنی مع یعنی ساتھ ہوں؛ ہر واو کے بعد یہ حکم نہیں۔|سِرْتُ وَالنَّهْرَ.|میں دریا کے ساتھ ساتھ چلا۔|link
adverbial|الْمَفْعُولُ فِيهِ|وقوع فعل کا وقت یا مقام|Adverbial accusative|اسم ظرف میں في کا مفہوم پایا جاتا ہے۔|سَافَرْتُ لَيْلًا.|میں نے رات کو سفر کیا۔|clock
time-adverb|ظَرْفُ الزَّمَانِ|وقت بتانے والا ظرف|Adverbial of time|بتاتا ہے کہ کام کب ہوا۔|وَصَلْتُ صَبَاحًا.|میں صبح پہنچا۔|clock
place-adverb|ظَرْفُ الْمَكَانِ|جگہ بتانے والا ظرف|Adverbial of place|بتاتا ہے کہ کام کہاں ہوا، متعلقہ ظرفی قواعد کے ساتھ۔|جَلَسْتُ أَمَامَ الْبَيْتِ.|میں گھر کے سامنے بیٹھا۔|pin
circumstance|الْحَالُ|وقوع فعل کے وقت کی کیفیت|Circumstantial qualifier|عموماً نکرہ منصوب؛ اس کا تعلق ذوالحال سے ہوتا ہے۔|رَجَعَ خَالِدٌ مُسْرِعًا.|خالد تیزی سے واپس آیا۔|spark
state-owner|ذُو الْحَالِ|جس کی کیفیت بیان ہو|Referent of the circumstantial qualifier|حال کس کی حالت بتاتی ہے، وہ ذوالحال ہے۔|رَجَعَ خَالِدٌ مُسْرِعًا.|مسرعًا خالد کی کیفیت بتاتا ہے۔|person
specification|التَّمْيِيزُ|مبہم عدد، مقدار یا نسبت کی وضاحت|Specification or distinguishing accusative|حال کی طرح کیفیت بتانا اس کا عمومی مقصد نہیں۔|عِنْدِي عِشْرُونَ كِتَابًا.|میرے پاس بیس کتابیں ہیں۔|target
called|الْمُنَادَى|جسے پکارا جائے|Vocative expression|منادی کی قسم کے مطابق اس کا اعراب یا بنا متعین ہوتی ہے۔|يَا طَالِبَ الْعِلْمِ!|اے علم کے طالب!|speaker
exception|الِاسْتِثْنَاءُ|عام حکم سے الگ کرنا|Exception|مستثنیٰ، مستثنیٰ منہ اور ادات استثناء کو الگ پہچانیں۔|حَضَرَ الطُّلَّابُ إِلَّا خَالِدًا.|خالد کے سوا طالب علم حاضر ہوئے۔|filter
excepted|الْمُسْتَثْنَى|حکم سے الگ کیا جانے والا اسم|Excepted element|اس کا اعراب استثناء کی ساخت سے متعین ہوتا ہے۔|حَضَرَ الطُّلَّابُ إِلَّا خَالِدًا.|خالد مستثنیٰ ہے۔|filter
exception-base|الْمُسْتَثْنَى مِنْهُ|جس جماعت سے استثناء ہو|Set from which an exception is made|تام استثناء میں یہ مذکور ہوتا ہے؛ مفرغ میں مذکور نہیں ہوتا۔|حَضَرَ الطُّلَّابُ إِلَّا خَالِدًا.|الطلاب مستثنیٰ منہ ہے۔|group
connected-exception|الْمُتَّصِلُ فِي الِاسْتِثْنَاءِ|اسی جنس سے استثناء|Connected exception|مستثنیٰ سابق جماعت کی جنس میں شامل ہو۔|حَضَرَ الطُّلَّابُ إِلَّا خَالِدًا.|خالد اسی طالب علم جماعت کا فرد ہے۔|link
disconnected-exception|الْمُنْقَطِعُ|دوسری جنس سے استثناء|Disconnected exception|مستثنیٰ سابق جماعت کی جنس کا فرد نہ ہو۔|حَضَرَ الْقَوْمُ إِلَّا حِمَارًا.|لوگ حاضر ہوئے، مگر گدھا نہیں آیا۔|filter
construct|الْإِضَافَةُ|دو اسموں کا نسبتی تعلق|Genitive construction or idafa|پہلے اسم کو مضاف، دوسرے کو مضاف الیہ کہتے ہیں۔|بَابُ الْمَدْرَسَةِ.|مدرسے کا دروازہ۔|link
construct-head|الْمُضَافُ|اضافت کا پہلا اسم|Head of a genitive construction|اس کا اپنا اعراب جملے کے کردار سے طے ہوتا ہے۔|قَلَمُ الطَّالِبِ جَدِيدٌ.|طالب کا قلم نیا ہے؛ قلم مضاف ہے۔|book
genitive-complement|الْمُضَافُ إِلَيْهِ|اضافت کا دوسرا مجرور اسم|Genitive complement|یہ تعلق ہمیشہ ملکیت ہی نہیں؛ مادہ، وقت یا دوسری نسبت بھی ہو سکتی ہے۔|صَلَاةُ اللَّيْلِ.|رات کی نماز؛ الليل مضاف الیہ ہے۔|link
estimated|الْإِعْرَابُ التَّقْدِيرِيُّ|اعراب جس کی حرکت ظاہر نہ ہو|Estimated inflection|اعرابی حکم موجود ہوتا ہے مگر تلفظ میں اس کی علامت ظاہر نہیں ہوتی۔|رَأَيْتُ مُوسَى.|میں نے موسیٰ کو دیکھا؛ فتحہ مقدر ہے۔|eye
maqsuur|الِاسْمُ الْمَقْصُورُ|آخر میں الف لازم والا معرب اسم|Alif-final inflectable noun|اس کی تینوں اعرابی حرکات الف پر مقدر ہوتی ہیں۔|جَاءَ الْفَتَى.|نوجوان آیا۔|letters
manquus|الِاسْمُ الْمَنْقُوصُ|آخر میں یاء لازم، ماقبل مکسور اسم|Ya-final inflectable noun|رفع و جر میں اعراب مقدر اور نصب ظاہر ہو سکتا ہے۔|رَأَيْتُ الْقَاضِيَ.|میں نے قاضی کو دیکھا۔|letters
follower|التَّابِعُ|اعراب میں دوسرے اسم کا پیرو|Dependent following expression|صفت، تاکید، بدل اور عطف اس کے معروف ابواب ہیں۔|طَالِبٌ مُجْتَهِدٌ.|محنتی طالب علم؛ مجتهد تابع ہے۔|link
followed|الْمَتْبُوعُ|جس کے اعراب کی پیروی ہو|Head followed by a dependent|تابع کا اعراب اس کے تعلق سے سمجھا جاتا ہے۔|طَالِبٌ مُجْتَهِدٌ.|طالب متبوع ہے۔|person
adjective|الصِّفَةُ|موصوف کا وصف یا حالت|Adjective or attributive modifier|حقیقی اور سببی صفت کے قواعد الگ سمجھیں۔|قَلَمٌ جَدِيدٌ.|نیا قلم۔|palette
described|الْمَوْصُوفُ|جس اسم کی صفت بیان ہو|Noun being modified|حقیقی صفت اپنے موصوف کی اہم نحوی خصوصیات کے مطابق ہوتی ہے۔|قَلَمٌ جَدِيدٌ.|قلم موصوف ہے۔|tag
emphasis|التَّوْكِيدُ|بات یا نسبت مضبوط کرنا|Emphasis|لفظی تکرار اور معنوی تاکید کی صورتیں الگ ہیں۔|جَاءَ خَالِدٌ نَفْسُهُ.|خالد خود آیا۔|shield
substitute|الْبَدَلُ|اصل مقصود کو دوسرے اسم سے بیان کرنا|Apposition or substitution|کل، بعض، اشتمال اور غلط اس کی بنیادی تعلیمی قسمیں ہیں۔|قَرَأْتُ الْكِتَابَ نِصْفَهُ.|میں نے کتاب کا نصف پڑھا۔|swap
conjunction|الْعَطْفُ|حرف کے ذریعے شرکت یا ربط|Coordination|معطوف اعراب میں اپنے معطوف علیہ کی پیروی کرتا ہے۔|جَاءَ خَالِدٌ وَسَعِيدٌ.|خالد اور سعید آئے۔|link
conjunct|الْمَعْطُوفُ|حرف عطف کے بعد آنے والا تابع|Conjunct|اعراب پہلے متعلقہ اسم کے مطابق ہوتا ہے۔|رَأَيْتُ خَالِدًا وَسَعِيدًا.|سعیدًا منصوب معطوف ہے۔|link
past|الْمَاضِي|گزرا ہوا زمانہ بتانے والا فعل|Past-tense verb|صیغہ ماضی شرط کے سیاق میں مستقبل کا مفہوم بھی دے سکتا ہے۔|كَتَبَ خَالِدٌ.|خالد نے لکھا۔|clock
imperfect|الْمُضَارِعُ|حال یا مستقبل سے متعلق فعل|Imperfect or present-future verb|ناصب و جازم سے اس کا اعراب بدل سکتا ہے۔|يَكْتُبُ خَالِدٌ.|خالد لکھتا ہے یا لکھ رہا ہے۔|clock
subjunctive-marker|النَّاصِبُ|مضارع کو نصب دینے والا|Subjunctive marker|لن اور أن کے متعلقہ استعمال اس کی مثالیں ہیں۔|لَنْ أَتَأَخَّرَ.|میں دیر نہیں کروں گا۔|gear
jussive-marker|الْجَازِمُ|مضارع کو جزم دینے والا|Jussive marker|لم، لا ناہیہ اور شرطی جوازم کی نوع الگ پہچانیں۔|لَمْ يَحْضُرْ.|وہ حاضر نہیں ہوا۔|gear
intransitive|اللَّازِمُ|براہ راست مفعول بہ کے بغیر مکمل ہونے والا فعل|Intransitive verb|لازم بھی ظرف، حال یا مصدر جیسے دوسرے منصوبات لے سکتا ہے۔|جَلَسَ الطِّفْلُ صَبَاحًا.|بچہ صبح بیٹھا۔|person
transitive|الْمُتَعَدِّي|مفعول بہ تک اثر پہنچانے والا فعل|Transitive verb|ایک، دو یا تین مفعول لینے والے افعال کے الگ ابواب ہیں۔|فَتَحَ خَالِدٌ الْبَابَ.|خالد نے دروازہ کھولا۔|arrow
defective-verb|الْفِعْلُ النَّاقِصُ|اسم کے ساتھ خبر بھی طلب کرنے والا فعل|Copular or incomplete verb|کان و اخوات کے متعلقہ استعمال میں اسم رفع اور خبر نصب ہوتی ہے۔|كَانَ الْجَوُّ بَارِدًا.|موسم ٹھنڈا تھا۔|blocks
praise|الْمَدْحُ|تعریف کرنا|Praise|نعم اور حبذا مدح کے معروف اسالیب ہیں۔|نِعْمَ الرَّجُلُ خَالِدٌ.|خالد کیا خوب آدمی ہے۔|star
blame|الذَّمُّ|مذمت کرنا|Blame|بئس اور ساء ذم کے معروف اسالیب ہیں۔|بِئْسَ الْخُلُقُ الْكَذِبُ.|جھوٹ کیا بری عادت ہے۔|shield
active-participle|اسْمُ الْفَاعِلِ|کام کرنے والے کا مشتق اسم|Active participle|مناسب شرائط کے ساتھ اپنے معروف فعل جیسا عمل کر سکتا ہے۔|كَاتِبٌ.|لکھنے والا۔|pen
passive-participle|اسْمُ الْمَفْعُولِ|جس پر کام ہوا اس کا مشتق اسم|Passive participle|مناسب شرائط کے ساتھ مجہول فعل جیسا عمل کر سکتا ہے۔|مَكْتُوبٌ.|لکھا ہوا۔|paper
verbal-noun|الْمَصْدَرُ|زمانے کے بغیر حدث یا عمل کا نام|Verbal noun|فعل کے معنی کا عمل بتاتا ہے مگر فعل کی طرح زمانہ اس میں شامل نہیں۔|كِتَابَةٌ.|لکھنا؛ تحریر کا عمل۔|pen
derived|الْمُشْتَقُّ|اصل سے بنا ہوا اسم|Derived noun or adjective|کاتب اور مکتوب جیسے الفاظ اصل معنی سے مشتق ہیں۔|كَاتِبٌ؛ مَكْتُوبٌ.|لکھنے والا؛ لکھا ہوا۔|branch
underived|الْجَامِدُ|غیر مشتق اسم|Underived noun|اس کتاب کی ابتدائی تقسیم میں حجر جیسے اصل اسماء کی مثال دی جاتی ہے۔|حَجَرٌ.|پتھر۔|blocks
elative|اسْمُ التَّفْضِيلِ|دو میں زیادہ وصف بتانے والا اسم|Comparative or superlative form|من، ال اور اضافت کے ساتھ اس کی الگ ساختیں آتی ہیں۔|خَالِدٌ أَطْوَلُ مِنْ سَعِيدٍ.|خالد سعید سے زیادہ لمبا ہے۔|up
stable-adjective|الصِّفَةُ الْمُشَبَّهَةُ|ثابت وصف کا مشتق اسم|Adjectival form expressing a stable quality|لازم فعل سے وصف بیان کرتی ہے اور اپنے متعلق میں عمل کر سکتی ہے۔|رَجُلٌ حَسَنٌ خُلُقُهُ.|ایسا آدمی جس کا اخلاق اچھا ہے۔|palette
lexical-governor|الْعَامِلُ اللَّفْظِيُّ|لفظ میں موجود اعرابی عامل|Expressed grammatical governor|حرف، اسم یا فعل کی ظاہر صورت عامل ہوتی ہے۔|مِنَ الْبَيْتِ.|گھر سے؛ من عامل لفظی ہے۔|gear
abstract-governor|الْعَامِلُ الْمَعْنَوِيُّ|نحوی حالت سے سمجھا جانے والا عامل|Abstract grammatical governor|روایتی توضیح میں ابتدا اس کی مثال ہے۔|الْعِلْمُ نُورٌ.|علم روشنی ہے۔|lamp
beginning|الِابْتِدَاءُ|عامل لفظی سے خالی اسمی آغاز|Initial nominal predication|مبتدا کے رفع کی روایتی نحوی توضیح میں یہ معنوی عامل ہے۔|الطَّالِبُ حَاضِرٌ.|طالب علم حاضر ہے۔|sun
negation|النَّفْيُ|کسی بات کی نفی|Negation|نفی کرنے والے لفظ کا عمل اور زمانی معنی سیاق سے متعین ہوتا ہے۔|لَمْ يَحْضُرْ.|وہ حاضر نہیں ہوا۔|shield
confirmation|التَّصْدِيقُ|سابق بات کی تصدیق|Confirmation|نعم اور بلى کا فرق خصوصاً منفی سوال میں سمجھیں۔|هَلْ حَضَرَ؟ نَعَمْ.|کیا وہ حاضر ہوا؟ ہاں۔|check
explanation|التَّفْسِيرُ|پہلے کلام کو واضح کرنا|Explanation|أي اور أن کے تفسیری استعمال الگ پہچانے جاتے ہیں۔|جَاءَ زَيْدٌ أَيْ أَخُوكَ.|زید، یعنی تمہارا بھائی، آیا۔|lamp
attention|التَّنْبِيهُ|سامع کی توجہ دلانا|Calling attention|ألا اور ها کے متعلقہ استعمال توجہ دلاتے ہیں۔|أَلَا إِنَّ الْعِلْمَ نَافِعٌ.|سن لو، بے شک علم فائدہ مند ہے۔|speaker
encouragement|التَّحْضِيضُ|کسی کام پر ابھارنا|Urging or exhortation|هلا جیسے حروف سے طلب یا سیاقی ملامت کا پہلو پیدا ہوتا ہے۔|هَلَّا تَقْرَأُ؟|تم پڑھتے کیوں نہیں؟|bolt
retraction|الْإِضْرَابُ|پہلی بات سے دوسری کی طرف انتقال|Correction or transition with bal|بل کے متعلقہ استعمال میں پہلے سے توجہ ہٹا کر بعد کی بات مقصود ہوتی ہے۔|مَا جَاءَ خَالِدٌ بَلْ سَعِيدٌ.|خالد نہیں، بلکہ سعید آیا۔|swap
contrast|الِاسْتِدْرَاكُ|پچھلی بات کے ممکن تاثر کی اصلاح|Adversative qualification|لكن کے مناسب استعمال میں مخالف پہلو واضح کیا جاتا ہے۔|خَالِدٌ غَائِبٌ لَكِنَّ سَعِيدًا حَاضِرٌ.|خالد غائب ہے لیکن سعید حاضر ہے۔|scales
respite|التَّرَاخِي|ترتیب کے ساتھ زمانی وقفہ|Sequence with an interval|ثم کی نمایاں دلالت میں ترتیب اور وقفہ دونوں آتے ہیں۔|جَاءَ خَالِدٌ ثُمَّ سَعِيدٌ.|خالد آیا، پھر کچھ وقفے کے بعد سعید آیا۔|clock
preposition|حَرْفُ الْجَرِّ|اسم کو جر دینے والا حرف|Preposition or genitive-governing particle|في، من اور إلى کے متعلقہ استعمال اس کی مثالیں ہیں۔|فِي الْبَيْتِ.|گھر میں۔|link
''' )
add('word','''
book-word|كِتَابٌ|کتاب|Book|عام لفظ؛ كُتُبٌ اس کی جمع مکسر ہے۔|الْكِتَابُ جَدِيدٌ.|کتاب نئی ہے۔|book
pen-word|قَلَمٌ|قلم|Pen|اسم واحد؛ أَقْلَامٌ اس کی معروف جمع ہے۔|هٰذَا قَلَمٌ.|یہ قلم ہے۔|pen
student-word|طَالِبٌ|طالب علم|Student|مذکر واحد؛ مؤنث طَالِبَةٌ ہے۔|الطَّالِبُ حَاضِرٌ.|طالب علم حاضر ہے۔|person
student-f-word|طَالِبَةٌ|طالبہ|Female student|تاء مربوطہ کے ساتھ مؤنث اسم۔|الطَّالِبَةُ مُجْتَهِدَةٌ.|طالبہ محنتی ہے۔|person
teacher-word|مُعَلِّمٌ|استاد|Teacher|جمع سالم مُعَلِّمُونَ ہے۔|حَضَرَ الْمُعَلِّمُ.|استاد حاضر ہوا۔|person
door-word|بَابٌ|دروازہ|Door|اضافت میں بَابُ الْبَيْتِ: گھر کا دروازہ۔|الْبَابُ مَفْتُوحٌ.|دروازہ کھلا ہے۔|door
school-word|مَدْرَسَةٌ|مدرسہ؛ اسکول|School|مؤنث اسم؛ جمع مَدَارِسُ ہے۔|هٰذِهِ مَدْرَسَةٌ.|یہ مدرسہ ہے۔|school
house-word|بَيْتٌ|گھر|House|جمع بُيُوتٌ ہے۔|الْبَيْتُ كَبِيرٌ.|گھر بڑا ہے۔|home
class-word|فَصْلٌ|کلاس؛ درسی کمرہ|Classroom|یہاں تعلیمی جگہ کا معنی ہے؛ فصل کے دوسرے معنی سیاق سے آتے ہیں۔|الطَّالِبُ فِي الْفَصْلِ.|طالب علم کلاس میں ہے۔|school
bag-word|حَقِيبَةٌ|بستہ؛ بیگ|Bag|مؤنث اسم، جس میں کتاب یا سامان رکھا جاتا ہے۔|الْكِتَابُ فِي الْحَقِيبَةِ.|کتاب بستے میں ہے۔|bag
desk-word|مَكْتَبٌ|میز؛ لکھنے کی میز|Desk|یہاں جگہ رکھنے والی میز مراد ہے؛ دفتر کا معنی بھی سیاق میں آ سکتا ہے۔|الْقَلَمُ عَلَى الْمَكْتَبِ.|قلم میز پر ہے۔|desk
lesson-word|دَرْسٌ|سبق|Lesson|دُرُوسٌ اس کی جمع ہے۔|فَهِمْتُ الدَّرْسَ.|میں نے سبق سمجھ لیا۔|book
knowledge-word|عِلْمٌ|علم؛ جاننا|Knowledge|یہاں علم و معلومات کا معنی، لفظ عَلم یعنی جھنڈا سے الگ ہے۔|الْعِلْمُ نَافِعٌ.|علم فائدہ مند ہے۔|lamp
light-word|نُورٌ|روشنی|Light|حسی روشنی اور مجازی ہدایت کے لیے سیاق کے مطابق آتا ہے۔|الْعِلْمُ نُورٌ.|علم روشنی ہے۔|sun
guest-word|ضَيْفٌ|مہمان|Guest|جملے میں فاعل یا مفعول ہونے سے اعراب بدل سکتا ہے۔|وَصَلَ الضَّيْفُ.|مہمان پہنچ گیا۔|person
friend-word|صَدِيقٌ|دوست|Friend|ندا میں معین مخاطب ہو تو يَا صَدِيقُ کہا جا سکتا ہے۔|يَا صَدِيقُ!|اے دوست!|group
child-word|طِفْلٌ|بچہ|Child|جمع أَطْفَالٌ ہے۔|جَلَسَ الطِّفْلُ.|بچہ بیٹھا۔|person
man-word|رَجُلٌ|آدمی؛ مرد|Man|جمع رِجَالٌ ہے۔|حَضَرَ رَجُلٌ.|ایک آدمی حاضر ہوا۔|person
woman-word|اِمْرَأَةٌ|عورت|Woman|مؤنث حقیقی؛ نِسَاءٌ اس کی جمع کا کام کرتا ہے۔|حَضَرَتِ امْرَأَةٌ.|ایک عورت حاضر ہوئی۔|person
father-word|أَبٌ|والد؛ باپ|Father|اسماء ستہ میں مخصوص شرائط کے ساتھ حرفی اعراب لیتا ہے۔|حَضَرَ أَبُوكَ.|تمہارے والد حاضر ہوئے۔|group
brother-word|أَخٌ|بھائی|Brother|اسماء ستہ میں متعلقہ شرطوں کے ساتھ أَخُوكَ وغیرہ آتا ہے۔|أَخُوكَ حَاضِرٌ.|تمہارا بھائی حاضر ہے۔|group
sun-word|شَمْسٌ|سورج|Sun|عربی میں سماعی مؤنث ہے، اگرچہ ظاہری تاء نہیں۔|طَلَعَتِ الشَّمْسُ.|سورج نکلا۔|sun
moon-word|قَمَرٌ|چاند|Moon|مذکر اسم۔|الْقَمَرُ جَمِيلٌ.|چاند خوب صورت ہے۔|moon
earth-word|أَرْضٌ|زمین|Earth or land|عربی میں مؤنث اسم؛ تصغیر میں أُرَيْضَةٌ آتا ہے۔|هٰذِهِ أَرْضٌ وَاسِعَةٌ.|یہ کشادہ زمین ہے۔|globe
garden-word|حَدِيقَةٌ|باغ|Garden|مؤنث اسم؛ جمع حَدَائِقُ ہے۔|الْحَدِيقَةُ جَمِيلَةٌ.|باغ خوب صورت ہے۔|leaf
tree-word|شَجَرَةٌ|درخت|Tree|تاء مربوطہ کے ساتھ مؤنث اسم۔|هٰذِهِ شَجَرَةٌ.|یہ درخت ہے۔|leaf
water-word|مَاءٌ|پانی|Water|مِيَاهٌ اس کی معروف جمع ہے۔|الْمَاءُ بَارِدٌ.|پانی ٹھنڈا ہے۔|drop
river-word|نَهْرٌ|دریا|River|مفعول معہ کی مثال میں ساتھ چلنے کی نسبت آتی ہے۔|سِرْتُ وَالنَّهْرَ.|میں دریا کے ساتھ ساتھ چلا۔|drop
morning-word|صَبَاحٌ|صبح|Morning|ظرفی استعمال میں صَبَاحًا منصوب آ سکتا ہے۔|وَصَلْتُ صَبَاحًا.|میں صبح پہنچا۔|sun
night-word|لَيْلٌ|رات|Night|ظرفی استعمال لَيْلًا: رات کو۔|سَافَرْتُ لَيْلًا.|میں نے رات کو سفر کیا۔|moon
day-word|يَوْمٌ|دن|Day|وقت کی مقدار یا خاص دن سیاق سے متعین ہوتا ہے۔|هٰذَا يَوْمٌ جَمِيلٌ.|یہ خوب صورت دن ہے۔|calendar
time-word|وَقْتٌ|وقت|Time|مذکر اسم؛ أَوْقَاتٌ اس کی جمع ہے۔|الْوَقْتُ قَصِيرٌ.|وقت کم ہے۔|clock
letter-word|رِسَالَةٌ|خط؛ پیغام|Letter or message|فعل كتب کے بعد مفعول کی مثال میں آتا ہے۔|كَتَبْتُ رِسَالَةً.|میں نے خط لکھا۔|paper
news-word|خَبَرٌ|اطلاع؛ خبر|News or information|عام لفظ کا معنی خبر ہے؛ نحوی الخبر کی اصطلاح الگ کارڈ میں ہے۔|الْخَبَرُ صَحِيحٌ.|خبر درست ہے۔|paper
judge-word|قَاضٍ|قاضی؛ فیصلہ کرنے والا|Judge|اسم منقوص کی نکرہ رفع و جر کی مثال؛ معرفہ الْقَاضِي ہے۔|جَاءَ قَاضٍ.|ایک قاضی آیا۔|scales
stone-word|حَجَرٌ|پتھر|Stone|جامد اسم کی ایک سادہ مثال۔|هٰذَا حَجَرٌ.|یہ پتھر ہے۔|blocks
new-word|جَدِيدٌ|نیا|New|مؤنث جَدِيدَةٌ ہے؛ صفت یا خبر ہو سکتا ہے۔|كِتَابٌ جَدِيدٌ.|نئی کتاب۔|spark
beautiful-word|جَمِيلٌ|خوب صورت|Beautiful|مؤنث جَمِيلَةٌ ہے۔|الْجَوُّ جَمِيلٌ.|موسم خوش گوار ہے۔|palette
useful-word|نَافِعٌ|فائدہ مند|Useful or beneficial|خبر یا صفت کے طور پر آ سکتا ہے۔|الْعِلْمُ نَافِعٌ.|علم فائدہ مند ہے۔|lamp
diligent-word|مُجْتَهِدٌ|محنتی|Diligent|مؤنث مُجْتَهِدَةٌ ہے؛ صفت و خبر کی مثالوں میں مفید لفظ ہے۔|الطَّالِبُ مُجْتَهِدٌ.|طالب علم محنتی ہے۔|star
present-word|حَاضِرٌ|حاضر؛ موجود|Present|غَائِبٌ اس کا متعلقہ متضاد ہے۔|الْمُعَلِّمُ حَاضِرٌ.|استاد حاضر ہے۔|check
absent-word|غَائِبٌ|غیر حاضر|Absent|حاضر کے مقابل غیر موجود شخص کے لیے۔|الطَّالِبُ غَائِبٌ.|طالب علم غیر حاضر ہے۔|person
cold-word|بَارِدٌ|ٹھنڈا|Cold|پانی یا موسم کی کیفیت بتا سکتا ہے۔|الْمَاءُ بَارِدٌ.|پانی ٹھنڈا ہے۔|drop
open-word|مَفْتُوحٌ|کھلا ہوا|Open|فعل فتح سے اسم مفعول کی مثال۔|الْبَابُ مَفْتُوحٌ.|دروازہ کھلا ہے۔|door
written-word|مَكْتُوبٌ|لکھا ہوا|Written|كتب سے اسم مفعول؛ مصدر كتابة سے الگ صورت ہے۔|الدَّرْسُ مَكْتُوبٌ.|سبق لکھا ہوا ہے۔|paper
smiling-word|مُبْتَسِمٌ|مسکراتا ہوا|Smiling|حال میں مُبْتَسِمًا کی صورت آ سکتی ہے۔|دَخَلَ مُبْتَسِمًا.|وہ مسکراتا ہوا داخل ہوا۔|smile
hurried-word|مُسْرِعٌ|جلدی کرنے والا؛ تیزی سے چلنے والا|Hurrying or moving quickly|حال کی مثال میں مُسْرِعًا منصوب آتا ہے۔|رَجَعَ خَالِدٌ مُسْرِعًا.|خالد تیزی سے واپس آیا۔|bolt
read-word|قَرَأَ|اس نے پڑھا|He read|فعل ماضی؛ مضارع يَقْرَأُ ہے۔|قَرَأَ الطَّالِبُ الْكِتَابَ.|طالب علم نے کتاب پڑھی۔|book
write-word|كَتَبَ|اس نے لکھا|He wrote|فعل ماضی؛ مضارع يَكْتُبُ ہے۔|كَتَبَ خَالِدٌ رِسَالَةً.|خالد نے خط لکھا۔|pen
understand-word|فَهِمَ|وہ سمجھا|He understood|فعل ماضی؛ مضارع يَفْهَمُ ہے۔|فَهِمْتُ الدَّرْسَ.|میں نے سبق سمجھ لیا۔|lamp
arrive-word|وَصَلَ|وہ پہنچا|He arrived|لازم فعل کی سادہ مثال۔|وَصَلَ الضَّيْفُ.|مہمان پہنچا۔|pin
attend-word|حَضَرَ|وہ حاضر ہوا|He attended or was present|فعل ماضی؛ مضارع يَحْضُرُ ہے۔|حَضَرَ الْمُعَلِّمُ.|استاد حاضر ہوا۔|check
sit-word|جَلَسَ|وہ بیٹھا|He sat|لازم فعل؛ وقت یا جگہ کا متعلق بھی لے سکتا ہے۔|جَلَسَ الطِّفْلُ.|بچہ بیٹھا۔|desk
enter-word|دَخَلَ|وہ داخل ہوا|He entered|فعل ماضی؛ مضارع يَدْخُلُ ہے۔|دَخَلَ الْمُعَلِّمُ.|استاد داخل ہوا۔|door
return-word|رَجَعَ|وہ واپس آیا|He returned|لازم فعل کے ساتھ حال کی مثال بن سکتی ہے۔|رَجَعَ مُسْرِعًا.|وہ تیزی سے واپس آیا۔|arrow
travel-word|سَافَرَ|اس نے سفر کیا|He travelled|فعل ماضی؛ ظرف زمان کے ساتھ آ سکتا ہے۔|سَافَرَ خَالِدٌ لَيْلًا.|خالد نے رات کو سفر کیا۔|globe
open-verb-word|فَتَحَ|اس نے کھولا|He opened|متعدی فعل؛ دروازہ مفعول کی مثال ہے۔|فَتَحَ خَالِدٌ الْبَابَ.|خالد نے دروازہ کھولا۔|door
see-word|رَأَى|اس نے دیکھا|He saw|یہاں بصری دیکھنا مراد ہے؛ قلبی معنی میں عمل مختلف ہو سکتا ہے۔|رَأَيْتُ الْقَمَرَ.|میں نے چاند دیکھا۔|eye
give-word|أَعْطَى|اس نے دیا|He gave|دو مفعول کی معروف مثال؛ لینے والا اور دی ہوئی چیز۔|أَعْطَيْتُ الطِّفْلَ كِتَابًا.|میں نے بچے کو کتاب دی۔|gift
think-word|ظَنَّ|اس نے گمان کیا؛ سمجھا|He thought or supposed|قلبی معنی میں اصل مبتدا و خبر کو دو مفعول بنا سکتا ہے۔|ظَنَنْتُ الطَّالِبَ غَائِبًا.|میں نے طالب علم کو غیر حاضر سمجھا۔|question
be-word|كَانَ|وہ تھا|Was|ناقص استعمال میں اسم مرفوع اور خبر منصوب کرتا ہے۔|كَانَ الْجَوُّ بَارِدًا.|موسم ٹھنڈا تھا۔|clock
become-word|صَارَ|وہ ہوگیا|Became|کان و اخوات میں حالت کی تبدیلی بتاتا ہے۔|صَارَ الْمَاءُ بَارِدًا.|پانی ٹھنڈا ہوگیا۔|swap
indeed-word|إِنَّ|بے شک؛ یقیناً|Indeed or certainly|اسم کو نصب اور خبر کو رفع دیتا ہے۔|إِنَّ الْعِلْمَ نَافِعٌ.|بے شک علم فائدہ مند ہے۔|check
in-word|فِي|میں؛ اندر|In|حرف جر کے استعمال میں بعد کا اسم مجرور ہوتا ہے۔|فِي الْبَيْتِ.|گھر میں۔|home
from-word|مِنْ|سے|From|ابتدا یا دوسرے معنوی تعلق کا فیصلہ سیاق سے ہوتا ہے۔|خَرَجَ مِنَ الْبَيْتِ.|وہ گھر سے نکلا۔|arrow
to-word|إِلَى|تک؛ کی طرف|To or towards|حرف جر؛ سمت یا انتہا کا معروف معنی۔|ذَهَبَ إِلَى الْمَدْرَسَةِ.|وہ مدرسے کی طرف گیا۔|arrow
on-word|عَلَى|پر|On or upon|حرف جر؛ استعلاء کا معروف معنی۔|الْقَلَمُ عَلَى الْمَكْتَبِ.|قلم میز پر ہے۔|desk
except-word|إِلَّا|سوائے؛ مگر|Except|استثناء کی قسم دیکھ کر بعد کے لفظ کا اعراب طے کریں۔|حَضَرُوا إِلَّا خَالِدًا.|خالد کے سوا وہ حاضر ہوئے۔|filter
and-word|وَ|اور|And|عطف کے استعمال میں بنیادی شرکت؛ واو کے دوسرے استعمال بھی ہیں۔|خَالِدٌ وَسَعِيدٌ.|خالد اور سعید۔|link
then-word|ثُمَّ|پھر؛ وقفے کے بعد|Then, after an interval|عطف میں ترتیب اور تراخی کا معنی دیتا ہے۔|جَاءَ خَالِدٌ ثُمَّ سَعِيدٌ.|خالد آیا، پھر سعید آیا۔|clock
yes-word|نَعَمْ|ہاں؛ سابق بات کی تصدیق|Yes; confirmation|منفی سوال کے جواب میں بلى سے معنوی فرق ملحوظ رکھیں۔|هَلْ حَضَرَ؟ نَعَمْ.|کیا وہ حاضر ہوا؟ ہاں۔|check
yes-negative-word|بَلَى|کیوں نہیں؛ نفی کو رد کرنے والا ہاں|Yes, contradicting a negative|منفی سوال میں مثبت واقعہ ثابت کرتا ہے۔|أَلَمْ يَحْضُرْ؟ بَلَى.|کیا وہ نہیں آیا؟ کیوں نہیں، آیا تھا۔|check
this-word|هٰذَا|یہ؛ مذکر واحد قریب|This, masculine singular|اسم اشارہ؛ جملے میں بنا وہی رہتے ہوئے محل بدل سکتا ہے۔|هٰذَا كِتَابٌ.|یہ کتاب ہے۔|pin
that-word|ذٰلِكَ|وہ؛ مذکر واحد بعید|That, masculine singular|دور کے مذکر واحد کی طرف اشارہ۔|ذٰلِكَ بَيْتٌ.|وہ گھر ہے۔|pin
who-word|مَنْ|کون؛ جو شخص|Who or whoever|سوال، موصول یا شرط کا صحیح معنی سیاق سے ہوتا ہے۔|مَنْ حَضَرَ؟|کون حاضر ہوا؟|question
when-word|مَتَى|کب|When|استفہام یا شرط میں وقت سے تعلق بتاتا ہے۔|مَتَى تَحْضُرُ؟|تم کب آؤ گے؟|clock
where-word|أَيْنَ|کہاں|Where|مقام پوچھنے کا استفہامی اسم۔|أَيْنَ الْكِتَابُ؟|کتاب کہاں ہے؟|pin
how-word|كَيْفَ|کیسا؛ کس طرح|How|کیفیت یا حالت کا سوال۔|كَيْفَ حَالُكَ؟|تمہارا حال کیسا ہے؟|question
how-many-word|كَمْ|کتنے|How many|یہاں استفہامیہ مراد ہے؛ خبریہ میں کثرت کا معنی آتا ہے۔|كَمْ كِتَابًا قَرَأْتَ؟|تم نے کتنی کتابیں پڑھیں؟|group
not-past-word|لَمْ|نہیں؛ ماضی کی نفی کے لیے|Did not|مضارع کو جزم دیتا ہے اور ماضی کی نفی کا مفہوم پیدا کرتا ہے۔|لَمْ يَكْتُبْ.|اس نے نہیں لکھا۔|shield
not-future-word|لَنْ|نہیں؛ مستقبل کی نفی کے لیے|Will not|مضارع کو نصب دیتا ہے۔|لَنْ أَتَأَخَّرَ.|میں دیر نہیں کروں گا۔|shield
if-word|إِنْ|اگر|If|شرطیہ استعمال میں دو افعال کو جزم دیتا ہے؛ إنَّ سے مختلف ہے۔|إِنْ تَقْرَأْ تَفْهَمْ.|اگر پڑھو گے تو سمجھو گے۔|branch
''')

chapter_keys={
1:'nahw word noun verb particle sentence speech compound nominal verbal topic predicate predicand predication declarative performative question command prohibition wish hope vocative exclamation book-word pen-word student-word read-word arrive-word',
2:'sentence nominal verbal conditional answer-condition cause-clause parenthesis circumstance time-adverb place-adverb teacher-word enter-word smiling-word in-word',
3:'noun verb particle tanwin derived underived verbal-noun past imperfect command prohibition nisba diminutive singular dual plural pen-word write-word student-f-word',
4:'case inflectable indeclinable agent governed position lexical-governor abstract-governor imperfect pronoun this-word student-word see-word not-past-word not-future-word',
5:'pronoun attached detached implicit relative relative-clause antecedent demonstrative verb-noun sound-noun time-adverb place-adverb this-word that-word who-word when-word where-word how-word book-word teacher-word',
6:'nisba derived pattern proper masculine feminine school-word teacher-word knowledge-word book-word',
7:'diminutive pattern noun feminine underived book-word man-word sun-word earth-word stone-word',
8:'definite indefinite proper pronoun demonstrative relative construct construct-head genitive-complement called book-word pen-word teacher-word this-word',
9:'masculine feminine adjective described noun student-word student-f-word man-word woman-word sun-word earth-word tree-word garden-word',
10:'singular dual plural sound-plural broken-plural pattern nominative accusative genitive book-word pen-word teacher-word man-word woman-word water-word',
11:'triptote diptote inflectable case proper adjective pattern feminine tanwin genitive nominative accusative judge-word school-word',
12:'nominative subject passive-subject topic predicate pronoun implicit active passive defective-verb teacher-word student-word door-word attend-word open-verb-word be-word',
13:'accusative object absolute purpose accompaniment adverbial time-adverb place-adverb circumstance state-owner specification called exception excepted exception-base connected-exception disconnected-exception read-word river-word night-word hurried-word friend-word except-word',
14:'genitive preposition construct construct-head genitive-complement attached pronoun dual plural book-word pen-word student-word school-word in-word from-word to-word on-word',
15:'case nominative accusative genitive damma fatha kasra estimated maqsuur manquus dual sound-plural diptote construct father-word brother-word judge-word teacher-word',
16:'follower followed adjective described emphasis substitute conjunction conjunct definite indefinite masculine feminine singular dual plural new-word diligent-word and-word',
17:'agent governed lexical-governor abstract-governor position case verb noun particle write-word student-word lesson-word in-word',
18:'preposition genitive accusative nominative agent defective-verb called vocative exception accompaniment negation indeed-word in-word from-word to-word on-word except-word friend-word father-word',
19:'imperfect past subjunctive-marker jussive-marker jussive accusative conditional answer-condition negation prohibition command not-past-word not-future-word if-word when-word understand-word write-word',
20:'verb active passive subject passive-subject intransitive transitive object defective-verb praise blame exclamation open-verb-word door-word child-word give-word think-word be-word become-word',
21:'noun agent conditional verb-noun active-participle passive-participle stable-adjective elative verbal-noun construct specification adjective how-many-word who-word written-word knowledge-word',
22:'abstract-governor lexical-governor beginning topic predicate imperfect subjunctive-marker jussive-marker knowledge-word light-word useful-word',
23:'particle attention confirmation explanation encouragement retraction contrast respite negation question emphasis conjunction tanwin conditional yes-word yes-negative-word and-word then-word if-word who-word how-word'
}
for n,more in {1:'guest-word letter-word',2:'time-word day-word morning-word',4:'house-word class-word',5:'bag-word desk-word',9:'beautiful-word moon-word',12:'present-word absent-word',13:'travel-word return-word',16:'cold-word open-word',19:'sukun',20:'sit-word news-word'}.items():
 chapter_keys[n]+=' '+more
ids={e['id'] for e in entries};assert len(ids)==len(entries)
assert set(chapter_keys)==set(range(1,24))
chapters={str(n):keys.split() for n,keys in chapter_keys.items()}
for n,keys in chapters.items():
 assert len(keys)==len(set(keys)),n
 assert set(keys)<=ids,(n,set(keys)-ids)
 assert {e['kind'] for e in entries if e['id'] in keys}=={'term','word'},n
used={x for v in chapters.values() for x in v};assert used==ids,ids-used
data={'schemaVersion':1,'titleUr':'الفاظ و اصطلاحات','titleEn':'Words & Grammar Terms','entries':entries,'chapters':chapters}
(ROOT/'data/vocabulary.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'data/vocabulary.js').write_text('window.NAHW_VOCABULARY='+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
print(json.dumps({'uniqueEntries':len(entries),'terms':sum(e['kind']=='term' for e in entries),'words':sum(e['kind']=='word' for e in entries),'chapters':len(chapters)}))
