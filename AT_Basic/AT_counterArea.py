#FLM: AT Counter area
import math, numpy as np
from robofab.world import CurrentFont,CurrentGlyph

def polygonArea(x,y):
  ind_arr = np.arange(len(x))-1  # for indexing convenience
  s = 0
  for ii in ind_arr:
    s = s + (x[ii]*y[ii+1] - x[ii+1]*y[ii])

  return abs(s)*0.5

def contornoArea(c):
    arrayx=[]
    arrayy=[]
    for n in c.points:
            arrayx.append(n.x)
            arrayy.append(n.y)
    return polygonArea(arrayx,arrayy)

def areaGlifo(glyph):
    positiveArea=0
    negativeArea=0
    for c in glyph:
        if c.clockwise==False:
            positiveArea=positiveArea+contornoArea(c)
        if c.clockwise==True:
            negativeArea=negativeArea+contornoArea(c)
    area = positiveArea-negativeArea
    return math.floor(area/1000)

def extremePoints(glyph):
    xval=[]
    yval=[]
    for c in glyph:
        if c.clockwise==False:
            for n in c.points:
                xval.append(n.x)
                yval.append(n.y)
            totalpoints=len(c.points)
            xval.sort()
            yval.sort()
            xvalmin=xval[0]
            xvalmax=xval[totalpoints-1]
            yvalmin=yval[0]
            yvalmax=yval[totalpoints-1]
            box=[(xvalmin,yvalmin),(xvalmin,yvalmax),(xvalmax,yvalmax),(xvalmax,yvalmin)]
            return box

def getBoxArea(g):
    puntos=extremePoints(g)
    arrayx=[]
    arrayy=[]
    for n in puntos:
        arrayx.append(n[0])
        arrayy.append(n[1])
    return math.floor(polygonArea(arrayx,arrayy)/1000)
#area individual
#print "Area de " + glyph.name +" = " + str(areaGlifo(glyph))
#glyph = CurrentGlyph()


glifosPeso=[]

def getAreas(g):

    glifosPeso.append([g.name,areaGlifo(g)])

    blockHeight=font.info.ascender
    block=(blockHeight*g.width)/1000

    area=areaGlifo(g)
    leftArea=(blockHeight*g.leftMargin)/1000
    box=getBoxArea(g)
    counter=box-area
    #print g.name + " = tA=" + str(block) + " bA=" + str(box) + " gA=" + str(area) + " cA=" + str(block-area)+ " gcA=" + str(counter)
    print "Area total: " + str(block)
    print "Area box: " + str(box)
    print "Forma: " + str(area)
    print "Contraforma: " + str(counter)
    print "Relacion Contra/Forma: " + str((box-area)/area)
    print "Area espaciado estimada = " + str(leftArea*2)
    #print "cA/gA = " + str((block-area)/area)
    #print "leftArea = " + str(leftArea)
    g.mark=100

def getSelected(g):
    for c in g:
        myPointsX=[]
        myPointsY=[]
        #217,483
        for n in c.points:
            myPointsX.append(n.x)
            myPointsY.append(n.y)
        if len(myPointsX)>1:
            print math.floor(polygonArea(myPointsX,myPointsY)/1000)

font = CurrentFont()
actualGlyph=font[fl.iglyph]

for g in font:
    #print "Area de " + g.name +" = " + str(areaGlifo(g))
    if g.selected and len(g)>0:
        getSelected(g)

getSelected(actualGlyph)
#print "Promedio `de area por glifo: "+str(promedioPeso)
