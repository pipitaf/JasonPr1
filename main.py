import json
import os

# Cargar datos desde el archivo JSON
datos = json.load(open("datos.json"))

instrumentos = datos["guitarras"] + datos["bajos"]

def menu():
    input("Pulsa cualquier tecla: ")
    os.system("cls")
    print("\n--- HAI-FAI MIUSIC ------------")
    print("- GLOBAL -")
    print("1. Mostrar todos los modelos")
    print("2. Filtrar por color")
    print("- GUITARRAS -")
    print("3. Comprobar stock")
    print("4. Mostrar precio de una guitarra")
    print("- BAJOS -")
    print("5. Comprobar stock")
    print("6. Mostrar bajos con 5 cuerdas")
    print("7. Mostrar precio de un bajo")
    print("8. Salir")
    print("-------------------------------")
    return input("\nSelecciona una opción: ")

def mostrarDisponible(tipo,ciudad):
    if ciudad in ["Madrid", "Barcelona"]:
        print(f"\nModelos de {tipo} disponibles en {ciudad}:")
        for valor in datos[tipo]:
            if ciudad in valor["tiendas_disponibles"]:
                print("-", valor["modelo"])
    else:
        print(f"{ciudad} no existe")

def buscarColor(color):
    instrumentoColor = [
        instrumento["modelo"]
        for instrumento in instrumentos
        if color in instrumento["colores_disponibles"]
    ]
    
    if instrumentoColor:
        print(f"Instrumentos disponibles en {color}: {', '.join(instrumentoColor)}")
    else:
        print(f"No existen instrumentos en color {color}.")

def mostrarGlobal():
    print("\nModelos de bajo:")
    for bajo in datos["bajos"]:
        print("-", bajo["modelo"], "|", bajo["tipo_cuerpo"])
    print("\nModelos de guitarra:")
    for guitarra in datos["guitarras"]:
        print("-", guitarra["modelo"], "|", guitarra["tipo_cuerpo"])

def mostrarCuerdas():
    print("\nBajos de 5 cuerdas:")
    for bajo in datos["bajos"]:
        if bajo["cuerdas"] == 5:
            print("-", bajo["modelo"])

def comprobarPrecio(tipo, modelo):
    for valor in datos[tipo]:
        if valor["modelo"] == modelo:
            print(f"{modelo} cuesta {valor['precio']} €")
            break
    else:
        print(f"No se encontró el modelo {modelo} en {tipo}.")
            

# Menu

while True:
    opcion = menu()
    if opcion == "1": # done
        mostrarGlobal() 
    elif opcion == "2": # done
        for i in ["Sunburst", "Blanco", "Negro", "Natural", "Azul", "Rojo","Verde","Marrón","Gris"]:
            print(f"- {i}")
        buscarColor((input("\nIntroduce un color: ")))
    elif opcion == "3": # done
        mostrarDisponible("guitarras",(input("Selecciona una tienda (Barcelona - Madrid): ")))
    elif opcion == "4": # done
        comprobarPrecio("guitarras",(input("Elige un modelo: ")))
    elif opcion == "5": # done
        mostrarDisponible("bajos",(input("Selecciona una tienda (Barcelona - Madrid): ")))
    elif opcion == "6": # done
        mostrarCuerdas()
    elif opcion == "7": # done
        comprobarPrecio("bajos",(input("Elige un modelo: ")))
    elif opcion == "8": # done
        print("Saliendo...")
        break
    else:
        print("Opcion no valida.")