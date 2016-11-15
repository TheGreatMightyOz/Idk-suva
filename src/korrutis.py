def korrutis(maatriks1,maatriks2):    #Võtab kahe tekstifaili andmed
    maatriks1 = get_file(maatriks1)   #Lisab listi
    maatriks2 = get_file(maatriks2)
    y1 = 0
    for a in maatriks1:             #Leiab listide mõõdud
        y1+=1
        x1 = len(a)
    y2 = 0
    for a in maatriks2:
        y2 +=1
        x2 = len(a)
    if x1 != y2:                    #Kontrollin, kas liste saab korrutada
        return("Ei saa korrutada")
    vastus = []
    counter1 = 0
    for a in maatriks1:             #Võtan maatriksi ridu ükshaaval
        counter2 = 0
        rida =[]
        for c in range(len(a)):    
            counter3 = 0
            element = 0
            for b in a:
                arv1 = b
                arv2 = maatriks2[counter3][counter2]
                element +=arv1*arv2
                counter3+=1
            counter2 +=1
            rida.append(element)
        vastus.append(rida)        
        counter1+=1
    return (vastus)

