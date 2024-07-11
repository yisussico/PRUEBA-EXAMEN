import random
import csv
import math

#SUELDOS BASE ANTES DE RANDOM
juan=0
maria=0
carlos=0
ana=0
pedro=0
laura=0
miguel=0
isabel=0
francisco=0
elena=0
#LISTAS
sueldos_trabajadores=[juan,maria,carlos,ana,pedro,laura,miguel,isabel,francisco,elena]
nombres_trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

def generar_sueldos():
    #ACA SE GENERAN LOS SUELDOS DE FORMA ALEATORIA
    global juan,maria,carlos,ana,pedro,laura,miguel,isabel,francisco,elena
    juan=random.randint(300000,2500000)
    maria=random.randint(300000,2500000)
    carlos=random.randint(300000,2500000)
    ana=random.randint(300000,2500000)
    pedro=random.randint(300000,2500000)
    laura=random.randint(300000,2500000)
    miguel=random.randint(300000,2500000)
    isabel=random.randint(300000,2500000)
    francisco=random.randint(300000,2500000)
    elena=random.randint(300000,2500000)
    print("Se han generado sueldos...")
    actualizar_lista()
    return juan,maria,carlos,ana,pedro,laura,miguel,isabel,francisco,elena

def actualizar_lista():
    #SE ACTUALIZA LA LISTA DE LOS SUELDO DE LOS TRABAJADORES
    global sueldos_trabajadores
    sueldos_trabajadores=[juan,maria,carlos,ana,pedro,laura,miguel,isabel,francisco,elena]

def clasificar_sueldos(nombre,sueldo):
    #ACA SE CLASIFICAN LOS SUELDOS
    if 800000 <= sueldo <=2000000:
        print("----------------------------------")
        print("Sueldo entre $800.000 y $2.000.000:")
        print("")
        print(f"{nombre}: Sueldo de ${sueldo}")
        print("----------------------------------")
    elif sueldo < 800000:
        print("----------------------------------")
        print("Sueldo menor a $800.000:")
        print("")
        print(f"{nombre}: Sueldo de ${sueldo}")
        print("----------------------------------")
    else:
        print("----------------------------------")
        print("Sueldo mayor a $2.000.000:")
        print("")
        print(f"{nombre}: Sueldo de ${sueldo}")
        print("----------------------------------")

def clasificando_sueldos():
    #ACA SE LE DA LA INSTRUCCION DE ALMACENAR LOS "NOMBRES" Y "SUELDOS" DE LAS LISTAS
    for nombre,sueldo in zip(nombres_trabajadores,sueldos_trabajadores):
        clasificar_sueldos(nombre,sueldo)

def sueldo_mas_alto():
    Max=max(sueldos_trabajadores)
    index=sueldos_trabajadores.index(Max)
    return f"El sueldo mas alto: {nombres_trabajadores[index]} con ${Max}"

def sueldo_mas_bajo():
    Min=min(sueldos_trabajadores)
    index=sueldos_trabajadores.index(Min)
    return f"El sueldo mas bajo: {nombres_trabajadores[index]} con ${Min}"

def promedio_sueldos():
    promedio=sum(sueldos_trabajadores)/len(sueldos_trabajadores)
    return f"El promedio de los sueldos es de: ${promedio:.2f}"

def media_geometrica():
    sueldo=math.prod(sueldos_trabajadores)
    media_geom=sueldo **(1/len(sueldos_trabajadores))
    return f"Cantidad geometrica de los sueldos: ${media_geom:.2f}"

def ver_estadisticas():
    #ACA LLAMA A DISTINTAS FUNCIONES PARA MOSTRAR CON UN PRINT LO QUE SE A EJECUTADO
    print(sueldo_mas_alto())
    print(sueldo_mas_bajo())
    print(promedio_sueldos())
    print(media_geometrica())

def generar_sueldo():
    #ACA SE GENERA EL ARCHIVO CSV
    reporte=[]
    for nombre,sueldo in zip(nombres_trabajadores,sueldos_trabajadores):
        descuento_afp=sueldo * 0.12
        descuento_salud=sueldo * 0.07
        sueldo_liquido=sueldo-descuento_afp-descuento_salud
        reporte.append([nombre,sueldo,descuento_afp,descuento_salud,sueldo_liquido])
    with open ("Reporte_trabajadores.csv","w",newline='')as file:
        writer=csv.writer(file)
        writer.writerow(["Nombre Trabajador","Sueldo Base","Descuento AFP","Descuento Salud","Sueldo Liquido"])
        writer.writerows(reporte)
    print("Se ha generado un reporte de sueldos...")

def menu():
    #ESTE ES EL MENU
    while True:
        print('''
1) Generar sueldos
2) Clasificar sueldos
3) Ver estadistica
4) Generar reporte
5) Salir''')
        rsp=input("Ingrese una opcion: ")
        if rsp.isdigit():
            rsp=int(rsp)
            if rsp == 1:
                generar_sueldos()
            elif rsp == 2:
                clasificando_sueldos()
            elif rsp == 3:
                ver_estadisticas()
            elif rsp == 4:
                generar_sueldo()
            elif rsp == 5:
                print("Finalizando programa...")
                print("Desarrollado por Alhvid Guzman")
                print("RUT 21.002.651-7")
                break
            else:
                print("Ingrese una opcion valida")
        else:
            print("Ingrese una opcion valida")

menu()#ESTE INICIA EL CODIGO