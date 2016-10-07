import fileinput
import korrutis
import determinant
import inverse

#main
print("Sisesta operatsioon, mida soovid sooritada.")
print("Lisainfo saamiseks kirjuta \"help\".")
while True:
    a=input("> ").lower()
    if a in {"exit"}:
        break
    elif a in {"help"}:
        print("No help")
    elif a in {"determinant", "det"}:
        print("Denis")
    elif a in {"korrutis","korruta","kor"}:
        print("koer")
    elif a in {"pöördmaatriks", "inverse", "inv"}:
        print("Siin me näeme")
    elif a in {"sin"}:
        print("")
        
