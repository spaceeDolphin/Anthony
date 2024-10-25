"""
Programmet simulerer Lotto i Norsk Tipping
https://no.wikipedia.org/wiki/Lotto_(Norge)

generator() simulerer en lottotrekning, 7 tall + tilleggstall, denne må utføres først
guess() gjetter en rekke og sjekker hvor mange rette + om tilleggstallet ble gjettet
vinn() bruker guess() kontinuerlig til den oppnår det ønskede resultatet, altså antall rette
spill() utfører et spesifisert antall guess() og summerer resultatet

TODO
Utvide programmet til å bruke spill() og fordele premiepotten
"""

import random as r
import numpy as np

def generator(t_tall = False):
    lotto_tall = np.array([r.randint(1,34)])
    for n in range(7):
        while True:
            same = 0
            random_n = r.randint(1,34)
            for x in lotto_tall:
                if random_n == x:
                    same += 1
            if same == 0 and n != 6:
                lotto_tall = np.append(lotto_tall, random_n)
                break
            elif same == 0 and n == 6:
                tilleggstall = random_n
                break
            #print(random_n, "already existed")
    if t_tall:
        return lotto_tall, tilleggstall
    elif t_tall == False:
        return lotto_tall
              
def guess():
    rekke = generator()
    #print("Gjettet rekka", rekke)
    
    rett = 0
    rett_tt = 0
    
    for x in lotto_tall:
        for n in rekke:
            if x == n:
                rett += 1
                #print("Gjettet", x, "riktig")
                
    if rett == 6:
        for n in rekke:
            if n == tilleggstall:
                rett_tt = 1
                
    return rett, rett_tt

def vinn(antall_rette, tt_tall=0):
    antall_spill = 0
    
    if antall_rette > 7:
        print("Det er bare 7 tall i en Lotto rekke")
        spiller = False
        avbryt = False
    elif tt_tall != 0 and antall_rette != 6:
        print("Rett tilleggstall er kun relevant for 6 rette")
        spiller = False
        avbryt = False
    elif tt_tall > 1:
        print("Det er bare ett tilleggstall!")
        spiller = False
        avbryt = False
    else:
        spiller = True
        avbryt = True
    
    while spiller:
        guess_n = guess()
        antall_spill += 1
        if guess_n[0] >= antall_rette and guess_n[1] >= tt_tall:
            spiller = False
    
    if tt_tall == 0 and avbryt:
        print("For å få", antall_rette, "eller flere rette krevdes", antall_spill, "forsøk")
        print("I dette tilfellet ble det", guess_n[0], "rette")
    elif tt_tall == 1 and avbryt:
        print("For å få", antall_rette, "rette og tilleggstallet rett krevdes", antall_spill, "forsøk")
    elif avbryt == False:
        print("Avbryter...")
    return antall_spill

def spill(forsøk):
    fire = 0
    fem = 0
    seks = 0
    seks_p1 = 0
    syv = 0
    print(forsøk, "rekker gjettet")
    
    for f in range(forsøk):
        guess_n = guess()
        
        if guess_n[0] == 4:
            fire += 1
            print("Rekke", f+1, "fikk 4 rette!")
        elif guess_n[0] == 5:
            fem += 1
            print("Rekke", f+1, "fikk 5 rette!")
        elif guess_n[0] == 6 and guess_n[1] == 1:
            seks_p1 += 1
            print("Rekke", f+1, "fikk 6 rette i tillegg til tilleggstallet!")
        elif guess_n[0] == 6:
            seks += 1
            print("Rekke", f+1, "fikk 6 rette!")
        elif guess_n[0] == 7:
            syv += 1
            print("Rekke", f+1, "fikk alle 7 rette!")
    
    if fire + fem + seks + seks_p1 + syv == 0:
        print("...men ingen vinnere")
    if fire == 1:
        print(fire, "rekke fikk fire rette")
    elif fire > 0:
        print(fire, "rekker fikk fire rette")
    if fem == 1:
        print(fem, "rekke fikk fem rette")
    elif fem > 0:
        print(fem, "rekker fikk fem rette")
    if seks == 1:
        print(seks, "rekke fikk seks rette")
    elif seks > 0:
        print(seks, "rekker fikk seks rette")
    if seks_p1 == 1:
        print(seks_p1, "rekke fikk seks rette i tillegg til tilleggstallet")
    elif seks_p1 > 0:
        print(seks_p1, "rekker fikk seks rette i tillegg til tilleggstallet")
    if syv == 1:
        print(syv, "rekke fikk alle syv rette")
    elif syv > 0:
        print(syv, "rekker fikk alle syv rette")
        
    return fire, fem, seks, seks_p1, syv

lotto_tall, tilleggstall = generator(True)
print("Lotto rekke:", lotto_tall, "\nTilleggstall:", tilleggstall)

#guess1 = guess()
#print(guess1[0], "rette")
spill(50000)
#vinn(6)
    
        































