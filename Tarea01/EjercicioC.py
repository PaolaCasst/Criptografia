##texto cifrado de ejemplo
texto_cifrado = "ECISCRVSWVLGDDWUEFHFNGESXUVTICOKQOTAJPHWAKFBNAEUONOJFHONCPHRZNSCOKEWLSUFPFEEUWOMHPQFAEEDOLDBQROKFZLNQBSXVMFZZNMQQSACESDDVMONHBROUEBGMOCVISLZAOXDGTJDAQVZLDRTOVAKDDWOKJTFEJBBFNHBGLCRJRLSKVEVUDBXOPVDVZADBGSLCPOKUWSSJCRQWCOLFOKUC"

##funcion para encontrar secuencias repetidas
def buscar_repeticiones(texto, longitud=3):
    secuencias = {}

    for i in range(len(texto) - longitud + 1):
        subcadena = texto[i:i+longitud]

        if subcadena in secuencias:
            secuencias[subcadena].append(i)
        else:
            secuencias[subcadena] = [i]

    ##solo nos quedamos con las que aparecen mas de una vez
    repetidas = {}
    for clave, posiciones in secuencias.items():
        if len(posiciones) > 1:
            repetidas[clave] = posiciones

    return repetidas


##funcion para calcular distancias entre repeticiones
def calcular_distancias(repetidas):
    distancias = []

    for secuencia in repetidas:
        posiciones = repetidas[secuencia]

        for i in range(len(posiciones)-1):
            distancia = posiciones[i+1] - posiciones[i]
            distancias.append(distancia)

    return distancias


##funcion para obtener factores de un numero
def factores(numero):
    resultado = []
    for i in range(2, numero+1):
        if numero % i == 0:
            resultado.append(i)
    return resultado


##funcion principal del test de kasiski
def test_kasiski(texto):
    texto = texto.lower().replace(" ", "")

    repeticiones = buscar_repeticiones(texto)
    print("Secuencias repetidas:", repeticiones)

    distancias = calcular_distancias(repeticiones)
    print("Distancias encontradas:", distancias)

    posibles_claves = []

    for d in distancias:
        posibles_claves.extend(factores(d))

    return quitar_repetidos(posibles_claves)

def quitar_repetidos(lista):
    resultado = []
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado

##ejemplo
resultado = test_kasiski(texto_cifrado)
resultado.sort()
print("\nPosibles longitudes de clave:", resultado)