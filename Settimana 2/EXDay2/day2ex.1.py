"""
stringa = str(input('Inserisci una stringa:')).upper()
new_stringa = stringa.replace('A','a').replace('E','e').replace('I','i').replace('O','o').replace('U','U')
print(new_stringa)
"""

stringa = str(input('Inserisci una stringa:'))
N = len(stringa)
new_frase = ''
i = 0
while i != N:
    carattere = stringa[i]
    if carattere == 'a' or carattere == 'e' or carattere == 'i' or carattere == 'o' or carattere == 'u':
        carattere = carattere.lower()
    else:
        carattere = carattere.upper()
    i = i + 1
    new_frase = new_frase + carattere
print(new_frase)


