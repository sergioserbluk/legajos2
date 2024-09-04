#script que pide los lados de un triangulo y determina si es equilatero, isosceles o escaleno
#'''
n1=int(input("ingrese el lado 1: "))
n2=int(input("ingrese el lado 2: "))
n3=int(input("ingrese el lado 3: "))
if n1==n2 and n2==n3:
    print("equilatero")
elif n1==n2 or n2==n3 or n1==n3:
    print("isosceles")
else:
    print("escaleno")
#'''
