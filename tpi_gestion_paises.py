import csv
import os
import subprocess

# Esta función solicita un tipo de ordenamiento válido
def pedir_tipo_orden():

    while True:

        print("\n1. Ascendente")
        print("2. Descendente")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":

            limpiar_pantalla()

            return False

        elif opcion == "2":

            limpiar_pantalla()

            return True

        else:
            print("Opción incorrecta. Debe ingresar 1 o 2.")

# Acá limpio la consola para que cada pantalla se vea ordenada
def limpiar_pantalla():
    subprocess.run("cls", shell=True)


# Esta función pausa el programa hasta que el usuario presione Enter
def pausar():
    input("\nPresione Enter para continuar...")


# Esta función muestra error técnico + mensaje de usuario
def manejar_error(error):
    print(error)
    print("Valor ingresado incorrecto. Operación cancelada.")


# Esta función fuerza a que el usuario ingrese un número entero válido
def pedir_entero_strict(prompt):

    while True:

        try:
            return int(input(prompt))

        except ValueError as error:
            print(error)
            print("Valor ingresado incorrecto. Intente nuevamente.")


# Esta función devuelve la ruta del CSV en la misma carpeta del programa
def obtener_ruta_csv():

    carpeta = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(carpeta, "paises.csv")



# FUNCIONES AUXILIARES


# Esta función valida que un texto no esté vacío
def validar_texto(texto, campo):

    if texto.strip() == "":
        raise ValueError(f"El campo {campo} no puede estar vacío.")

    return texto.strip()


# Esta función valida números enteros no negativos
def validar_entero(numero, campo):

    valor = int(numero)

    if valor < 0:
        raise ValueError(f"{campo} no puede ser negativo.")

    return valor


# En esta función logro encontrar un país dentro de la lista
def buscar_pais(paises, nombre):

    nombre = nombre.strip().lower()

    for pais in paises:

        if pais["nombre"].lower() == nombre:
            return pais

    return None


# Acá muestro un país siempre con el mismo formato
def mostrar_pais(pais):

    print(
        f"{pais['nombre']:<15}"
        f"{pais['poblacion']:<15}"
        f"{pais['superficie']:<15}"
        f"{pais['continente']:<15}"
    )


# Acá se muestra el contenido completo de la lista
def mostrar_paises(lista):

    if len(lista) == 0:
        print("\nNo hay países para mostrar.")
        return

    print()

    print(
        f"{'Nombre':<15}"
        f"{'Población':<15}"
        f"{'Superficie':<15}"
        f"{'Continente':<15}"
    )

    print()

    for pais in lista:
        mostrar_pais(pais)


# CSV


# Esta opción permite crear un archivo CSV de prueba
def crear_csv_prueba():

    datos = [
        ["Argentina", 45376763, 2780400, "América"],
        ["Brasil", 213993437, 8515767, "América"],
        ["Japón", 125800000, 377975, "Asia"],
        ["Alemania", 83149300, 357022, "Europa"],
        ["Canadá", 38008005, 9984670, "América"],
        ["China", 1412600000, 9596961, "Asia"],
        ["España", 47431256, 505990, "Europa"],
        ["Australia", 25690000, 7692024, "Oceanía"],
        ["Egipto", 109262178, 1002450, "África"],
        ["México", 128932753, 1964375, "América"]
    ]

    ruta = obtener_ruta_csv()

    try:

        with open(ruta, "w", newline="", encoding="utf-8") as archivo:

            escritor = csv.writer(archivo)

            escritor.writerow([
                "nombre",
                "poblacion",
                "superficie",
                "continente"
            ])

            escritor.writerows(datos)

        print("\nCSV de prueba creado correctamente.")

    except Exception as error:
        manejar_error(error)


# Esta opción permite cargar países desde un archivo CSV
def cargar_csv():

    paises = []

    ruta = obtener_ruta_csv()

    try:

        with open(ruta, "r", encoding="utf-8") as archivo:

            lector = csv.DictReader(archivo)

            for fila in lector:

                try:

                    pais = {
                        "nombre": validar_texto(
                            fila["nombre"],
                            "nombre"
                        ),
                        "poblacion": validar_entero(
                            fila["poblacion"],
                            "población"
                        ),
                        "superficie": validar_entero(
                            fila["superficie"],
                            "superficie"
                        ),
                        "continente": validar_texto(
                            fila["continente"],
                            "continente"
                        )
                    }

                    paises.append(pais)

                except Exception:
                    print("Registro inválido encontrado en el CSV.")

    except FileNotFoundError:
        print("\nNo se encontró el archivo CSV.")

    except Exception as error:
        manejar_error(error)

    return paises



