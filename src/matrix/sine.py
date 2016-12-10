import matrix.arithmetic
import matrix.korrutis
import matrix.inverse
import copy
def sin(maatriks, res):
    maatriks2=copy.deepcopy(maatriks)
    maatriks3=copy.deepcopy(maatriks)#maatriksi ruut
    maatriks3=matrix.korrutis.korrutis(maatriks3,maatriks3)

    
    for i in range(res):
        maatriks2=matrix.korrutis.korrutis(maatriks2,maatriks3)
        maatriks2=matrix.arithmetic.scalar_product(maatriks2,(-1)/((2*i+3)*(2*i+2)))
        maatriks=matrix.arithmetic.addition(maatriks,maatriks2)
    return maatriks

def cos(maatriks, res):
    maatriks2=copy.deepcopy(maatriks)
    
    maatriks3=copy.deepcopy(maatriks)#maatriksi ruut
    maatriks3=matrix.korrutis.korrutis(maatriks3,maatriks3)
    
    maatriks=matrix.inverse.genId(len(maatriks))
    maatriks2=matrix.inverse.genId(len(maatriks))
    for i in range(res):
        maatriks2=matrix.korrutis.korrutis(maatriks2,maatriks3)
        maatriks2=matrix.arithmetic.scalar_product(maatriks2,(-1)/((2*i+1)*(2*i+2)))
        maatriks=matrix.arithmetic.addition(maatriks,maatriks2)
    return maatriks
def test(maatriks,res):
    maatriks1=copy.deepcopy(maatriks)
    maatriks2=copy.deepcopy(maatriks)
    maatriks1=sin(maatriks1,res)
    maatriks2=cos(maatriks2,res)
    maatriks1=matrix.korrutis.korrutis(maatriks1,maatriks1)
    maatriks2=matrix.korrutis.korrutis(maatriks2,maatriks2)
    return matrix.arithmetic.addition(maatriks1,maatriks2)
