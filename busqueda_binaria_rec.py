def busqueda_binaria(arreglo, valor, inicio, final):
    mitad = (inicio + final)//2
    if arreglo[mitad] == valor:
        return mitad
    elif inicio == final:
        return -1
    if arreglo[mitad] < valor:
        return busqueda_binaria(arreglo, valor, mitad + 1 , final)
    else:
        return busqueda_binaria(arreglo, valor, inicio, mitad - 1)
