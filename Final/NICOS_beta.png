from PIL import Image, ImageDraw, ImageFont
import os
from scipy import stats

def refH():
    move(Hand1_y,-17000000)
    move(Hand1_z,-17000000)
    move(Hand2_z,-17000000)
    move(Hand3_z,-17000000)
    move(Hand4_z,-17000000)
    wait(1)
    move(StageX, -16000)
    move(StageY, -16000)
    move(StageX, 9000)
    move(StageY, 9000)
    Hand1_x.reference()
    Hand1_y.reference()
    Hand1_z.reference()
    Hand2_x.reference()
    Hand2_y.reference()
    Hand2_z.reference()
    Hand3_x.reference()
    Hand3_y.reference()
    Hand3_z.reference()
    Hand4_x.reference()
    Hand4_y.reference()
    Hand4_z.reference()

    for i in ["1_x", "1_y", "1_z", "2_x", "2_y", "2_z", "3_x", "3_y", "3_z", "4_x", "4_y", "4_z"]:
        wait(f"Hand{i}")
    
    return 0

def autoRotS():
    if os.system("/dev/video0") == 32256:
        video = 0
    elif os.system("/dev/video1") == 32256:
        video = 1


    name = "ref_rot"

    os.system(f"ffmpeg -y -f v4l2 -video_size 1920x1080 -i /dev/video{video} -vframes 1 -qscale:v 2 -update 1 /data/2023/service/data/{name}.jpg")
    os.system(f"ffmpeg -y -f v4l2 -video_size 1920x1080 -i /dev/video{video} -vframes 1 -qscale:v 2 -update 1 /data/2023/service/data/{name}.jpg")


    pim = Image.open(f'/data/2023/service/data/{name}.jpg')
    pro = pim.load()
    nw = Image.new('RGB', (pim.size[0], pim.size[1]), color = 'white') #vytvoreni noveho obrazku
    new = nw.load()
    ts = Image.new('RGB', (pim.size[0], pim.size[1]), color = 'white') #vytvoreni noveho obrazku
    test = ts.load()

    detect=[]
    anything=[[0]]

    for i in range(39-1, 1748-1):
        for j in range(4-1, 1076-1):
            R,G,B=pro[i,j]
            if (R == 0 and G > 150):
                pro[i,j] = (256, 0, 0)
            else:
                if (G>150 and G/R>1 and B/R>1):
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
                        detect.append((i, j))

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
                    new[k,l] = (256, 0, 0)

    final=[]
    for n in anything:
        for m in n:
            final.append(m)

    X = []
    Y = []
    for (x, y) in final:
        try:
            X.index(x)
        except ValueError:
            X.append(x)
            Y.append(y)
        else:
            if Y[X.index(x)] < y:
                Y[X.index(x)] = y

    X1 = []
    Y1 = []
    X2 = []
    Y2 = []

    for x in range(int(len(X)/2)):
        X1.append(X[x])
        Y1.append(Y[x])
        X2.append(X[x+int(len(X)/2)])
        Y2.append(Y[x+int(len(X)/2)])    

    a1, b1, r1, p1, std_err1 = stats.linregress(X1, Y1)
    a2, b2, r2, p2, std_err2 = stats.linregress(X2, Y2)

    if std_err1 < std_err2:
        a = a1
    else:
        a = a2
    
    print(a)

    move(StageRot, int(a/0.0228))

    nw.save(f'/data/2023/service/data/{name}_p.png') #ulozeni obrazku

    os.system(f"ffmpeg -y -f v4l2 -video_size 1920x1080 -i /dev/video{video} -vframes 1 -qscale:v 2 -update 1 /data/2023/service/data/{name}_2.jpg")
    os.system(f"ffmpeg -y -f v4l2 -video_size 1920x1080 -i /dev/video{video} -vframes 1 -qscale:v 2 -update 1 /data/2023/service/data/{name}_2.jpg")

    return a

