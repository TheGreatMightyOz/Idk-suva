import fileinput
import korrutis
import determinant
import inverse
import copy
def printm(maatriks):
    for rida in maatriks:
        for element in rida:
            print(str(element)+' ', end='')
        print('')
    print('')


#main
print("Sisesta operatsioon, mida soovid sooritada.")
print("Lisainfo saamiseks kirjuta \"help\".")
maatrixid=[]
while True:
    a=input("> ").lower()
    if a in {"exit"}:
        break
    elif a in {"help"}:
        print("No help")
    elif a in {"determinant", "det"}:
        try:
            print(determinant.determinant(copy.deepcopy(maatrixid[len(maatrixid)-1])))
        except IndexError:
            print("Peab leiduma maatriks millest determinanti võtta")
    elif a in {"korrutis","korruta","kor"}:
        try:
            print(korrutis.korrutis(copy.deepcopy(maatrixid[0]),copy.deepcopy(maatrixid[1])))
        except IndexError:
            print("Peab olema kaks maatriksit mida korrutada.")
    elif a in {"pöördmaatriks", "inverse", "inv"}:
        printm(inverse.inverse(maatrixid[len(maatrixid)-1]))
    elif a in {"sin"}:
        print("")
    elif a in {"file"}:
        while(True):
            #dev-test
            f=fileinput.get_file("C.txt")
            if(f!=None):
                maatrixid.append(f)
                break
            #dev-test end
            fileName=input("Sisesta faili nimi\n>")
            f=fileinput.get_file(fileName)
            if(f!=None):
                maatrixid.append(f)
                break
    elif a in {"print"}:
        printm(maatrixid[len(maatrixid)-1])
