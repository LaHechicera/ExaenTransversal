import statistics as st
import random
import csv

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

def sueldos(trabajadores):
    sueldos = {}
    for trabajador in trabajadores:
        sueldos[trabajador] = random.randint(300000, 2500000)
    return sueldos

sueldos_asignados = sueldos(trabajadores)

def clasificar(sueldos):
    bajos = {}
    medio = {}
    alto = {}
    for trabajador, sueldo in sueldos.items():
        if sueldo < 800000:
            bajos[trabajador] = sueldo
        elif 800000 <= sueldo <= 2000000:
            medio[trabajador] = sueldo
        else:
            alto[trabajador] = sueldo
    return bajos, medio, alto

def descuentos (sueldos):
    for trabajador, sueldo in sueldos.items():
        descuento_salud = sueldo * 0.07
        descuento_afp = sueldo * 0.12
        sueldo_liquido = sueldo - descuento_salud - descuento_afp
        print(f"{trabajador}: Sueldo Base: ${sueldo}, Descuento Salud: ${descuento_salud:.2f}, Descuento AFP: ${descuento_afp:.2f}, Sueldo Líquido: ${sueldo_liquido:.2f}")


print("----Sueldos Trabajadores----")
print("1. Asignar sueldos aleatorios \n2. Clasificar sueldos \n3. Ver estadisticas \n4. Reporte de sueldos \n5. Salir del programa")
op = int(input("Eliga una opcion (solo numeros): "))

if op == 1:
    for trabajador, sueldo in sueldos_asignados.items():
        print(f"{trabajador}: ${sueldo}")

elif op == 2:
    bajos, medio, alto = clasificar(sueldos_asignados)
    print("Sueldos menores a 800.000:")
    for trabajador, sueldo in bajos.items():
        print("Nombre trabajador", "Sueldo")
        print(f"{trabajador}: ${sueldo}")
    print("\nSueldos entre $800.000 y $2.000.000:")
    for trabajador, sueldo in medio.items():
        print("Nombre trabajador", "Sueldo")
        print(f"{trabajador}: ${sueldo}")
    print("\nSueldos superiores a 2.000.000:")
    for trabajador, sueldo in alto.items():
        print("Nombre trabajador", "Sueldo")
        print(f"{trabajador}: ${sueldo}")



elif op == 4:
    descuentos(sueldos_asignados)


else:
    print("Finalizando programa...\nDesarrollado por Camila González\nRUT 19.368.775-K")