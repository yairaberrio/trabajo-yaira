

def calcular_costo_llamada(destino, minutos):
    """Calcula el costo de una llamada internacional.

    Args:
        destino (str): El país donde se realiza la llamada.
        minutos (int): La duración de la llamada en minutos.

    Returns:
        float: El costo de la llamada.
    """
    tarifas_base = {
        "estados unidos": 900,
        "canadá": 800,
        "europa": 950,
        "resto del mundo": 1250,
    }
    tarifa = tarifas_base.get(destino.lower(), 1250)
    costo = tarifa * minutos
    if minutos > 15:
        costo *= 0.8
    return costo

# Ejemplo de uso
destino = "europa"
minutos = 20
costo = calcular_costo_llamada(destino, minutos)
print(f"El costo de la llamada a {destino} es {costo:.2f} pesos.")