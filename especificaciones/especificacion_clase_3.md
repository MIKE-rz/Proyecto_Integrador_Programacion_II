# Especificación de la clase 3: Historial

## 1. Nombre de la clase

Historial.

## 2. ¿Para qué servirá esta clase?

Esta clase servirá para guardar los cálculos que se vayan realizando en el programa. De esta manera, el usuario podrá consultar los resultados anteriores sin tener que volver a realizar las operaciones.

También permitirá mantener un registro de las sustancias que se hayan utilizado.

## 3. Atributos

Los atributos que tendrá esta clase serán:

| Atributo | Tipo de dato | ¿Para qué sirve? |
|---|---|---|
| registros | List | Guardar los cálculos realizados. |
| total_calculos | Integer | Contar cuántos cálculos se han realizado. |

## 4. Constructor (__init__)

El constructor se encargará de crear una lista vacía donde se irán guardando los resultados.

También inicializará el contador de cálculos en cero.

Se utilizará `self` para guardar estos datos dentro del objeto.

## 5. Métodos

La clase tendrá los siguientes métodos:

| Método | ¿Qué hará? |
|---|---|
| agregar_registro() | Guardar un nuevo cálculo en la lista. |
| mostrar_historial() | Mostrar los cálculos anteriores. |
| eliminar_historial() | Borrar los registros guardados. |
| contar_calculos() | Mostrar cuántos cálculos se han realizado. |

## 6. Ejemplo de uso

Si el usuario realiza un cálculo con KOH y después otro con HCl, ambos resultados podrán guardarse en el historial.

Así podrá consultar los datos y resultados de las operaciones anteriores.

## 7. Relación con las otras clases

Esta clase recibirá los resultados obtenidos por CalculadoraAcidoBase y los guardará junto con los datos de la sustancia proporcionados por Disolucion.

De esta manera, las tres clases podrán trabajar juntas dentro del programa.

## 8. Elementos de programación que se utilizarán

Para desarrollar esta clase se utilizarán:

- Clases y objetos.
- Atributos.
- Constructor `__init__`.
- `self`.
- Listas.
- Métodos.
- Ciclos para recorrer los registros.
- Condiciones para comprobar si existen datos.