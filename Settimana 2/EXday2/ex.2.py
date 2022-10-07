#OPZIONE 1

import random
x = 0
y = 0
num = 0
while num < 100:
    x = x + random.randint(-10,10)
    y = y + random.randint(-10,10)
    num = num + 1
print('Le coordinate finali sono', '(', x,',',y,')')

