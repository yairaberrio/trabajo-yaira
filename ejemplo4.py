def calcular_promedio(notas):
    """Calcula el promedio de las notas de un estudiante.

    Args:
        notas (list): Una lista de cuatro notas de un estudiante.

    Returns:
        float: El promedio de las notas.
    """
    return sum(notas) / len(notas)

def clasificar_rendimiento(promedio):
    """Clasifica el rendimiento de un estudiante según su promedio.

    Args:
        promedio (float): El promedio de las notas de un estudiante.

    Returns:
        str: Una cadena que indica la clasificación del rendimiento del estudiante.
    """
    if promedio >= 4.0 and promedio <= 5.0:
        return "Excelente"
    elif promedio >= 3.0 and promedio < 4.0:
        return "Bien"
    elif promedio >= 0.0 and promedio < 3.0:
        return "Deficiente"
    else:
        return "Promedio inválido"

# Ejemplo de uso
notas = [4.5, 4.2, 4.8, 4.7]
promedio = calcular_promedio(notas)
rendimiento = clasificar_rendimiento(promedio)
print(f"El rendimiento del estudiante es: {rendimiento}")