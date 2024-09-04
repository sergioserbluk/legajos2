'''
n1=int(input("ingrese un numero: "))
n2=int(input("ingrese otro numero: "))
res=n1+n2
print("el resultado es: ", res)
print(f"el resultado es {res}")
'''
c=input("ingrese el color del semaforo ")
if c == "rojo":
    print("alto!")
elif c == "amarillo":
    print("atencion!!")
elif c=="verde":
    print("avance")
match c:
    case "rojo":
        print("alto!")
    case "amarillo":
        print("atencion!!")
    case "verde":
        print("avance")
    case _:
        print("error")