import json
import os

def guardarDatos(dic):
    with open("legajos.json","w")as file:
        json.dump(dic,file,indent=4)
    return

def cargarEmpleado(dic):
    listhijos=[]
    print("ingreso de datos".center(50," "))
    dni=input("ingrese el dni: ")
    apellido=input("ingrese el apellido: ")
    nombre=input("ingrese el nombre: ")
    direccion=input("ingrese la direccion: ")
    anac=input("ingrese el año de nacimiento: ")
    ec=input("ingrese el estado civil casado/soltero")
    sb=input("ingrese el sueldo base: ")
    resp=input("tiene hijos? s/n: ")
    while resp=="s":
        nombreh=input("ingrese el nombre: ")
        anach=input("ingrese el año de nacimiento: ")
        estudia=input("estudia? s/n: ")
        listhijos.append({"nombre":nombreh, "anac":anac,"estudia":estudia})
        resp=input("quiere cargar otro hijo? s/n")
    dic[dni]={"nombre":nombre,"apellido":apellido,"direccion":direccion,"anac":anac,"sb":sb,"hijos":listhijos}
#prog principal
legajos={}

cargarEmpleado(legajos)
guardarDatos(legajos)
