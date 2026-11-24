# Especificación del archivo principal: main.py

## 1. Nombre del archivo

main.py

## 2. ¿Para qué servirá?

Este archivo será el encargado de iniciar el programa y mostrar el menú principal. Desde aquí el usuario podrá elegir qué operación quiere realizar con las disoluciones químicas.

También se encargará de conectar las tres clases para que puedan trabajar juntas.

## 3. Funcionamiento del menú

Cuando se ejecute el programa, aparecerá un menú con las siguientes opciones:

1. Calcular el pH de un ácido fuerte.
2. Calcular el pOH de una base fuerte.
3. Calcular la concentración de iones H⁺.
4. Calcular la concentración de iones OH⁻.
5. Clasificar una disolución.
6. Consultar el historial de cálculos.
7. Salir del programa.

El usuario podrá seleccionar una opción y el programa realizará la operación correspondiente.

## 4. Funciones principales

El archivo tendrá las siguientes funciones:

| Función | ¿Qué hará? |
|---|---|
| mostrar_menu() | Mostrar las opciones disponibles. |
| solicitar_datos() | Pedir los datos necesarios para el cálculo. |
| ejecutar_opcion() | Realizar la operación seleccionada. |
| main() | Iniciar y controlar el funcionamiento del programa. |

## 5. Relación con las clases

El archivo principal utilizará las tres clases que se diseñaron anteriormente:

- Disolucion: permitirá guardar los datos de la sustancia.
- CalculadoraAcidoBase: realizará los cálculos químicos.
- Historial: guardará los resultados obtenidos.

De esta manera, el menú podrá utilizar las funciones de cada clase dependiendo de la opción seleccionada.

## 6. Elementos de programación que se utilizarán

Para desarrollar el archivo principal se utilizarán:

- Variables para guardar las opciones del usuario.
- Condiciones para seleccionar las operaciones.
- Ciclos para mantener el menú funcionando.
- Funciones para organizar el programa.
- Objetos para utilizar las tres clases.
- Validaciones para evitar entradas incorrectas.

## 7. Resultado esperado

Al ejecutar el archivo main.py, el usuario podrá ingresar al menú, seleccionar una operación, proporcionar los datos solicitados y obtener los resultados de sus cálculos.

También podrá consultar el historial de operaciones y salir del programa cuando lo desee.