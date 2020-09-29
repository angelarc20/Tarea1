#Un programa que registre clientes sin ningun limite de cantidad.

#Creo la lista 
listaRegistro = []
clientes = 1

while clientes != 0 :
    cliente = input("Nombre del cliente: ")    
    producto = input("nombre del producto: ")
    precio = float(input("precio ($0.00) : "))

    registro = dict(cliente=cliente, producto=producto, precio=precio)
    listaRegistro.append(registro)

    clientes += 1

for registro in listaRegistro:
    print(registro)




