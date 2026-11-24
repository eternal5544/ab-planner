import random,json,os,datetime,math
from PIL import Image,ImageDraw,ImageFilter
d=datetime.date.today().isoformat()
out=os.path.join("icons",d);os.makedirs(out,exist_ok=True)
seed=random.randrange(10**6)
def draw(S):
    rnd=random.Random(seed);k=S/512
    hue=rnd.choice([(244,63,94),(91,154,255),(61,220,138),(251,191,36),(168,85,247)])
    im=Image.new("RGB",(S,S),(11,11,13));g=ImageDraw.Draw(im)
    cx=cy=S/2
    n=rnd.choice([5,7,8,9]);rot=rnd.random()*math.tau
    for i,r in enumerate([220,170,120]):
        st=2 if n%2 else 1
        pts=[(cx+r*k*math.cos(rot+j*math.tau/n*st),cy+r*k*math.sin(rot+j*math.tau/n*st)) for j in range(n+1)]
        g.line(pts,fill=tuple(int(v*(1-.25*i)) for v in hue),width=max(2,int(10*k)))
    g.ellipse([cx-60*k,cy-60*k,cx+60*k,cy+60*k],outline=(138,21,24),width=max(2,int(14*k)))
    g.ellipse([cx-20*k,cy-20*k,cx+20*k,cy+20*k],fill=hue)
    return Image.blend(im,im.filter(ImageFilter.GaussianBlur(10*k)),.35)
for s in (180,192,512):
    im=draw(s);im.save(f"{out}/icon-{s}.png");im.save(f"icon-{s}.png")
h=json.load(open("icons/history.json")) if os.path.exists("icons/history.json") else []
h.append({"date":d,"seed":seed,"path":out});json.dump(h,open("icons/history.json","w"),indent=1)
print(out,seed)
