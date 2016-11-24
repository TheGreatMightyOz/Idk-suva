def determinant(maatriks): #Võtab faili nime
    #maatriks = get_file(maatriks)
    y1 = 0
    for a in maatriks:             #Leiab listide mõõdud
        y1+=1
        x1 = len(a)
    if x1 != y1 or x1 == 0:                    #Kontrollin, kas saab leida determinanti
        return("Ei saa leida determinanti")
    loendur1 = 0
    while loendur1 != x1:
        lahutatav_rida = maatriks[loendur1]
        loendur2 = loendur1 + 1
        while loendur2 != x1:
            rida = maatriks[loendur2]
            loendur3 = 0
            tegur =rida[loendur1]/lahutatav_rida[loendur1]
            while loendur3 != x1:
                uus = rida[loendur3] - tegur*lahutatav_rida[loendur3]
            
                maatriks[loendur2][loendur3]= uus
                loendur3 +=1
        
            loendur2 +=1
        loendur1 +=1
    loendur1 = 0
    vastus = 1
    while loendur1 != x1:
        arv = maatriks[loendur1][loendur1]
        vastus = vastus*arv
        loendur1 +=1
    return(vastus)
