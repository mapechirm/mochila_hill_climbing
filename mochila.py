import numpy as np
import copy

peso_mochila = int(input("Ingrese el peso de la mochila: "))

class Item:
    def __init__(self, valor, peso, nombre, estado) -> None:
        self.valor = valor
        self.peso = peso
        self.nombre = nombre
        self.estado = estado


def ingresar_item(items, item):
    peso = calc_peso(items)

    if (peso_mochila < peso + item.peso):
        return True
    
    return False

def calc_peso(items) :
    peso = 0
    for item in items:
        if (item.estado == True):
            peso = peso + item.peso

    return peso


def llenar_mochila(mochila) :
    local_mochila = copy.deepcopy(mochila)
    while (calc_peso(local_mochila) < peso_mochila):
        pos = int(np.random.uniform(0,len(local_mochila)))
        if (local_mochila[pos].estado == False):
            if (calc_peso(local_mochila) + local_mochila[pos].peso <= peso_mochila):
                local_mochila[pos].estado = True
            else:
                break

    return local_mochila


def imprimir_mochila(mochila) :
    for x in mochila:
        print("Nombre: ", x.nombre, ";Estado: ", x.estado,";Peso: ", x.peso,";Valor: ", x.valor, "\n")

def calc_valor(items):
    valor = 0
    for item in items:
        if (item.estado == True):
            valor = valor + item.valor

    return valor

def main() :
    global peso_mochila

    mochila = [
        Item(4,1,"Telefono",False),
        Item(2,2,"Tableta",False),
        Item(5,4,"Computadora",False),
        Item(1,1,"Manga",False),
        Item(1,1,"Estuchera",False),
        Item(2,2,"Botella",False),
    ]

    while(peso_mochila > sum(x.peso for x in mochila)):
        peso_mochila = int(input("Ingrese un peso valido para la mochila: "))


    saltos = int(input("Ingrese el numero de saltos: "))
    sol = llenar_mochila(mochila)

    for i in range(saltos):
        vecino = llenar_mochila(mochila)

        valor_vecino = calc_valor(vecino) 
        valor_sol = calc_valor(sol) 
        peso_vecino = calc_peso(vecino)

        if (valor_vecino > valor_sol and peso_vecino <= peso_mochila):
            print("Se modifico la anterior mochila con peso ", calc_peso(sol), " y valor ", valor_sol, " para la nueva mochila con peso ", peso_vecino, " y valor ", valor_vecino)

            sol = vecino
        
    print("\nMochila solucion: \n")

    print("Peso total: ", calc_peso(sol))
    print("Valor total: ", calc_valor(sol), "\n")
    
    imprimir_mochila(sol)

    return sol

main()

