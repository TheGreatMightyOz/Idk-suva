import fileinput
from matrix import *
import copy
def printm(maatriks):
    for rida in maatriks:
        for element in rida:
            print(str("%.2f" % element)+' ', end='')
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
        print("Kirjuta \"file\", et lugeda maatrikist sisaldavat faili. \n" +
              "Failis on maatriksi rea elemendid eraladatud tühikuga ja \n" +
              "read eraldatud rea vahetusega (ENTER). \n" +
              "Programm sooritab operatsioone viimasena või ja eelviimasena lisatud maatriksiga \n"+
              "Võimalikud ühe maatriksi operatsioonid on: \n"+
              " 1. Determinant - \"det\" \n" +
              " 2. Pöördmaatriks - \"inv\" \n"+
              " 3. Siinus ja koosinus - \"sin\" ja \"cos\" \n" +
              "Kahte maatiksi operatsioonid:\n"+
              " 1. Korrutamine - \"kor\" ")
    elif a in {"determinant", "det"}:
        try:
            print(determinant.determinant(copy.deepcopy(maatrixid[len(maatrixid)-1])))
        except IndexError:
            print("Peab leiduma maatriks millest determinanti võtta")
    elif a in {"korrutis","korruta","kor"}:
        try:
            printm(korrutis.korrutis(copy.deepcopy(maatrixid[0]),copy.deepcopy(maatrixid[1])))
        except IndexError:
            print("Peab olema kaks maatriksit mida korrutada.")
    elif a in {"pöördmaatriks", "inverse", "inv"}:
        printm(inverse.inverse(maatrixid[len(maatrixid)-1]))
    elif a in {"sin"}:
        printm(sine.sin(maatrixid[len(maatrixid)-1],100))
    elif a in {"cos"}:
        printm(sine.cos(maatrixid[len(maatrixid)-1],100))
    elif a in {"file"}:
        while(True):
            #dev-test
            #f=fileinput.get_file("A.txt")
            #if(f!=None):
            #    maatrixid.append(f)
            #    break
            #dev-test end
            fileName=input("Sisesta faili nimi\n>")
            f=fileinput.get_file(fileName)
            if(f!=None):
                maatrixid.append(f)
                break
    elif a in {"print"}:
        printm(maatrixid[len(maatrixid)-1])
