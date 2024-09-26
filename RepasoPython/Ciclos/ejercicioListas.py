# Una empresa llamada “Transportes Cesde” requiere guardar los nombres de los
# conductores y el dinero que recaudan cada día de la semana (lun a sábado)
# movilizando a la comunidad educativa y el porcentaje de recaudo de cada conductor.
# Para guardar esta información se crearán las siguientes listas:
# NombreConductor: para almacenar los nombres de los conductores.
# DiasSemana: que contiene los días de lunes a sábado.
# Recaudo: lista para guardar la cantidad recolectada cada día de la semana.
# Se debe generar una lista llamada total recaudo con la suma total de lo recaudado por
# cada conductor.
# Debe solicitar el número de conductores que hacen parte de la empresa de Transporte Cesde.


# Inicialización de listas
NombreConductor = []
DiasSemana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
Recaudo = []
TotalRecaudo = []

# Solicitar el número de conductores
num_conductores = int(input("Ingrese el número de conductores: "))

# Recoger la información de cada conductor
for i in range(num_conductores):
    nombre = input(f"Ingrese el nombre del conductor {i + 1}: ")
    NombreConductor.append(nombre)
    
    # Recaudar dinero por cada día de la semana
    recaudos_dia = []
    total = 0
    
    for dia in DiasSemana:
        recaudo_dia = float(input(f"Ingrese el recaudo del {dia} para {nombre}: "))
        recaudos_dia.append(recaudo_dia)
        total += recaudo_dia
    
    Recaudo.append(recaudos_dia)
    TotalRecaudo.append(total)

# Mostrar resultados
print("\nResultados:")
for i in range(num_conductores):
    print(f"Conductor: {NombreConductor[i]}")
    print(f"Recaudos por día: {Recaudo[i]}")
    print(f"Total recaudado: {TotalRecaudo[i]}\n")
