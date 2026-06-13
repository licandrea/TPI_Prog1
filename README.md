README – Sistema de Gestión de Países

Integrantes:

Andrea Barrios

Carlos Germán Zapatta

Descripción

Este proyecto consiste en un sistema de gestión de países desarrollado en Python utilizando estructuras de datos, funciones, manejo de excepciones y lectura de archivos CSV.

El sistema permite cargar información de países, realizar búsquedas, aplicar filtros, ordenar registros y obtener estadísticas generales.

Requisitos:

Python 3 instalado.
Archivo paises.csv ubicado en la misma carpeta que el programa (puede generarse mediante la opción "Crear CSV de Prueba").
Ejecución:

Guardar el archivo Python en una carpeta.
Abrir una terminal en dicha carpeta.
Ejecutar:
tpi_gestion_paises.py

Aparecerá el menú principal con todas las opciones disponibles.
Funcionalidades:

Cargar Países desde CSV
Carga los datos almacenados en el archivo paises.csv.

Mostrar Países
Muestra todos los países cargados en memoria.

Agregar País
Permite ingresar un nuevo país validando que no exista previamente.

Actualizar País
Modifica la población y superficie de un país existente.

Buscar País
Busca un país por nombre completo o parcial.

Filtrar por Continente
Muestra únicamente los países pertenecientes al continente indicado.

Filtrar por Población
Filtra países dentro de un rango de población.

Filtrar por Superficie
Filtra países dentro de un rango de superficie.

Ordenar por Nombre
Ordena alfabéticamente los países en forma ascendente o descendente.

Ordenar por Población
Ordena los países según su población.

Ordenar por Superficie
Ordena los países según su superficie.

Mostrar Estadísticas
Calcula y muestra:

País con mayor población.
País con menor población.
Promedio de población.
Promedio de superficie.
Cantidad de países por continente.
Crear CSV de Prueba
Genera automáticamente un archivo CSV con datos precargados.

Salir
Finaliza la ejecución del programa.

Ejemplos de uso:

Ejemplo 1: Agregar un país

Entrada:

Ingrese el nombre del país: Chile

Ingrese la población: 19600000

Ingrese la superficie: 756102

Ingrese el continente: América

Salida:

País agregado correctamente.

Ejemplo 2: Buscar un país

Entrada:

Ingrese el nombre o parte del nombre: arg

Salida:

Nombre Población Superficie Continente

Argentina 45376763 2780400 América

Ejemplo 3: Error de validación

Entrada:

Ingrese la población: abc

Salida:

Valor ingresado incorrecto. Intente nuevamente.

Ejemplo 4: Estadísticas

Salida:

========== ESTADÍSTICAS ==========

País con mayor población: China (1412600000)

País con menor población: Australia (25690000)

Promedio de población: 244830369.2

Promedio de superficie: 3312563.4

Cantidad de países por continente:

América: 4

Asia: 2

Europa: 2

Oceanía: 1

África: 1

Estructura de datos:

Cada país se almacena como un diccionario con los siguientes campos:

{ "nombre": "Argentina", "poblacion": 45376763, "superficie": 2780400, "continente": "América" }

Todos los países son almacenados dentro de una lista.

Manejo de errores:

El sistema incorpora manejo de excepciones mediante bloques try/except para:

Validar entradas numéricas.
Detectar archivos inexistentes.
Evitar datos inválidos en el CSV.
Impedir la carga de países duplicados.
Controlar opciones incorrectas del menú.
