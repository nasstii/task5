#дополнительное задание. Нечётные числа - увеличить на 5, четные - занулить.
N=int(input('Введите желаемый размер массива - '))
A=[0]*N
from random import randint
for i in range(N):
    A[i]=randint(1,100)
print(A,'- исходный массив', sep=' ')
for i in range(N):
    if A[i]%2==0:
        A[i]=A[i]+5
    else:
        A[i]=0
print(A, '- массив с изменёнными значениями', sep=' ')