# Actvidad de acondicionamiento en desarrollo de software

# Desarrolloe los ejercicios presentados a continuación y haga push permanentemente a medida que va logrando las soluciones.

---

## Ejercicio 1: Suma de Dígitos

**Descripción:**  
Dado un número entero, calcula la suma de todos sus dígitos.

**Entrada:**  
- Una línea que contenga un número entero.

**Salida:**  
- Un entero que es la suma de los dígitos.

**Ejemplo de entrada:**
1234
**Ejemplo de salida:**
10

**Pistas:**  
- Puedes convertir el número a cadena para iterar sobre cada carácter o usar operaciones aritméticas (módulo y división).

---

## Ejercicio 2: Contar Vocales en una Cadena

**Descripción:**  
Dada una cadena de texto, cuenta el número de vocales (a, e, i, o, u, sin distinguir mayúsculas de minúsculas) que contiene.

**Entrada:**  
- Una línea de texto.

**Salida:**  
- Un entero que representa la cantidad de vocales encontradas.

**Ejemplo de entrada:**
Hola Mundo
**Ejemplo de salida:**
4


**Pistas:**  
- Recorre la cadena carácter por carácter y compara con las vocales.
- Convierte la cadena a minúsculas para simplificar la comparación.

---

## Ejercicio 3: Verificar Palíndromo

**Descripción:**  
Determina si una cadena de texto es un palíndromo, es decir, se lee igual de izquierda a derecha que de derecha a izquierda.  
**Importante:** Debes ignorar espacios y diferencias entre mayúsculas y minúsculas.

**Entrada:**  
- Una línea de texto.

**Salida:**  
- Imprime `"Sí"` si la cadena es un palíndromo, o `"No"` en caso contrario.

**Ejemplo de entrada:**
anita lava la tina
**Ejemplo de salida:**
Si


**Pistas:**  
- Elimina los espacios y convierte la cadena a una forma uniforme (por ejemplo, a minúsculas) antes de comparar.
- Puedes comparar la cadena con su reverso.

---

## Ejercicio 4: Invertir una Lista de Números

**Descripción:**  
Dada una lista de números enteros separados por espacios, invierte el orden de los elementos y muestra la lista invertida en una sola línea.

**Entrada:**  
- Una línea con números enteros separados por espacios.

**Salida:**  
- Una línea con los números en orden inverso, separados por espacios.

**Ejemplo de entrada:**
1 2 3 4 5
**Ejemplo de salida:**
5 4 3 2 1


**Pistas:**  
- Puedes utilizar la técnica de slicing (`lista[::-1]`) o el método `reverse()`.

---

## Ejercicio 5: Contar Palabras en una Cadena

**Descripción:**  
Dada una cadena de texto, cuenta la cantidad de palabras que contiene.  
Se asume que las palabras están separadas por uno o más espacios.

**Entrada:**  
- Una línea de texto.

**Salida:**  
- Un entero que indica la cantidad de palabras.

**Ejemplo de entrada:**
Hola mundo desde Python
**Ejemplo de salida:**
4


**Pistas:**  
- Utiliza el método `split()` para dividir la cadena en palabras.

---

## Ejercicio 6: Encontrar el Máximo y Mínimo

**Descripción:**  
Dada una lista de números enteros separados por espacios, determina cuál es el número mayor y cuál es el menor.

**Entrada:**  
- Una línea con números enteros separados por espacios.

**Salida:**  
- Dos enteros separados por un espacio: primero el número máximo y luego el mínimo.

**Ejemplo de entrada:**
3 1 4 1 5 9
**Ejemplo de salida:**
9 1


**Pistas:**  
- Puedes usar las funciones integradas `max()` y `min()` de Python.
