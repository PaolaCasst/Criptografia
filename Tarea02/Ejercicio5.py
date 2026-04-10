import numpy as np
import matplotlib.pyplot as plt

def simular_ataque(n_elementos):
    d = 0
    probabilidades = []
    mensajes = []
    
    # Iteramos sobre d
    prob_actual = 0
    while prob_actual < 0.9999:
        d += 1
        exponente = -(d * (d - 1)) / (2 * n_elementos)
        prob_actual = 1 - np.exp(exponente)
        
        mensajes.append(d)
        probabilidades.append(prob_actual)
        
    return mensajes, probabilidades

# U n representativo 
n = 2**16 
mensajes_interceptados, prob_colision = simular_ataque(n)

# punto de inflexión y efectividad
punto_inflexion = 1.17741 * np.sqrt(n)
# cuando d alcanza el final de nuestra lista
punto_efectividad = mensajes_interceptados[-1]

plt.figure(figsize=(10, 6))
plt.plot(mensajes_interceptados, prob_colision, label='Probabilidad de Colisión', color='magenta', linewidth=2)

plt.axvline(x=punto_inflexion, color='blue', linestyle='--', label=f'Prob > 0.5 (d ≈ {int(punto_inflexion)})')
plt.axhline(y=0.5, color='gray', linestyle=':')
plt.axvline(x=punto_efectividad, color='red', linestyle='--', label=f'Efectividad ≈ 1 (d = {punto_efectividad})')

plt.title(f'Ataque de la Paradoja del Cumpleaños (n = {n})', fontsize=14)
plt.xlabel('Número de mensajes interceptados (d)', fontsize=12)
plt.ylabel('Probabilidad de colisión', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()


print(f"--- Resultados de la Simulación ---")
print(f"Espacio de búsqueda (n): {n}")
print(f"Mensajes para probabilidad > 50%: {int(punto_inflexion)}")
print(f"Mensajes para efectividad total (~100%): {punto_efectividad}")

plt.show()