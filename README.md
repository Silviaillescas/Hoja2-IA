# Hoja2-IA
Michelle Mejía 22596 - Silvia Illescas 22376

# Simulación de un Agente en el Entorno Frozen Lake (MDP)

## Descripción
Este programa implementa un agente que resuelve un problema simplificado del Proceso de Decisión de Markov (MDP) basado en el entorno *Frozen Lake*. Se genera una cuadrícula de 4x4 en la que el agente debe llegar a la meta evitando caer en hoyos, siguiendo una política óptima calculada mediante *Value Iteration*.

## Características
- **Ambiente 4x4** con suelo congelado, hoyos, punto inicial y meta.
- **Posición inicial aleatoria** en una de las esquinas.
- **Meta en la esquina opuesta** a la posición inicial.
- **Hoyos generados aleatoriamente** (entre 1 y 3) asegurando que no coincidan con el inicio ni la meta.
- **Cálculo de la política óptima** usando el algoritmo de *Value Iteration*.
- **Simulación del agente** siguiendo la política obtenida para alcanzar la meta.
- **Uso de semilla (*seed*)** para garantizar reproducibilidad de los resultados.

## Instalación y Ejecución
1. Asegúrese de tener Python 3 instalado.
2. Clone este repositorio o descargue el archivo `MdpFrozenLake.py`.
3. Instale las dependencias necesarias (si no están instaladas previamente):
   ```bash
   pip install numpy
   ```
4. Ejecute el programa con el siguiente comando:
   ```bash
   python MdpFrozenLake.py
   ```

## Uso
Al ejecutar el script, se generará un entorno de *Frozen Lake* aleatorio y se calculará la mejor política para que el agente llegue a la meta. La salida del programa incluirá:
- La representación de la cuadrícula con los elementos `S` (inicio), `G` (meta), `H` (hoyos) y `F` (suelo congelado).
- La función de valores obtenida mediante iteración de valores.
- La simulación del agente y su camino desde el inicio hasta la meta o la caída en un hoyo.

## Ejemplo de Salida
```
S F F F
F F H F
F F F F
H F F G

Función de valores:
[0.18, 0.31, 0.46, 0.62]
[0.31, 0.46, 0.62, 0.8]
[0.46, 0.62, 0.8, 1.0]
['H', 0.8, 1.0, 0]

¡El agente alcanzó la meta!
Camino del agente: [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (3, 3)]
```
