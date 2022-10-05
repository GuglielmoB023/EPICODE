
l_benzina = float(input('Quant\'è la capacità del serbatoio ?'))
km_l = float(input('Quanti km fai con un litro ?'))

while True:
    if km_l < 1:
       print('La capacità non può esistere')
       km_l = float(input('Quanti km fai con un litro ?'))
    break

price = float(input('Quanto costa la benzina al litro ?'))

costo_100km = (100/km_l) * price
autonomia = km_l * l_benzina

print('Il costo per 100 km è', costo_100km, 'euro')
print('La tua autonomia è di', autonomia, 'km')












