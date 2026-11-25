import json,re
rv=json.load(open('/home/claude/rev_titles.json'))
lib=json.load(open('/home/claude/quiz/src/data/library.json'))
SW=set('the of and in a an to for on with its how is s'.split())
def clean_lib(t): return re.sub(r'^(?:\d+(?:[._]\d+)?_?)?(?:TOEFL |IELTS |Review )?(?:Reading|Listening)\s*[-_ ]*','',t,flags=re.I).replace('_',' ').strip()
def toks(s): return {w for w in re.findall(r'[a-z]+',s.lower()) if w not in SW and len(w)>2}
def stem(w): return w[:5]
def cleanrev(t):
    t=re.split(r'[^\x00-\x7F]',t)[0]
    t=re.sub(r'\s+[KQ]\s*$','',t)
    return re.sub(r'\s*\(\d\d\.\d\d\.\d\d\)','',t).strip(' /')
BAT=[(1,24,'ชุดหลัก (ก่อน ต.ค. 2568)'),(25,33,'9 เรื่องใหม่ (ต.ค. 2568)'),(34,60,'27 เรื่องใหม่ (17.01.69)'),(61,65,'5 เรื่องใหม่ (21.01.69)'),(66,69,'4 เรื่องใหม่ (31.01.69)'),(70,70,'14.02.69'),(71,71,'28.02.69'),(72,72,'14.03.69'),(73,73,'18.03.69'),(74,77,'28.03.69'),(78,78,'18.04.69'),(79,79,'25.04.69'),(80,80,'09.05.69'),(81,81,'04.07.69')]
MAN=json.load(open('/home/claude/quiz/scripts/manual.json')) if __import__('os').path.exists('/home/claude/quiz/scripts/manual.json') else {}
out=[]
for sec,key in (('Reading','reading'),('Listening','listening')):
    for no,t,_ in rv[key]:
        en=cleanrev(t); alts=[a for a in re.split(r'\s*/\s*|\s+หรือ\s+',en) if a]
        best=[]
        for r in lib:
            if r['type']!=sec or r['status']=='dup': continue
            lt=toks(clean_lib(r['title']))
            sc=0
            for a in alts:
                at=toks(a)
                if not at: continue
                ov=len({stem(w) for w in at}&{stem(w) for w in lt})
                sc=max(sc,ov/min(len(at),max(len(lt),1)))
            if sc>=0.6: best.append((round(sc,2),r['n'],r['status']))
        best.sort(reverse=True)
        k=f'{sec}{no}'
        m=MAN.get(k)
        ids=m if m is not None else [b[1] for b in best if b[0]>=best[0][0]-0.15][:3]
        bt=next((b for x,y,z in [(0,0,0)] for b in BAT if b[0]<=no<=b[1]),None) if sec=='Reading' else None
        APPROX={'Reading2':[69,72,2],'Reading9':[46],'Reading14':[69,72]}
        out.append(dict(approx=APPROX.get(k,[]),sec=sec,no=no,title=en,batch=bt[2] if bt else '',ids=ids,auto=[b[:2] for b in best[:3]]))
json.dump(out,open('/home/claude/quiz/src/data/checklist.json','w'),ensure_ascii=False)
for o in out: print(o['sec'][0],o['no'],'|',o['title'][:55],'|',o['ids'],[ (lib[i-1]['title'][:28]) for i in o['ids']])
