# Especificación de la clase 1: Disolucion

## 1. Nombre de la clase

Disolucion.

## 2. ¿Para qué servirá esta clase?

Esta clase se encargará de guardar los datos de las sustancias que se van a utilizar en el programa. Por ejemplo, cuando el usuario quiera realizar un cálculo con KOH o HCl, aquí se guardará la información necesaria de esa disolución.

De esta manera será más fácil utilizar los mismos datos en las diferentes operaciones del programa.

## 3. Atributos

Los atributos que tendrá esta clase serán los siguientes:

| Atributo | Tipo de dato | ¿Para qué sirve? |
|---|---|---|
| nombre | String | Guardar el nombre de la sustancia. |
| formula | String | Guardar su fórmula química. |
| tipo | String | Indicar si es ácido o base. |
| concentracion | Float | Guardar la concentración molar. |
| volumen | Float | Guardar el volumen de la disolución en litros. |
| temperatura | Float | Guardar la temperatura en °C. |

## 4. Constructor (__init__)

El constructor servirá para asignar los datos cuando se cree una nueva disolución.

Se utilizará `__init__` para inicializar los atributos y `self` para guardar la información dentro de cada objeto.

## 5. Métodos

La clase tendrá los siguientes métodos:

| Método | ¿Qué hará? |
|---|---|
| mostrar_datos() | Mostrar los datos de la sustancia. |
| validar_datos() | Revisar que los datos ingresados sean correctos. |
| obtener_concentracion() | Obtener la concentración de la disolución. |
| obtener_tipo() | Indicar si la sustancia es un ácido o una base. |

## 6. Ejemplos de objetos

Algunos objetos que se podrán crear utilizando esta clase son:

- Una disolución de KOH.
- Una disolución de HCl.
- Una disolución de NaOH.

Cada uno tendrá sus propios datos, como su concentración, fórmula y tipo de sustancia.

## 7. Relación con las otras clases

Esta clase estará relacionada principalmente con CalculadoraAcidoBase, ya que le proporcionará los datos que necesita para realizar los cálculos.

También se relacionará con Historial, porque la información de las disoluciones utilizadas podrá guardarse junto con los resultados obtenidos.

## 8. Elementos de programación que se utilizarán

Para crear esta clase se utilizarán los siguientes elementos que hemos visto en Programación II:

- Clases y objetos.
- Atributos.
- Constructor `__init__`.
- `self`.
- Métodos.
- Condiciones para validar los datos.