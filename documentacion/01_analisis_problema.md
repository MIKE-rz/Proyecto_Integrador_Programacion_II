# Análisis del problema
## Sistema de cálculo de ácidos y bases fuertes

### 1. Nombre del problema y asignatura

**Nombre del problema:** Cálculo de pH y pOH de ácidos y bases fuertes.

**Materia:** Química General Aplicada.

**Proyecto:** Programación II.

### 2. Descripción y justificación del problema

El problema que elegí consiste en realizar cálculos relacionados con ácidos y bases fuertes, un tema que hemos trabajado en la materia de Química. En estos ejercicios se utilizan diferentes fórmulas para obtener el pH, pOH y las concentraciones de los iones hidrógeno e hidróxido.

Elegí este tema porque ya tengo conocimientos sobre cómo resolver este tipo de ejercicios y considero que es una buena opción para convertirlo en un programa de Python. La idea es que el usuario pueda ingresar los datos de una disolución, seleccionar el cálculo que necesita y obtener los resultados sin tener que hacer todas las operaciones manualmente.

### 3. Entradas del problema

Para realizar los cálculos, el programa podrá solicitar los siguientes datos:

| Entrada | Tipo de dato | Descripción |
|---|---|---|
| Sustancia química | Texto | Nombre o fórmula de la sustancia |
| Tipo de sustancia | Texto | Ácido o base |
| Concentración | Decimal | Concentración molar de la disolución |
| Masa | Decimal | Cantidad de sustancia en gramos |
| Volumen | Decimal | Volumen de la disolución |
| Temperatura | Decimal | Temperatura de la disolución |

Los datos dependerán del cálculo que el usuario quiera realizar. También se validará que los valores ingresados sean correctos y que no existan concentraciones negativas o iguales a cero.

### 4. Procesos y fórmulas

El programa utilizará las fórmulas que hemos aprendido en Química para resolver los ejercicios.

Las principales serán:

**Para calcular el pH:**

pH = -log[H⁺]

**Para calcular el pOH:**

pOH = -log[OH⁻]

**Relación entre pH y pOH:**

pH + pOH = 14

**Producto iónico del agua a 25 °C:**

Kw = [H⁺][OH⁻] = 1.0 × 10⁻¹⁴

También se tomará en cuenta que los ácidos y bases fuertes se disocian completamente en agua. Por eso, dependiendo de la sustancia, se deberá considerar la cantidad de iones que produce.

### 5. Salidas esperadas

Al terminar cada operación, el programa mostrará los resultados correspondientes:

- Concentración de iones H⁺.
- Concentración de iones OH⁻.
- Valor del pH.
- Valor del pOH.
- Indicación de si la disolución es ácida, básica o neutra.
- Registro de los cálculos realizados anteriormente.

### 6. Ejemplo original resuelto

Para comprobar que el programa funcione correctamente, utilizaré un ejercicio que resolví anteriormente en mi tarea de Química General Aplicada, correspondiente al ejercicio 16.36 (a).

**Enunciado:**

Calcular la concentración de iones hidróxido [OH⁻] y el pH de una disolución de KOH 0.0050 M.

**Datos:**

- Sustancia: KOH.
- Concentración: 0.0050 M.
- Temperatura: 25 °C.

**Procedimiento:**

Primero se escribe la disociación del hidróxido de potasio:

KOH → K⁺ + OH⁻

Como el KOH es una base fuerte, se disocia completamente, por lo tanto:

[OH⁻] = 0.0050 M

Después calculamos el pOH:

pOH = -log(0.0050)

pOH = 2.30

Finalmente calculamos el pH:

pH = 14 - 2.30

pH = 11.70

**Resultados obtenidos:**

- [OH⁻] = 0.0050 M.
- pOH = 2.30.
- pH = 11.70.
- La disolución es básica.

Se incluirá la fotografía del ejercicio resuelto a mano como evidencia del problema original.

### 7. Alcance de la aplicación

El programa tendrá un menú principal para que el usuario pueda elegir qué operación desea realizar.

Las opciones que tendrá serán:

1. Calcular el pH de un ácido fuerte.
2. Calcular el pOH de una base fuerte.
3. Calcular la concentración de iones H⁺.
4. Calcular la concentración de iones OH⁻.
5. Identificar si una disolución es ácida, básica o neutra.
6. Consultar el historial de cálculos.
7. Salir del programa.

También se agregarán validaciones para evitar que el programa acepte datos incorrectos.

### 8. Comprobación de los requisitos técnicos

Considero que este problema cumple con los requisitos del proyecto porque permite utilizar diferentes elementos de programación que hemos visto durante el curso.

Se podrán utilizar variables para almacenar los datos, operaciones para realizar los cálculos, condiciones para seleccionar las opciones del menú, ciclos para mantener el programa funcionando y listas para guardar los resultados.

Además, se podrán crear al menos dos clases con diferentes funciones y responsabilidades, utilizando constructores, atributos y métodos.

Por último, contamos con un ejercicio resuelto anteriormente en Química que servirá para comparar los resultados obtenidos por el programa y comprobar que los cálculos sean correctos.