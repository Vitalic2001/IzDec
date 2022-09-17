def NumProv(n):
    temp = True
    while temp == True:
        if n.isdigit():
            return int(n)
        else:
            print('Введите адекватное число')
            n = input()

def sgit(n,y):
    otv = ''
    while n >= y:
        otv += str(n % y) + ' '
        n = n // y
    k = '10'
    otv += str(n)
    for i in "ABCDEF":
        otv = otv.replace(k, i)
        k = str(int(k)+1)
    otv = otv.replace(' ','')
    otv = otv[-1::-1]
    return otv


tt = input('В какую систему счисления будем переводить? \n')
tt = NumProv(tt)
num = input('Какое число переведем из 10-тичной системы? \n')
num = NumProv(num)
print(sgit(num,tt))