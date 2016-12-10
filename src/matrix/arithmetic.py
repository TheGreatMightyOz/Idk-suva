def addition(maatriks1, maatriks2):
    for i in range(len(maatriks1)):
        for j in range(len(maatriks1)):
            maatriks1[i][j]=maatriks1[i][j]+maatriks2[i][j]
    return maatriks1
def scalar_product(maatriks, scalar):
    for i in range(len(maatriks)):
        for j in range(len(maatriks)):
            maatriks[i][j]=maatriks[i][j]*scalar
    return maatriks
