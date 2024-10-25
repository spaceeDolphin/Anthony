"""
Dette programmet er et verktøy for planlegging ev EL-installasjoner i bolig
Det innholder nyttige kalkulatorer for estimering av nødvendig utstyr
"""

#%% Importering av pakker
import numpy as np
import math as m

#%% Definering av data

#%% Antall stikkontakter ihht bolignormen NEK 400-8-823
"""
Dette er reglene:
2 uttak per 4m2 for Oppholdsrom, Stue, Arbeidsrom, Soverom
    Samt. 6 uttak ved multimedia, hvor 2 kan være euro 
    2 uttak ved ekomuttak (siste er nytt for 2022)
2 uttak per 6m2 for gang
Kjøkken:
    1 uttak for hvert utstyr med fast plass
    2 uttak per m kjøkkenbenk
    4 uttak v/spiseplass
    2 uttak per 2m fri vegg
Bad/vaskerom:
    min. 2 uttak
    Uttak til fast utstyr
Garasje/bod:
    min. 2 uttak
Ute:
    2 uttak på balkong eller altan
"""

houseDef = True

def house():
    print("Definer husets spesifikasjoner")
    print("Dette er rom å velge mellom:")
    print("Oppholdsrom, Stue, Soverom, Kjøkken, Bad, Vaskerom, Bod, Gang, Ute")
    while houseDef:
        newRoom = input("hvilket rom?")
        if newRoom == "Oppholdsrom" or newRoom == "Stue" or newRoom == "Soverom":
            