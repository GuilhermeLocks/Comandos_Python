import random
import time
n1 = int(input('Em que numero eu pensei? '))
n2 = random.randint(0, 5)
print(n1, n2)
if n1 == n2:
    print('procesando')
    time.sleep(5)
    print('acertou')
if n1 != n2:
    print('procesando')
    time.sleep(5)
    print('acertou')