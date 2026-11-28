# เพิ่มเรื่องใหม่ (นอกไฟล์ใหญ่) เข้า library.json — ใช้เฉพาะข้อความจาก PDF ต้นฉบับ
import re, json, subprocess, glob, os
D=os.path.dirname(os.path.abspath(__file__))
LIB=os.path.join(D,'..','src','data','library.json')
TH=re.compile(r'[\u0E00-\u0E7F]')
def pages(f):
    return subprocess.run(['pdftotext',os.path.join(D,'source',f),'-'],capture_output=True,text=True).stdout.split('\f')
def eng_lines(page):
    out=[]
    for l in page.split('\n'):
        l=l.strip()
        if TH.search(l): break
        if l: out.append(l)
    return out
def split_paras(text,starts):
    idx=sorted(text.index(s) for s in starts)+[len(text)]
    return [text[a:b].strip() for a,b in zip(idx,idx[1:])]
def mcq(q,opts,ans,n=None):
    return dict(kind='mcq',ok=True,q=q,opts=opts,ans=ans,th='',raw=None,ans_text=None)
def opts_from(lines):
    q=[];opts=[]
    for s in lines:
        m=re.match(r'^([A-F])\.\s*(.*)$',s)
        if m: opts.append([m.group(1),m.group(2)])
        elif opts: opts[-1][1]+=' '+s
        else: q.append(s)
    return ' '.join(q),opts
def images(prefix):
    return sorted('pages/'+os.path.basename(p) for p in glob.glob(os.path.join(D,'..','public','pages',prefix+'-*.png')))

# ---------- 1) The Story of Animation ----------
P=pages('animation.pdf')
body=' '.join(eng_lines(P[0])[1:]+eng_lines(P[1]))
paras=split_paras(body,['The first animations','In the early 1900s','For many years','In the 1990s','Today, many movies','Animation has come'])
txt='\n'.join(P[2:5])
txt=txt.split('Answer Key')[0]
key=dict(re.findall(r'^(\d+)\.\s*([A-E])\s*$',P[4].split('Answer Key')[1] if 'Answer Key' in P[4] else '',re.M))
lines=[l.strip() for l in txt.split('\n') if l.strip() and not re.match(r'^\d+$',l.strip()) and 'Reading Comprehension Questions' not in l and l.strip()!='The Story of Animation']
blocks=[];cur=None
for l in lines:
    if re.match(r'^\d+\.\s+[A-Z]',l): cur=[l];blocks.append(cur)
    elif cur is not None: cur.append(l)
qs1=[]
for b in blocks:
    n=re.match(r'^(\d+)\.',b[0]).group(1); b[0]=re.sub(r'^\d+\.\s*','',b[0])
    q,o=opts_from(b); qs1.append(mcq(f'{n}. {q}',o,key[n]))
item1=dict(n=157,type='Reading',title='TOEFL The Story of Animation',date='2026-11-28',status='ok',dup=None,added=True,
  body='\n\n'.join(paras),qs=qs1,qa_raw='',images=images('animation'),thai_images=True)

# ---------- 2) The Hidden Work of Urban Trees ----------
T=pages('trees.pdf')
parts=[]
for pg in T[:7]:
    L=eng_lines(pg[pg.index('Paragraph'):])
    L=[l for l in L if not re.match(r'^\d+$',l) and not l.startswith('Reading ')]
    h=L[0]; parts.append(h+'\n'+' '.join(L[1:]))
body2='\n\n'.join(parts)
qtxt='\n'.join(T[7:12])
chunks=re.split(r'^Question\s+(\d+)(?:\s*—\s*[^\n]*)?\s*$',qtxt,flags=re.M)
qs2=[]
for i in range(1,len(chunks),2):
    n=chunks[i]; b=[l.strip() for l in chunks[i+1].split('\n') if l.strip() and not re.match(r'^\d+$',l.strip())]
    ai=next(k for k,l in enumerate(b) if l.startswith('ตอบ'))
    letter=re.match(r'^ตอบ\s*([A-E])\.',b[ai]).group(1)
    q,o=opts_from(b[:ai]); qs2.append(mcq(f'{n}. {q}',o,letter))
dd=[l.strip() for l in '\n'.join(T[12:14]).split('\n') if l.strip() and not TH.search(l) and not re.match(r'^\d+$',l.strip())]
qs2.append(dict(kind='raw',ok=False,q='',opts=[],ans=None,th='',ans_text=None,raw='Question 11 (Drag & Drop) — ข้อความต้นฉบับ\n'+'\n'.join(dd)+'\n\n(คำแปลไทยของข้อนี้ดูจากภาพต้นฉบับด้านล่าง)'))
item2=dict(n=158,type='Reading',title='The Hidden Work of Urban Trees',date='2026-11-28',status='ok',dup=None,added=True,
  body=body2,qs=qs2,qa_raw='',images=images('trees'),thai_images=True)

lib=[r for r in json.load(open(LIB)) if r['n']<157]+[item1,item2]
json.dump(lib,open(LIB,'w'),ensure_ascii=False)
print('added',[(i['n'],len(i['qs']),len(i['body'])) for i in (item1,item2)])
for i in (item1,item2):
    for q in i['qs'][:2]: print(q['kind'],q['q'][:80],q['opts'][:2],q['ans'])
print(item1['body'][:200]); print(item2['body'][:200])
