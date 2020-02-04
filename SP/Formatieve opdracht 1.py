# Opg1

lengte = int(input('hoe groot? '))
lenwhile = 1

for i in range(1, lengte+1):
    print('*' * i)

for j in reversed(range(1, lengte)):
    print('*' * j)

while lenwhile <= lengte:
    print('*' * lenwhile)
    lenwhile += 1

lenwhile -= 2

while lenwhile > 0:
    print('*' * lenwhile)
    lenwhile -= 1
