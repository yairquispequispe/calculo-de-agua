def calcular_objetivo_ml(peso_kg, nivel_actividad):
    objetivo = peso_kg * 35
    
    if nivel_actividad == "bajo":
        objetivo = objetivo * 0.90  
    elif nivel_actividad == "alto":
        objetivo = objetivo * 1.10  
    
    return objetivo

def estado_hidratacion(consumo_ml, objetivo_ml):
    if consumo_ml < objetivo_ml:
        falta = ((objetivo_ml - consumo_ml) / objetivo_ml) * 100
        return (f"Te falta para llegar")
    
    elif consumo_ml == objetivo_ml:
        return ("Has alcanzado tu objetivo")
    
    else:
        sobra = ((consumo_ml - objetivo_ml) / objetivo_ml) * 100
        return (f"Has excedido tu objetivo")

personas = []

while True:
    try:
        peso = float(input("Peso en kg: "))
        if peso == 0: 
            break
            
        actividad = input("Actividad (bajo, medio, alto): ").lower()
        consumo = float(input("Agua consumida hoy (ml): "))

        obj_diario = calcular_objetivo_ml(peso, actividad)
        mensaje = estado_hidratacion(consumo, obj_diario)

        print(f"Objetivo recomendado: {obj_diario} ml")
        print(f"Actual: {mensaje}")

        persona = {
            "peso": peso,
            "nivel_actividad": actividad,
            "consumo": consumo,
            "objetivo": obj_diario
        }
        personas.append(persona)

    except ValueError:
        print("Dato no válido. Por favor, ingrese números.")
