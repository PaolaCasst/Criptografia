abc = list("abcdefghijklmnopqrstuvwxyz")

claves = ["star", "pinamar", "lazy", "lagrima", "passenger", "diente"] 

texto = "eocyjicmytecplkgvecmtnfyyysftnfguurrhamlllzwtnlwmecbznsdpekjtkdntcjgygtnxyofzndqzldygezkpsryrezrehdrzndalurceocyjirupaqgxnnroohlramwehhlrileznmyvibixyecpttnehdldtzppasrseeyyttpytgcevnlehqmhmxflncgymxnlnsq"

letra_a_num = {letra: i for i, letra in enumerate(abc)}
num_a_letra = {i: letra for i, letra in enumerate(abc)}

def vigenere(tex, clave):
    resultado = ""
    tex = tex.lower()
    for i in range(len(tex)):
        letra_texto = tex[i]
        letra_clave = clave[i % len(clave)]

        num_texto = letra_a_num[letra_texto]
        num_clave = letra_a_num[letra_clave]

        num_descifrado = (num_texto - num_clave) % 26
        resultado += num_a_letra[num_descifrado]

    print(resultado+"\n")

for clave in claves:
    vigenere(texto, clave)