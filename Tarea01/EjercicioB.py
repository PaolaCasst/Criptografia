##declaramos el cuadrado de polibio
Cuadrado_Polibio = [
    ['a', 'b', 'c', 'd', 'e'],
    ['f', 'g', 'h', 'i', 'j'],
    ['k', 'l', 'm', 'n', 'o'],
    ['p', 'q', 'r', 's', 't'],
    ['u', 'v', 'w', 'x', 'y']
]

##Esto tambien se puede implementar con un diccionario, pero senti que perdía el punto de la busqueda intensiva 
def get_index(valor):
    for i, fila in enumerate(Cuadrado_Polibio, start=1):
        for j, elemento in enumerate(fila, start=1):
            if elemento == valor:
                return i, j
    return None

##aqui lo que hacemos es buscar los indices y concatenar las letras
def descifrar(list):
    resultado = ""
    for i in list:
        i = str(i)
        x,y = i[0],i[1]
        resultado += Cuadrado_Polibio[int(x)-1][int(y)-1]
    return resultado


##aqui lo que hacemos es buscar la coincidencia y concatenar los indices
def cifrar(texto):
    texto = texto.lower().replace(" ", "")
    resultado = []
    for letra in texto:
        indice = get_index(letra)
        resultado.append( str(indice[0]) + (str(indice[1])) )
    return resultado

##ejemplos de la tarea
print("El resultado de descifrar [15, 32, 45, 24, 15, 33, 41, 35, 34, 35, 15, 44, 41,15, 43, 11, 11, 34, 11,14, 24, 15] es " + descifrar([15, 32, 45, 24, 15, 33, 41, 35, 34, 35, 15, 44, 41,15, 43, 11, 11, 34, 11,14, 24, 15]))

print("\nEl resultado de descifrar \"Si la felicidad tuviera una forma tendria forma de cristal\" es " +  str(cifrar("Si la felicidad tuviera una forma tendria forma de cristal")))