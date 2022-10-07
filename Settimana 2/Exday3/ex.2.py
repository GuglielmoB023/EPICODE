importi = []
clienti = []

while True:
    nome = input("Inserire nome cliente: ")
    importo = float(input("Inserire importo: "))
    if importo == 0:
        break
    if nome in clienti:
        posizione = 0
        for n in clienti:
            if n == nome:
                break
            posizione = posizione + 1
        #Aggiorno l'importo del cliente
        importi[posizione] = importi[posizione] + importo
    else:
        # Nuovo cliente non presente nella lista clienti
        clienti.append(nome)
        importi.append(importo)

# calcolo del cliente con spesa massima
massimo = max(importi)
posizione_max = 0
for i in importi:
    if i == massimo:
        break
    posizione_max = posizione_max + 1

# calcolo del cliente con spesa minima
minimo = min(importi)
posizione_min = 0
for i in importi:
    if i == minimo:
        break
    posizione_min = posizione_min + 1

# calcolo media spesa
somma = sum(importi)
media = somma/len(importi)

# calcolo mediana spesa
importi_ordinati = importi.sort()
posizione_med = len(importi) // 2
mediana = importi[posizione_med]

print("Il cliente che ha speso di piu é:", clienti[posizione_max], "e il cliente che ha speso di meno è:", clienti[posizione_min])
print("Importo cliente spesa massima è: ", importi[posizione_max], "e l'mporto cliente spesa minima è:", clienti[posizione_min])
print("La media della spesa dei clienti è:", media, "e la mediana è invece:", mediana)
