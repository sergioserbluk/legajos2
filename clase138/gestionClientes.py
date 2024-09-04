import colorama
def menu():
    print(colorama.Fore.CYAN + "0 para salir")
    print("1 para agregar clientes")
    print("2 para listar")
    op=input("seleccione una opcion")
    
    return op
def cargarCliente(lista):
    cliente=input("ingrese el nombre del cliente: ")
    lista.append(cliente)
    print("cliente agregado exitosamente!")
    return
def listarClientes(lista):
    print("Lista de clientes")
    for cliente in clientes:
        print(cliente)
    print("fin de la lista...")
    return
#programa principal
colorama.init(autoreset=False)
clientes=[]
while True:
    op=menu()
    if op=="0":
        break
    elif op=="1":
        cargarCliente(clientes)
        colorama.Style.RESET_ALL
    elif op=="2":
        listarClientes(clientes)
    else:
        print("opcion incorrecta!")

