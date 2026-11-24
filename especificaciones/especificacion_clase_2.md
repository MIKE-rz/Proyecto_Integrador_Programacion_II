# Especificación de la clase 2: CalculadoraAcidoBase

## 1. Nombre de la clase

CalculadoraAcidoBase.

## 2. ¿Para qué servirá esta clase?

Esta clase será la encargada de realizar las operaciones químicas del programa. Utilizará los datos de las disoluciones para calcular el pH, pOH y las concentraciones de los iones H⁺ y OH⁻.

También permitirá identificar si una disolución es ácida, básica o neutra.

## 3. Atributos

Los atributos que tendrá esta clase serán:

| Atributo | Tipo de dato | ¿Para qué sirve? |
|---|---|---|
| disolucion | Objeto | Guardar la disolución que se va a analizar. |
| resultado_ph | Float | Guardar el resultado del pH. |
| resultado_poh | Float | Guardar el resultado del pOH. |
| concentracion_h | Float | Guardar la concentración de H⁺. |
| concentracion_oh | Float | Guardar la concentración de OH⁻. |

## 4. Constructor (__init__)

El constructor permitirá recibir la información de la disolución que se quiere analizar.

También inicializará los resultados de los cálculos para poder guardar los valores que se obtengan.

Se utilizará `self` para trabajar con los atributos de cada objeto.

## 5. Métodos

La clase tendrá los siguientes métodos:

| Método | ¿Qué hará? |
|---|---|
| calcular_ph() | Calcular el pH de una disolución. |
| calcular_poh() | Calcular el pOH de una disolución. |
| calcular_concentracion_h() | Obtener la concentración de iones H⁺. |
| calcular_concentracion_oh() | Obtener la concentración de iones OH⁻. |
| clasificar_disolucion() | Indicar si la disolución es ácida, básica o neutra. |
| mostrar_resultados() | Mostrar los resultados obtenidos. |

## 6. Ejemplos de uso

Esta clase se utilizará para resolver ejercicios como el del KOH 0.0050 M que se trabajó anteriormente en Química.

También podrá utilizarse con otras sustancias, como HCl y NaOH, dependiendo de los datos que ingrese el usuario.

## 7. Relación con las otras clases

Esta clase utilizará los datos proporcionados por Disolucion para realizar las operaciones.

Después de obtener los resultados, podrá enviar la información a la clase Historial para guardar los cálculos realizados.

## 8. Elementos de programación que se utilizarán

Para desarrollar esta clase se utilizarán:

- Clases y objetos.
- Atributos y métodos.
- Constructor `__init__`.
- `self`.
- Operaciones matemáticas.
- Condiciones para realizar los cálculos.
- Validaciones de datos.