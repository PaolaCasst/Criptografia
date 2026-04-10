def generar_matriz(clave):
    clave = clave.upper().replace("J", "I")
    alfabeto = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matriz = []
    usadas = set()
    
    for letra in clave:
        if letra not in usadas and letra in alfabeto:
            matriz.append(letra)
            usadas.add(letra)
    for letra in alfabeto:
        if letra not in usadas:
            matriz.append(letra)
            usadas.add(letra)
    return [matriz[i:i+5] for i in range(0, 25, 5)]

def buscar_posicion(matriz, letra):
    for r in range(5):
        for c in range(5):
            if matriz[r][c] == letra:
                return r, c
    return None

def descifrar_playfair(texto, clave):
    matriz = generar_matriz(clave)
    texto = texto.upper().replace("-", "").replace("\n", "").replace(" ", "")
    plano = ""
    
    for i in range(0, len(texto), 2):
        a, b = texto[i], texto[i+1]
        r1, c1 = buscar_posicion(matriz, a)
        r2, c2 = buscar_posicion(matriz, b)
        
        if r1 == r2: # Misma fila
            plano += matriz[r1][(c1-1)%5] + matriz[r2][(c2-1)%5]
        elif c1 == c2: # Misma columna
            plano += matriz[(r1-1)%5][c1] + matriz[(r2-1)%5][c2]
        else: # Rectangulo
            plano += matriz[r1][c2] + matriz[r2][c1]
            
    return plano

# el problema
cripto = """SHPETXSQZNSPLBMBWFFKCEBRBQMVQSEGOLRBLGXPPSUXHWLGXPDLSZSNAZINELFTEQRGTSRIFWKBRGZVNPWKBQPGPBMZOMGEQMXPHGUFDIKBSCMGQMSHVZXTQMFXFOGPSHBWIOSNOQNPWKKCOQMFAVSHSMFOSNDKHGMVSZSHQPIYSQAVPNEGCERZQBQOKSSCOFOHPYQSBKQOZSHPFKEGKCRLSNQOIKOQOWPSTDPSBRAVGMVZQZKGFRZVVPZVSHPGVAOHRBGEZVEQHGWMKSNSZSRZPHZVPSZSIRDLSNAZINDLOBFWSKGPZSMZQZOWMCAVSHGRMPXGNSPGFPKFHBMGSQSGPEKGQSFSSNOWBLPYSQKBSQBRQSEFSGKSKSUXHWLGXPZSZSNSZKRGFZQPOQDYSXTFRZQMPQRGXECNZPCEGLBQNQPCMESNOWBLPYSCGSOHQPFSRIFWKBQBDTQOQNDOZVMIZPUFDIKBSCNGRYCYBLQGBQOQZAMRZPBRPESNGRQEPE SNVPVZBKZVVPPSKSSPQBKGBKQOBKWHKDZVYMMGMQZLKEIOEQGLBRWHUXFOSPZSGPGFQOGKAV"""

clave_k = "pegasuz"
mensaje_final = descifrar_playfair(cripto, clave_k)
print(mensaje_final)