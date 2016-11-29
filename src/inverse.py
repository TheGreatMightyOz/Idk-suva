
import determinant
import copy
def printm(maatriks):
    for rida in maatriks:
        for element in rida:
            print(str(element)+' ', end='')
        print('')
    print('')

def genId(size):
    return[[min(1,abs(min(1,abs(x-y))-1)) for x in range(size)] for y in range(size)] 
                

def addLineY(maatriks, y1, y2, multiplier):
    for i in range(len(maatriks[y1])):
        #print(str(maatriks[y2][i])+' - '+str(maatriks[y1][i])+'*'+str(multiplier))
        maatriks[y2][i]=maatriks[y2][i]-maatriks[y1][i]*multiplier
    #return maatriks
def multiplyLine(maatriks,y,multiplier):
    for i in range(len(maatriks[y])):
        maatriks[y][i]=maatriks[y][i]*multiplier
def inverse(maatriks):
    d=determinant.determinant(copy.deepcopy(maatriks))
    if type(d)is int == False or d==0:
        return "Maatriksist ei saa pöördmaatriksit võtta"
    height=len(maatriks)
    width=len(maatriks[0]) #Kogemata kirjutasin topelt.
    id_maatriks=genId(height)
    #printm(maatriks)
    for x in range(width):
        for y in range(height):
            if(x==y):
                continue
            #print('y: '+str(y+1)+' x: '+str(x+1))
            #print(maatriks[y][x]/maatriks[x][x])
            addLineY(id_maatriks,x,y,maatriks[y][x]/maatriks[x][x])
            addLineY(maatriks,x,y,maatriks[y][x]/maatriks[x][x])
            #printm(id_maatriks)
    for x in range(width):
        multiplyLine(id_maatriks,x,1/maatriks[x][x])
        multiplyLine(maatriks,x,1/maatriks[x][x])
        #printm(id_maatriks)
    return id_maatriks
