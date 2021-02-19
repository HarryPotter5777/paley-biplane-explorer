#paley biplane matrix
M = [
     [1,1,1,1,1,0,0,0,0,0,0],
     [1,1,0,0,0,1,1,1,0,0,0],
     [1,0,1,0,0,1,0,0,1,1,0],
     [1,0,0,1,0,0,1,0,1,0,1],
     [1,0,0,0,1,0,0,1,0,1,1],
     [0,1,1,0,0,0,1,0,0,1,1],
     [0,1,0,1,0,0,0,1,1,1,0],
     [0,1,0,0,1,1,0,0,1,0,1],
     [0,0,1,1,0,1,0,1,0,0,1],
     [0,0,1,0,1,0,1,1,1,0,0],
     [0,0,0,1,1,1,1,0,0,1,0]

     ]
cell_size=25
N=500
offset=(N-cell_size*11.0)/2.0
rsel=[]
csel=[]
def setup():
    size(N,N)

colclass = [0,0,1,1,1,2,2,2,3,3,3]
colors = [(255,255,255),(255,0,0),(255,255,0),(0,255,100)]
weights=[1,0.8,0.6,0.4]
def get_color(a,b):
    c=colors[a]
    w=weights[b]
    return color(int(c[0]*w),int(c[1])*w,int(c[2])*w)
def mousePressed():
    global rsel,csel,M
    i=(mouseX-offset)//cell_size
    j=(mouseY-offset)//cell_size
    if i<0 or i>=11 and (j>=0) and j<11:
        rsel.append(j)
    if j<0 or j>=11 and 0<=i<11:
        csel.append(i)
    if len(rsel)>=2:
        a,b=rsel[0],rsel[1]
        M[int(a)],M[int(b)]=M[int(b)],M[int(a)]
        rsel=[]
    if len(csel)>=2:
        a,b=csel[0],csel[1]
        for v in range(11):
            M[v][int(a)],M[v][int(b)]=M[v][int(b)],M[v][int(a)]
        csel=[]
def draw():
    background(0)
    translate(offset,offset)
    for r in rsel:
        #print(r,(r+0.3)*cell_size)
        fill(100,0,255)
        rect(-10,(r+0.3)*cell_size,11*cell_size+20,0.7*cell_size)
    for c in csel:
        #print(r,(r+0.3)*cell_size)
        fill(100,0,255)
        rect((c+0.3)*cell_size,-10,0.7*cell_size,11*cell_size+20)
    fill(255)
    rect(0,0,11*cell_size,11*cell_size)
    
    for i in range(11):
        for j in range(11):
            if M[j][i]>0:
                fill(get_color(colclass[i],colclass[j]))
                rect(i*cell_size,j*cell_size,cell_size,cell_size)

    translate(-offset,-offset)