# AGREGAR PAÍS


# En esta función se agrega un nuevo país
def agregar_pais(paises):

    try:

        nombre = validar_texto(
            input("Ingrese el nombre del país: "),
            "nombre"
        )

        if buscar_pais(paises, nombre) is not None:
            raise ValueError("El país ya existe.")

        while True:

            poblacion = pedir_entero_strict(
                "Ingrese la población: "
            )

            if poblacion >= 0:
                break

            print("La población no puede ser negativa.")

        while True:

            superficie = pedir_entero_strict(
                "Ingrese la superficie: "
            )

            if superficie >= 0:
                break

            print("La superficie no puede ser negativa.")

        continente = validar_texto(
            input("Ingrese el continente: "),
            "continente"
        )

        pais = {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }

        paises.append(pais)

        print("\nPaís agregado correctamente.")

    except ValueError as error:
        manejar_error(error)



# ACTUALIZAR DATOS


# Esta función permite actualizar los datos de un país
def actualizar_pais(paises):

    if len(paises) == 0:
        print("\nNo hay países cargados.")
        return

    nombre = input("Ingrese el país a actualizar: ")

    pais = buscar_pais(paises, nombre)

    if pais is None:
        print("\nEl país no existe.")
        return

    while True:

        nueva_poblacion = pedir_entero_strict(
            "Nueva población: "
        )

        if nueva_poblacion >= 0:
            break

        print("La población no puede ser negativa.")

    while True:

        nueva_superficie = pedir_entero_strict(
            "Nueva superficie: "
        )

        if nueva_superficie >= 0:
            break

        print("La superficie no puede ser negativa.")

    pais["poblacion"] = nueva_poblacion
    pais["superficie"] = nueva_superficie

    print("\nDatos actualizados correctamente.")
    

# BUSCAR PAÍS


# Esta función busca países por nombre o parte del nombre
def buscar_por_nombre(paises):

    if len(paises) == 0:
        print("\nNo hay países cargados.")
        return

    texto = input(
        "Ingrese el nombre o parte del nombre: "
    ).strip().lower()

    encontrados = []

    for pais in paises:

        if texto in pais["nombre"].lower():
            encontrados.append(pais)

    if len(encontrados) == 0:
        print("\nNo se encontraron resultados.")
    else:
        mostrar_paises(encontrados)



# FILTROS


# Esta función filtra países por continente
def filtrar_continente(paises):

    if len(paises) == 0:
        print("\nNo hay países cargados.")
        return

    continente = input(
        "Ingrese continente: "
    ).strip().lower()

    filtrados = []

    for pais in paises:

        if pais["continente"].lower() == continente:
            filtrados.append(pais)

    if len(filtrados) == 0:
        print("\nNo hay resultados.")
    else:
        mostrar_paises(filtrados)


# Esta función filtra países por rango de población
def filtrar_poblacion(paises):

    if len(paises) == 0:
        print("\nNo hay países cargados.")
        return

    while True:

        minimo = pedir_entero_strict(
            "Población mínima: "
        )

        if minimo >= 0:
            break

        print("La población no puede ser negativa.")

    while True:

        maximo = pedir_entero_strict(
            "Población máxima: "
        )

        if maximo >= 0:
            break

        print("La población no puede ser negativa.")

    filtrados = []

    for pais in paises:

        if minimo <= pais["poblacion"] <= maximo:
            filtrados.append(pais)

    if len(filtrados) == 0:
        print("\nNo hay resultados.")
    else:
        mostrar_paises(filtrados)


# Esta función filtra países por rango de superficie
def filtrar_superficie(paises):

    if len(paises) == 0:
        print("\nNo hay países cargados.")
        return

    while True:

        minimo = pedir_entero_strict(
            "Superficie mínima: "
        )

        if minimo >= 0:
            break

        print("La superficie no puede ser negativa.")

    while True:

        maximo = pedir_entero_strict(
            "Superficie máxima: "
        )

        if maximo >= 0:
            break

        print("La superficie no puede ser negativa.")

    filtrados = []

    for pais in paises:

        if minimo <= pais["superficie"] <= maximo:
            filtrados.append(pais)

    if len(filtrados) == 0:
        print("\nNo hay resultados.")
    else:
        mostrar_paises(filtrados)



