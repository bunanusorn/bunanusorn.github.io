import re, json, sys
SRC='/home/claude/raw.txt'; LAY='/home/claude/big.txt'
raw=open(SRC).read().replace('\f','\n')
lay=open(LAY).read().split('\f')
# ---- TOC (layout) ----
toc_txt='\n'.join(lay).split('Part 1 — Reading')[0].split('\n')
toc={}; date=None; pend=None
for i,l in enumerate(toc_txt):
    m=re.match(r'^\s*(20\d\d-\d\d-\d\d)\b(.*)$',l)
    if m:
        date=m.group(1); rest=m.group(2)
        d=re.search(r'ซ้ำกับ #(\d+)',rest)
        if d: pend=int(d.group(1))
        continue
    m=re.match(r'^\s*(\d+)\s+(Reading|Listening)\s*(.*?)\s*$',l)
    if m:
        n=int(m.group(1)); rest=m.group(3)
        st='ok'
        if 'รอแปล' in rest: st='pending'
        d=re.search(r'ซ้ำกับ #(\d+)',rest)
        dup=int(d.group(1)) if d else pend
        if dup: st='dup'
        title=re.split(r'\s{2,}',rest)[0]
        toc[n]=dict(n=n,type=m.group(2),title=title,date=date,status=st,dup=dup)
        pend=None
        continue
    d=re.search(r'ซ้ำกับ #(\d+)',l)
    if d: pend=int(d.group(1))
# ---- content ----
parts=re.split(r'^Part 2 — Listening\s*$',raw,flags=re.M)
items={}
def split_items(txt,ptype):
    pos=[(m.start(),int(m.group(1))) for m in re.finditer(r'^#(\d+) · ',txt,re.M)]
    for k,(s,n) in enumerate(pos):
        e=pos[k+1][0] if k+1<len(pos) else len(txt)
        items[n]=(ptype,txt[s:e])
split_items(parts[0],'Reading'); split_items(parts[1],'Listening')
TH=re.compile(r'[\u0E00-\u0E7F]')
def parse_qs(qa):
    lines=[l for l in qa.split('\n')]
    blocks=[];cur=None
    for l in lines:
        s=l.strip()
        if re.match(r'^(Question\s+\d+\b|\d+\.\s+[A-Za-z“"‘\'])',s) or re.match(r'^Q\d+[\.:]',s):
            cur=[s];blocks.append(cur)
        elif cur is not None: cur.append(s)
    out=[]
    for b in blocks:
        txt='\n'.join(b)
        # split english part / thai part
        idx=None
        for i,s in enumerate(b):
            if re.match(r'^ข้อ\s*\d+',s) or (i>0 and TH.search(s) and not re.match(r'^[A-D]\.',s) and not s.startswith('Answer')):
                idx=i;break
        en=b[:idx] if idx else b; th=b[idx:] if idx else []
        opts=[];q=[];ans=None;mode='q';mark=None
        for s in en:
            m=re.match(r'^(?:✅\s*)?Answer:?\s*(.*)$',s)
            if m: ans=m.group(1).strip();mode='a';continue
            m=re.match(r'^\(?([A-Fa-f])[\.\)]\s*(.*)$',s)
            if m and mode!='a':
                L=m.group(1).upper();t=m.group(2)
                if t.rstrip().endswith('✔'): t=t.rstrip()[:-1].rstrip(); ans=ans or 'MARK:'+L; mark=L
                opts.append([L,t]);mode='o';continue
            if mode=='a':
                if s and ans is not None: ans+=' '+s
            elif mode=='o' and s: opts[-1][1]+=' '+s
            elif s: q.append(s)
        letter=None
        ans=(ans or '').strip()
        if ans.startswith('MARK:'): ans=ans[5:]
        if ans:
            m=re.match(r'^\(?([A-Fa-f])\b',ans); m=re.match(r'^\(?([A-Fa-f])',ans) if m else None
            if m: letter=m.group(1).upper()
            else:
                for L,t in opts:
                    if t and ans.replace(' ','').startswith(t.replace(' ','')[:25]): letter=L
        ok=len(opts)>=2 and letter in [o[0] for o in opts]
        if not th: 
            thline=[]
        kind='mcq' if ok else ('open' if (ans and not opts and q) else 'raw')
        out.append(dict(kind=kind,ok=ok,q='\n'.join(q),opts=opts,ans=letter,th='\n'.join(th).strip(),ans_text=ans if kind=='open' else None,raw=txt if kind=='raw' else None))
    return out
toc.setdefault(25,dict(n=25,type='Reading',title='20_2Reading_Protecting Our Planet_The Importance of Environmental Conservation',date='2026-06-21',status='dup',dup=24))
res=[]
for n in range(1,max(toc)+1):
    t=toc.get(n,dict(n=n,type='?',title='?',date=None,status='?',dup=None))
    it=dict(n=n,type=t['type'],title=t['title'],date=t['date'],status=t['status'],dup=t['dup'])
    if n in items:
        pt,txt=items[n]; it['type']=pt
        h=txt.split('\n',1)[0]
        m=re.match(r'^#\d+ · (.*?)(?:\s*\((20\d\d-\d\d-\d\d)\))?\s*$',h)
        if m: it['title']=m.group(1)
        d=re.search(r'ไฟล์วันที่\s*(20\d\d-\d\d-\d\d)',txt)
        if d: it['date']=d.group(1)
        mm=re.search(r'^(?:คำถามและเฉลย|Questions? & Answers?).*$|^คำถามและเฉลย.*$',txt,re.M)
        if mm: body,qa=txt[:mm.start()],txt[mm.end():]
        else: body,qa=txt,''
        body=re.sub(r'^#\d+ · .*\n(ไฟล์วันที่.*\n)?','',body).strip()
        it['body']=body; it['qs']=parse_qs(qa) if qa.strip() else []; it['qa_raw']=qa.strip()
        if not it['qs']: it['no_qs']=True
    res.append(it)
json.dump(res,open('/home/claude/quiz/src/data/library.json','w'),ensure_ascii=False)
from collections import Counter
print(len(res),Counter(r['status'] for r in res),Counter((r['date'] or '')[:7] for r in res))
tot=sum(len(r.get('qs',[])) for r in res); ok=sum(q['ok'] for r in res for q in r.get('qs',[]))
print('questions',tot,'playable',ok)
print([ (r['n'],r['title']) for r in res if r['status']!='dup' and 'body' not in r])
print([ (r['n'],r['title']) for r in res if r.get('no_qs')])
