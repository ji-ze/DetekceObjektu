from PIL import Image, ImageDraw, ImageFont

name="hand"

pim = Image.open(f'{name}.jpg')
pro = pim.load()
nw = Image.new('RGB', (pim.size[0], pim.size[1]), color = 'white') #vytvoreni noveho obrazku
new = nw.load()
ts = Image.new('RGB', (pim.size[0], pim.size[1]), color = 'white') #vytvoreni noveho obrazku
test = ts.load()

detect=[]
anything=[[0]]

for i in range(pim.size[0]-1):
    for j in range(pim.size[1]-1):
        R,G,B=pro[i,j]
        if not (R>150 and G>150 and B>150):
            pro[i,j] = (256, 0, 0)

for i in range(10, pim.size[0]-11, 20):
    for j in range(10, pim.size[1]-11, 20):
            red=0
            px=0
            for k in range(i-10, i+10):
                for l in range(j-10, j+10):
                    R,G,B=pro[k,l]
                    if(R==255):
                        red+=1
                    px+=1
            if(px!=0):
                if red/float(px)>0.95:
                    for k in range(i-10, i+10):
                        for l in range(j-10, j+10):
                            new[k,l] = (256, 0, 0)
                    detect.append((i, j))
#print(len(detect))

i=1

while len(detect) != 0:
    anything.append([detect[0]])
    detect.remove(detect[0])
    q=1
    while q == 1:
        q=0
        for (x, y) in detect:
            if (x+20, y) in anything[i]:
                anything[i].append((x, y))
                detect.remove((x, y))
                q=1
            elif (x-20, y) in anything[i]:
                anything[i].append((x, y))
                detect.remove((x, y))
                q=1
            elif (x, y+20) in anything[i]:
                anything[i].append((x, y))
                detect.remove((x, y))
                q=1
            elif (x, y-20) in anything[i]:
                anything[i].append((x, y))
                detect.remove((x, y))
                q=1
    #print(i)
    #print(detect)
    i+=1
    
j=0
for q in range(len(anything)):
    if (len(anything[j])==1):
        anything.remove(anything[j]) 
        j-=1
    j+=1

for n in range(len(anything)):
    for (i, j) in anything[n]:
        for k in range(i-10, i+10):
            for l in range(j-10, j+10):
                test[k,l] = (256-(n*50), n*50, 0)


centre=[]
for q in range(len(anything)):
    centre.append((int(sum(x for (x, y) in anything[q])/len(anything[q])), int(sum(y for (x, y) in anything[q])/len(anything[q]))))
#print(anything)


p=0
for (i, j) in centre:
    ImageDraw.Draw(ts).text((i+5, j+5), str(len(anything[p])), (0, 0, 0))
    #print(len(anything[p]))
    for k in range(i-5, i+5):
        for l in range(j-5, j+5):
            test[k,l] = (0, 0, 0)
    p+=1


ts.save(f'{name}_1.png') #ulozeni obrazku
pim.save(f'{name}_2.png') #ulozeni obrazku
nw.save(f'{name}_3.png') #ulozeni obrazku


