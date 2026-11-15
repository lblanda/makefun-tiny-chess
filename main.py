import json,os,urllib.request as u
E=os.environ["MAKEFUN_ENV_URL"]
V=(0,100,320,330,500,900,0)
KN=(-33,-31,-18,-14,14,18,31,33);DG=(-17,-15,15,17);ST=(-16,-1,1,16);DS=((),(),KN,DG,ST,DG+ST,DG+ST)
X=TimeoutError;M=100000
CR=[15]*128;CR[0],CR[4],CR[7],CR[112],CR[116],CR[119]=13,12,14,7,3,11
T={};N=[0];L=150000
def P(p,b):
 try:
  r=u.Request(E+p,data=json.dumps(b).encode());return json.load(u.urlopen(r))
 except Exception:return{"status":"error"}
def F(f):
 a=f.split();b=[0]*128;w=a[1]=="w"
 for r,row in enumerate(a[0].split('/')[::-1]):
  c=0
  for ch in row:
   if ch.isdigit():c+=int(ch)
   else:i="PNBRQKpnbrqk".index(ch);b[r*16+c]=(i%6+1)*(1 if i<6 else-1);c+=1
 b[120]=sum((1<<i)for i,ch in enumerate("KQkq")if ch in a[2])
 b[121]=-1 if a[3]=="-"else(ord(a[3][0])-97)+(int(a[3][1])-1)*16
 b[122]=b.index(6);b[123]=b.index(-6)
 return b,w
def K(b,s,w):
 for ds,v in(((-15,-17)if w else(15,17),1),(KN,2),(DG+ST,6)):
  for d in ds:
   t=s+d
   if not t&0x88 and b[t]==(v if w else-v):return 1
 for d in DG+ST:
  t=s+d
  while not t&0x88:
   q=b[t]
   if q:
    if(q>0)==w and abs(q)in((3,5)if d in DG else(4,5)):return 1
    break
   t+=d
 return 0
def G(b,w):
 ms=[]
 for s in range(120):
  p=b[s]
  if not p or(p>0)!=w:continue
  t=abs(p)
  if t==1:
   d=16 if w else-16;r=s>>4;pr=r==6 if w else r==1
   A=lambda x:[s|x<<7|q<<14 for q in(5,4,3,2)]if pr else[s|x<<7]
   for dd in(d-1,d,d+1):
    x=s+dd
    if x&0x88:continue
    q=b[x]
    if dd==d:
     if q:continue
     ms+=A(x)
     if(r==1 if w else r==6)and not b[s+2*d]:ms.append(s|s+2*d<<7)
    elif(q and(q>0)!=w)or x==b[121]:ms+=A(x)
  else:
   for d in DS[t]:
    x=s+d
    while not x&0x88:
     q=b[x]
     if q:
      if(q>0)!=w:ms.append(s|x<<7)
      break
     ms.append(s|x<<7)
     if t==2 or t==6:break
     x+=d
   if t==6:
    for rb,dd in(((1,2),(2,-2))if w else((4,2),(8,-2))):
     g=dd//2
     if b[120]&rb and b[s+3 if dd>0 else s-4]==(4 if w else-4)and not b[s+g]and not b[s+2*g]and(dd>0 or not b[s+3*g])and all(not K(b,s+i*g,not w)for i in(0,1,2)):ms.append(s|s+dd<<7)
 return ms
def D(b,m):
 f=m&127;t=(m>>7)&127;q=(m>>14)&7;p=b[f];c=b[t];n=b[:]
 if abs(p)==1 and t==b[121] and not c:n[t-(16 if p>0 else-16)]=0
 n[t]=p if not q else q if p>0 else-q;n[f]=0
 if abs(p)==6 and abs(t-f)==2:
  r,w_=(f+3,f+1)if t>f else(f-4,f-1);n[w_]=n[r];n[r]=0
 n[120]&=CR[f]&CR[t]
 n[121]=(f+t)//2 if abs(p)==1 and abs(t-f)==32 else-1
 if abs(p)==6:n[122 if p>0 else 123]=t
 return n
def ev(b):
 s=0
 for i in range(120):
  p=b[i]
  if p:
   t=abs(p);v=V[t];f=i&7;r=i>>4;rr=r if p>0 else 7-r;c=(3-abs(3-f))*(3-abs(3-rr))
   v+=(0,rr*10+c*3,c*5,c*4,c*2,c*2,-c*8)[t]
   s+=v if p>0 else-v
 return s
def O(b,ms,w,tt):
 def sc(m):
  f=m&127;t=(m>>7)&127;q=(m>>14)&7;s=1000000 if m==tt else 0
  v=b[t]
  if v:s+=10*V[abs(v)]
  if q:s+=900+q*10
  return s
 ms.sort(key=sc,reverse=True);return ms
def S(b,d,a,be,w):
 N[0]+=1
 if N[0]>L:raise X
 if d<=0:
  s=ev(b)if w else-ev(b)
  if s>=be:return be
  if s>a:a=s
 ms=G(b,w);tt=-1;k=None
 if d<=0:
  ic=K(b,b[122 if w else 123],not w)
  if not ic:ms=[m for m in ms if b[(m>>7)&127]or(m>>14)&7 or((m>>7)&127)==b[121] and abs(b[m&127])==1]
 else:k=(tuple(b),w);tt=T.get(k,-1)
 bs=-M-1;bm=-1;lg=0
 for m in O(b,ms,w,tt):
  n=D(b,m)
  if K(n,n[122 if w else 123],not w):continue
  lg=1
  s=-S(n,d-1,-be,-a,not w)
  if s>bs:bs=s;bm=m
  a=max(a,s)
  if a>=be:break
 if not lg:
  if d<=0:return-M if ic else a
  return-M if K(b,b[122 if w else 123],not w)else 0
 if d>0:T[k]=bm
 return a if d<=0 else bs
def H(fen):
 b,W=F(fen);N[0]=0;T.clear()
 ms=G(b,W);bm=ms[0]if ms else 0
 for d in range(1,10):
  try:S(b,d,-M,M,W)
  except X:break
  bm=T.get((tuple(b),W),bm)
 f=bm&127;t=(bm>>7)&127;q=(bm>>14)&7
 return chr(97+(f&7))+str((f>>4)+1)+chr(97+(t&7))+str((t>>4)+1)+("nbrq"[q-2]if q else"")
if __name__=="__main__":
 while True:
  g=P("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":
   h=P("/move",{"game":g["game"],"move":H(g["fen"])})
   if h["status"]=="error":h=P("/resign",{"game":g["game"]})
   g=h
  print(g['game'],g['outcome'])