# ORDENAMIENTOS

# Esta función ordena países por nombre
def ordenar_nombre(paises):

    if len(paises) == 0:
        print("\nNo hay países cargados.")
        return

    reverse = pedir_tipo_orden()

    ordenados = sorted(
        paises,
        key=lambda pais: pais["nombre"].lower(),
        reverse=reverse
    )

    mostrar_paises(ordenados)


# Esta función ordena países por población
def ordenar_poblacion(paises):

    if len(paises) == 0:
        print("\nNo hay países cargados.")
        return

    reverse = pedir_tipo_orden()

    ordenados = sorted(
        paises,
        key=lambda pais: pais["poblacion"],
        reverse=reverse
    )

    mostrar_paises(ordenados)


# Esta función ordena países por superficie
def ordenar_superficie(paises):

    if len(paises) == 0:
        print("\nNo hay países cargados.")
        return

    reverse = pedir_tipo_orden()

    ordenados = sorted(
        paises,
        key=lambda pais: pais["superficie"],
        reverse=reverse
    )

    mostrar_paises(ordenados)



# ESTADÍSTICAS


# Esta función calcula estadísticas generales
def mostrar_estadisticas(paises):

    if len(paises) == 0:
        print("\nNo hay países cargados.")
        return

    mayor = paises[0]
    menor = paises[0]

    total_poblacion = 0
    total_superficie = 0

    continentes = {}

    for pais in paises:

        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais

        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

        total_poblacion += pais["poblacion"]
        total_superficie += pais["superficie"]

        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    promedio_poblacion = (
        total_poblacion / len(paises)
    )

    promedio_superficie = (
        total_superficie / len(paises)
    )

    print("\n========== ESTADÍSTICAS ==========\n")

    print(
        f"País con mayor población: "
        f"{mayor['nombre']} ({mayor['poblacion']})"
    )

    print(
        f"País con menor población: "
        f"{menor['nombre']} ({menor['poblacion']})"
    )

    print(
        f"Promedio de población: "
        f"{promedio_poblacion}"
    )

    print(
        f"Promedio de superficie: "
        f"{promedio_superficie}"
    )

    print("\nCantidad de países por continente:")

    for continente in continentes:

        print(
            f"{continente}: "
            f"{continentes[continente]}"
        )



# MENÚ


# Esta función muestra el menú principal del sistema
def mostrar_menu():

    print("Sistema de Gestión de Países\n")

    print("1. Cargar Países desde CSV")
    print("2. Mostrar Países")
    print("3. Agregar País")
    print("4. Actualizar País")
    print("5. Buscar País")
    print("6. Filtrar por Continente")
    print("7. Filtrar por Población")
    print("8. Filtrar por Superficie")
    print("9. Ordenar por Nombre")
    print("10. Ordenar por Población")
    print("11. Ordenar por Superficie")
    print("12. Mostrar Estadísticas")

    print("\n----------------------------")
    print("13. Crear CSV de Prueba")
    print("----------------------------\n")

    print("14. Salir")



# PROGRAMA PRINCIPAL


paises = []

limpiar_pantalla()

while True:

    mostrar_menu()

    try:

        opcion = int(
            input("\nSeleccione una opción: ")
        )

        if opcion < 1 or opcion > 14:
            raise ValueError(
                "La opción debe estar entre 1 y 14."
            )

    except ValueError as error:

        manejar_error(error)

        pausar()
        limpiar_pantalla()

        continue

    limpiar_pantalla()

    if opcion == 1:

        paises = cargar_csv()

        if len(paises) > 0:
            print(
                "\nPaíses cargados correctamente."
            )

    elif opcion == 2:

        mostrar_paises(paises)

    elif opcion == 3:

        agregar_pais(paises)

    elif opcion == 4:

        actualizar_pais(paises)

    elif opcion == 5:

        buscar_por_nombre(paises)

    elif opcion == 6:

        filtrar_continente(paises)

    elif opcion == 7:

        filtrar_poblacion(paises)

    elif opcion == 8:

        filtrar_superficie(paises)

    elif opcion == 9:

        ordenar_nombre(paises)

    elif opcion == 10:

        ordenar_poblacion(paises)

    elif opcion == 11:

        ordenar_superficie(paises)

    elif opcion == 12:

        mostrar_estadisticas(paises)

    elif opcion == 13:

        crear_csv_prueba()

    elif opcion == 14:

        print("\nSaliendo del programa...")
        break

    pausar()
    limpiar_pantalla()
