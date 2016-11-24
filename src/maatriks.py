import fileinput
import korrutis
import determinant
import inverse

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
            print(determinant.determinant(maatrixid[len(maatrixid)-1]))
        except IndexError:
            print("Peab leiduma maatriks millest determinanti võtta")
    elif a in {"korrutis","korruta","kor"}:
        try:
            print(korrutis.korrutis(maatrixid[0],maatrixid[1]))
        except IndexError:
            print("Peab olema kaks maatriksit mida korrutada.")
    elif a in {"pöördmaatriks", "inverse", "inv"}:
        print("Siin me näeme")
    elif a in {"sin"}:
        print("")
    elif a in {"file"}:
        while(True):
            fileName=input("Sisesta faili nimi\n>")
            f=fileinput.get_file(fileName)
            if(f!=None):
                maatrixid.append(f)
                break