def refS():
    maw(Hand1_y,-17000000)
    maw(Hand1_z,-17000000)
    maw(Hand2_y,-17000000)
    maw(Hand2_z,-17000000)
    maw(Hand3_y,-17000000)
    maw(Hand3_z,-17000000)
    maw(Hand4_y,-17000000)
    maw(Hand4_z,-17000000)

    for i in ["1_x", "1_y", "1_z", "2_x", "2_y", "2_z", "3_x", "3_y", "3_z", "4_x", "4_y", "4_z"]:
        wait(f"Hand{i}")
    wait(1)

    move(StageX, -18000)
    move(StageY, -18000)
    move(StageX, 8000)
    move(StageY, 6000)

    autoRotS()
    a = autoRotS()
    #print(a)    
    while abs(a) >= 0.0228:
        a = autoRotS()
    if a>(0.022/2):
        move(StageRot, 1)
    elif a<(-0.022/2):
        move(StageRot, -1)

    move(StageX, 500)
    move(StageY, 500)
    return 1

def scaning():
    a = 0
    if not begin == 1:
        refS()
    T, B, L, R = frame(a)
    a+=1
    while B == 0:
        b=0
        while L == 0:
            move(StageY, 1000)
            T, B, L, R = frame(a)
            a+=1
            b+=1
            if b>7:
                break
        move(StageX, 1000)
        T, B, L, R = frame(a)
        a+=1
        b=0
        while R == 0:
            move(StageY, -1000)
            T, B, L, R = frame(a)
            a+=1
            b+=1
            if b>7:
                break
        move(StageX, 1000)
        T, B, L, R = frame(a)
        a+=1
    else:
        if L==0:
            while L == 0:
                move(StageY, 1000)
                T, B, L, R = frame(a)
                a+=1
        elif R==0:
            while R == 0:
                move(StageY, -1000)
                T, B, L, R = frame(a)
                a+=1

    return 0

def frame(a):    
    if os.system("/dev/video0") == 32256:
        video = 0
    elif os.system("/dev/video1") == 32256:
        video = 1


    name = "test3.0"

    os.system(f"ffmpeg -y -f v4l2 -video_size 1920x1080 -i /dev/video{video} -vframes 1 -qscale:v 2 -update 1 /data/2023/service/data/scan/{str(a)}.jpg")
    os.system(f"ffmpeg -y -f v4l2 -video_size 1920x1080 -i /dev/video{video} -vframes 1 -qscale:v 2 -update 1 /data/2023/service/data/scan/{str(a)}.jpg")


    pim = Image.open(f'/data/2023/service/data/scan/{str(a)}.jpg')
    pro = pim.load()
    nw = Image.new('RGB', (pim.size[0], pim.size[1]), color = 'white') #vytvoreni noveho obrazku
    new = nw.load()


    detect=[]
    anything=[[0]]

    for i in range(39-1, 1748-1):
        for j in range(4-1, 1076-1):
            R,G,B=pro[i,j]
            if (R == 0 and G > 150):
                pro[i,j] = (256, 0, 0)
            else:
                if (G>150 and G/R>1 and B/R>1):
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
                        detect.append((i, j))


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
            if (i in range(850, 950) or j in range(475, 525)):
                for k in range(i-10, i+10):
                    for l in range(j-10, j+10):
                        new[k,l] = (256, 0, 0)

    nw.save(f'/data/2023/service/data/{name+str(a)}_p.png') #ulozeni obrazku


    final=[]
    for n in anything:
        for m in n:
            final.append(m)

    top = 0
    down = 0
    left = 0
    right = 0

    #print(final) #je treba zjistit, pro má right problem

    for (i, j) in final:
        if (i in range(850, 950)) and (j in range(4-1, int(pim.size[1]/2-100))):
            top=1
        if (i in range(850, 950)) and (j in range(int(pim.size[1]/2+100), 1076-1)):
            down=1
        if (i in range(39-1, int(pim.size[0]/2-100))) and (j in range(475, 525)):
            left=1
        if (i in range(int(pim.size[0]/2+100), 1076-1)) and (j in range(475, 525)):
            right=1
    #print(top, down, left, right)
    return top, down, left, right




print("Setting of offset")
refH()
begin = refS()
#scaning()
print("Finish a process")











