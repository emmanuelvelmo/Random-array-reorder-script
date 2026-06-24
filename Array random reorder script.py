import random # Generación de números aleatorios para reordenar elementos
import copy # Copia profunda de listas para preservar original

# VARIABLES GLOBALES
valores_iniciales = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] # Array original con valores hexadecimales

# FUNCIONES
# Mezcla elementos de forma aleatoria sin repetir
def reordenar_aleatorio(lista_original):
    # Crear copia de la lista original para no modificarla
    lista_temporal = copy.deepcopy(lista_original)
    
    # Lista para almacenar elementos reordenados
    lista_reordenada = []
    
    # Mientras haya elementos en la lista temporal
    while lista_temporal:
        # Seleccionar índice aleatorio
        indice_aleatorio = random.randint(0, len(lista_temporal) - 1)
        
        # Extraer elemento en esa posición y agregarlo a nueva lista
        elemento_seleccionado = lista_temporal.pop(indice_aleatorio)
        lista_reordenada.append(elemento_seleccionado)
    
    return lista_reordenada

# Muestra la lista como secuencia de valores separados por coma y espacio
def mostrar_lista(lista_valores):
    # Construir cadena con elementos separados por comas y espacios
    cadena_salida = ""
    
    # Recorrer elementos de la lista
    for indice, valor in enumerate(lista_valores):
        # Agregar elemento a la cadena
        cadena_salida += valor
        
        # Agregar separador si no es el último elemento
        if indice < len(lista_valores) - 1:
            cadena_salida += ", "
    
    # Mostrar secuencia formateada
    print(cadena_salida)

# PUNTO DE PARTIDA
# Generar lista reordenada aleatoriamente
lista_aleatoria = reordenar_aleatorio(valores_iniciales)

# Mostrar solo la secuencia reordenada
mostrar_lista(lista_aleatoria)

# Detener el programa
input()