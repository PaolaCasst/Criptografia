from collections import Counter
abc=list("abcdefghijklmnñopqrstuvwxyz")

##diccionario para la posiciónde la letra en el alfabeto
indice_a_letra = {i:letra for i,letra in enumerate(abc)}
letra_a_indice = {letra:i for i,letra in enumerate(abc)}

##esto realmente hace todo, los demas son wrappers
def descifrado_cesar(texto, desplazamiento):
    resultado = ""
    for i in range(len(texto)):
        letra_texto =texto[i]
        if(letra_texto == " "):
            resultado += " "
        else:
            indice_letra= letra_a_indice[letra_texto]

            letra_descifrado= (indice_letra - desplazamiento) % 27
            resultado += indice_a_letra[letra_descifrado]
    return resultado

def cesar_fuerza_bruta(texto):
    for i in range(1,27):
        print(descifrado_cesar(texto,i))

def cesar_conocimiento_adicional(texto, letracif, letradescif):
    i = (letra_a_indice[letracif] - letra_a_indice[letradescif] ) % 27
    return descifrado_cesar(texto,i)

def cesar_frecuencias(texto):
    c = Counter(texto.replace(" ", ""))
    frecuencias = dict(c)
    masrepetida= max(frecuencias, key=frecuencias.get)
    descifrado = cesar_conocimiento_adicional(texto,masrepetida,'e')
    resultado = ""
    aux = 0
    for i in range(len(texto)):
        if texto[i] == " ":
            resultado += " "
        resultado += descifrado[aux]
        aux += 1
    return  resultado

##ejemplos de la tarea
print("Resolviendo con fuerza bruta para nc xkfc gu dgnnc es igual a ")
cesar_fuerza_bruta("dqiqobtvtvshz")

print("\nResolviendo con conocimiento adicional para Zo qgweidugotío sh jb hsqgsid es igual a " + cesar_conocimiento_adicional("zo qgweidugotio sh jb hsqgsid",'d','o'))

print("\nResolviendo con análisis de frenciencias para Jx qzd kfhnp mjwnw f ptx ijqfx xnr ifwxj hzjryf xtgwj ytit hzfrit jwjx  ñtajr hsqgsid es igual a " + cesar_frecuencias("jx qzd kfhnp mjwnw f ptx ijqfx xnr ifwxj hzjryf xtgwj ytit hzfrit jwjx  ñtajr"))