def calcular_costo_llamada(destino, minutos):
       tarifa_base = {
        "estados unidos": 900,
        "canadá": 800,
        "europa": 950,
        "resto del mundo": 1250,
    }
   def tarifa = tarifa_base.get(destino . lugar(), 1250)
    costo = tarifa * minutos
    if minutos > 15:
        costo *= 0.8
    return costo

# Ejemplo de uso
lista_llamadas = [("Estados Unidos", 10), ("Canadá", 15), ("Europa", 20)]
costo_total = calcular_costo_total_llamada(lista_llamadas)
print(f"El costo total de todas las llamadas es {costo_total:.2f} pesos.")