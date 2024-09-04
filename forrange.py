clientes=[]
for c in range(3):
    nombre=input("ingrese su nombre: ")
    apellido=input("ingrese el aplellido: ")
    celec=input("ingrese el correo electronico: ")
    domicilio=input("ingrese el domicilio: ")
    clientes.append({
        "nombre":nombre,
        "apellido":apellido,
        "correo":celec,
        "domicilio":domicilio
    })
for cliente in clientes:
    print(f"nombre:{cliente["nombre"]} apellido:{cliente["apellido"]}correo electronico:{cliente["correo"]} direccion:{cliente["direccion"]}")

