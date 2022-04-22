# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


""" 
#Proyect1

hrs = input("Enter Hours: ")
hra=float(hrs)
tar = input("Enter Tarifa: ")
tari=float(tar)
Pay=(hra*tari)
print("Pay: "+Pay) 
"""

"""
#Proyect2
hrs = input("Enter Hours: ")
ta = input("Enter Tasa: ")
t = float(ta)
h = float(hrs)
if h<=40:
    print(h*10.5)
elif h>40:
    print((40*t)+((h-40)*t*1.5))
"""

"""
#Proyect3
def computepay(h, r):
    if h<=40:
        return h*r
    elif h>40:
        return (40*r)+((h-40)*r*1.5)


hrs = input("Enter Hours: ")
ho=float(hrs)
tar = input("Enter Tarifa: ")
t=float(tar)
p = computepay(ho, t)
print("\nPay", p)
"""



"""
5.2 Escriba un programa que solicite repetidamente al usuario números enteros 
hasta que el usuario ingrese 'done'. Una vez que haya ingresado 'done', 
imprima el mayor y el menor de los números. Si el usuario ingresa algo que no
sea un número válido, atrápelo con un intento/excepto y emita un mensaje 
apropiado e ignore el número. Ingrese 7, 2, bob, 10 y 4 y haga coincidir el
resultado a continuación.
"""

largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        n = int(num)
    except:
        print('Invalid input')
        continue
    if largest is None or largest < n:
        largest = n
    elif smallest is None or smallest > n:
        smallest = n


print('Maximum is',largest)
print('Minimum is',smallest)