import numpy as np
import random

# Genera el entorno del lago congelado con una semilla para reproducibilidad
def generate_frozen_lake(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    
    size = 4
    lake = np.full((size, size), 'F')  # 'F' representa suelo congelado
    
    # Definir las posiciones iniciales posibles
    start_positions = [(0, 0), (0, 3), (3, 0), (3, 3)]
    start = random.choice(start_positions)
    lake[start] = 'S'  # 'S' representa el punto de inicio
    
    # Definir la meta en la esquina opuesta
    goal = (size - 1 - start[0], size - 1 - start[1])
    lake[goal] = 'G'  # 'G' representa el punto de meta
    
    # Colocar hoyos de forma aleatoria (entre 1 y 3)
    num_holes = random.randint(1, 3)
    possible_positions = [(i, j) for i in range(size) for j in range(size) if (i, j) != start and (i, j) != goal]
    holes = random.sample(possible_positions, num_holes)
    for hole in holes:
        lake[hole] = 'H'  # 'H' representa un hoyo
    
    return lake

# Imprime la cuadrícula del lago congelado
def print_lake(lake):
    for row in lake:
        print(' '.join(row))
    print()

# Implementa el algoritmo de iteración de valores para encontrar la política óptima
def value_iteration(lake, gamma=0.9, theta=1e-6):
    size = len(lake)
    
    # Definir los estados accesibles (excluyendo los hoyos)
    states = [(i, j) for i in range(size) for j in range(size) if lake[i, j] != 'H']
    
    # Definir las acciones posibles (arriba, abajo, izquierda, derecha)
    actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Inicializar los valores de los estados y la política óptima
    V = {s: 0 for s in states}
    policy = {s: None for s in states}
    
    while True:
        delta = 0  # Diferencia máxima entre iteraciones
        new_V = V.copy()  # Crear una copia de la función de valores
        
        for s in states:
            if lake[s] == 'G':  # Si el estado es la meta, no se actualiza
                continue
            
            max_value = float('-inf')
            best_action = None
            
            for a in actions:
                # Calcular el nuevo estado después de tomar la acción
                new_s = (s[0] + a[0], s[1] + a[1])
                
                # Evitar salir de los límites del lago
                if new_s not in states:
                    new_s = s
                
                # Definir la recompensa (1 si llega a la meta, -0.1 en otro caso)
                reward = 1 if lake[new_s] == 'G' else -0.1
                value = reward + gamma * V[new_s]  # Aplicar la ecuación de Bellman
                
                # Actualizar el mejor valor y la mejor acción
                if value > max_value:
                    max_value = value
                    best_action = a
            
            new_V[s] = max_value
            policy[s] = best_action
            delta = max(delta, abs(V[s] - new_V[s]))  # Actualizar el delta
        
        V = new_V  # Actualizar la función de valores
        
        # Terminar si los valores convergen
        if delta < theta:
            break
    
    return V, policy

# Simula el movimiento del agente siguiendo la política óptima
def simulate_agent(lake, policy):
    start = np.argwhere(lake == 'S')[0]  # Encontrar la posición inicial
    goal = np.argwhere(lake == 'G')[0]  # Encontrar la posición de la meta
    state = tuple(start)  # Convertir a tupla para indexación
    path = [state]  # Registrar el camino del agente
    
    while state != tuple(goal):  # Mientras el agente no llegue a la meta
        action = policy.get(state)  # Obtener la mejor acción según la política
        
        if action is None:
            break  # Si no hay acción válida, detener la simulación
        
        # Calcular el nuevo estado después de tomar la acción
        new_state = (state[0] + action[0], state[1] + action[1])
        
        if lake[new_state] == 'H':  # Si cae en un hoyo, termina la simulación
            print("¡El agente cayó en un hoyo!")
            return path
        
        state = new_state
        path.append(state)  # Guardar el nuevo estado en el camino
    
    print("¡El agente alcanzó la meta!")
    return path

# Generar y mostrar el entorno del lago congelado
lake = generate_frozen_lake()
print_lake(lake)

# Calcular la política óptima usando iteración de valores
V, policy = value_iteration(lake)
print("Función de valores:")
for i in range(4):
    print([round(V[(i, j)], 2) if (i, j) in V else 'H' for j in range(4)])

# Simular el movimiento del agente
path = simulate_agent(lake, policy)
print("Camino del agente:", path)

# Reflexión sobre el uso de IA generativa:
# Inicialmente, el prompt era muy general y generaba respuestas ambiguas.
# Se mejoró especificando la estructura del entorno y el uso de Value Iteration.
# Esto permitió obtener un código más preciso y alineado con los requisitos de la tarea.
# La experiencia mostró que un prompt más detallado da mejores resultados.
