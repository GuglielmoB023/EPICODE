stringa = input("Scrivi delle parole: ") # chiedo input la stringa
stringa.lower() #c onverto le parole in minuscolo
lista_parole = stringa.split(" ")

lettere_da_cercare = "abcdefghiklmnopqrstuvxyz"

dizionario = {} # creo dizionario vuoto

for lettera in lettere_da_cercare:
    lista_parole_per_lettera= []
    for stringa in lista_parole:
        if lettera in stringa:
            lista_parole_per_lettera.append(stringa)

    tupla = tuple(lista_parole_per_lettera) # trasformo in tupla
    dizionario[lettera] = tupla # crea dizionario con chiave

print(dizionario)
