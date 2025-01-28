# Databricks notebook source
# MAGIC %md
# MAGIC <h1>Procesamiento de Datos a Gran Escala</h1>

# COMMAND ----------

# MAGIC %md
# MAGIC <h2>Operaciones con Cadenas</h2>

# COMMAND ----------

# MAGIC %md
# MAGIC <p><strong>¡Bienvenido!</strong> En este cuaderno aprenderás sobre operaciones con cadenas en el Lenguaje de Programación Python. Al finalizar, conocerás acerca de las operaciones con cadenas que se pueden realizar en Python como son, indexación, operaciones y secuencias de escape.</p>

# COMMAND ----------

# MAGIC %md
# MAGIC <h2>Tabla de Contenido</h2>
# MAGIC <div class="alert alert-block alert-info" style="margin-top: 20px">
# MAGIC     <ul>
# MAGIC         <li>
# MAGIC             <a href="#strings">¿Qué es una cadena?</a>
# MAGIC         </li>
# MAGIC         <li>
# MAGIC             <a href="#index">Indexación</a>
# MAGIC             <ul>
# MAGIC                 <li><a href="neg">Indexación Negativa</a></li>
# MAGIC                 <li><a href="slice">Slicing</a></li>
# MAGIC                 <li><a href="stride">Stride</a></li>
# MAGIC                 <li><a href="concat">Concatenar Cadenas</a></li>
# MAGIC             </ul>
# MAGIC         </li>
# MAGIC         <li>
# MAGIC             <a href="#escape">Secuencias de Escape</a>
# MAGIC         </li>
# MAGIC         <li>
# MAGIC             <a href="#operations">Operaciones con Cadenas</a>
# MAGIC         </li>
# MAGIC         <li>
# MAGIC             <a href="#quiz">Exámen sobre Cadenas</a>
# MAGIC         </li>
# MAGIC     </ul>
# MAGIC     <p>
# MAGIC         Tiempo Estimado: <strong>15 min</strong>
# MAGIC     </p>
# MAGIC </div>
# MAGIC
# MAGIC <hr>

# COMMAND ----------

# MAGIC %md
# MAGIC <h2 id="strings">¿Qué es una cadena?</h2>

# COMMAND ----------

# MAGIC %md
# MAGIC A continuación, se muestra una cadena entre comillas dobles.

# COMMAND ----------

# Usa las comillas dobles para definir una cadena

"Michael Jackson"

# COMMAND ----------

# MAGIC %md
# MAGIC También podemos usar comillas simples:

# COMMAND ----------

# Usa comillas simples para definir una cadena

'Michael Jackson'

# COMMAND ----------

# MAGIC %md
# MAGIC Una cadena puede ser una combinación de espacios y dígitos:

# COMMAND ----------

# Dígitos y espacios en una cadena

'1 2 3 4 5 6 '

# COMMAND ----------

# MAGIC %md
# MAGIC Una cadena también puede estar formada por caracteres especiales :

# COMMAND ----------

# Caracteres especiales en una cadena

'@#2_#]&*^%$'

# COMMAND ----------

# MAGIC %md
# MAGIC Podemos imprimir en pantallas una cadena usando la sentencia print:

# COMMAND ----------

# Imprimir la cadea

print("hello!")

# COMMAND ----------

# MAGIC %md
# MAGIC Podemos asignar una cadena como valor de una variable:

# COMMAND ----------

# Asignar una cadena a una variable

Name = "Michael Jackson"
Name

# COMMAND ----------

# MAGIC %md
# MAGIC <h2 id="index">Indexación</h2>

# COMMAND ----------

# MAGIC %md
# MAGIC Debemos pensar en una cadena como una secuencia ordenada. Cada elemento de la secuencia puede ser accedido utilizando un índice numérico, el cual representa el lugar que ocupa dicho elemento en la cadena:

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%201/Images/StringsIndex.png" width="600" align="center" />

# COMMAND ----------

# MAGIC %md
# MAGIC Se puede acceder al primer índice de la siguiente manera:

# COMMAND ----------

# MAGIC %md
# MAGIC <hr/>
# MAGIC <div class="alert alert-success alertsuccess" style="margin-top: 20px">
# MAGIC [Tip]: En la indexación se empieza por el 0, esto quiere decir que el primer elemento de la cadena está en el índice 0.
# MAGIC </div>
# MAGIC <hr/>

# COMMAND ----------

# Imprime el primer elemento de la cadena

print(Name[0])

# COMMAND ----------

# MAGIC %md
# MAGIC Podemos acceder el índice 6:

# COMMAND ----------

# Imprime el elemento en el índice 6 de la cadena

print(Name[6])

# COMMAND ----------

# MAGIC %md
# MAGIC También, podemos acceder al treceavo elemento:

# COMMAND ----------

# Imprime el elemento en el treceavo índice de la cadena

print(Name[13])

# COMMAND ----------

# MAGIC %md
# MAGIC <h3 id="neg">Indexación Negativa</h3>

# COMMAND ----------

# MAGIC %md
# MAGIC Con las cadenas tambien podemos usar la indexación negativa:

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%201/Images/StringsNeg.png" width="600" align="center" />

# COMMAND ----------

# MAGIC %md
# MAGIC La indexación negativa nos sirve para numerar un elemento desde el final de una cadena.

# COMMAND ----------

# MAGIC %md
# MAGIC El ultima elemento tiene el índice -1:

# COMMAND ----------

# Imprime el último elemento de la cadena

print(Name[-1])

# COMMAND ----------

# MAGIC %md
# MAGIC El primer elemento se obtiene usando como índice el -15:

# COMMAND ----------

# Imprime el primer elemento de la cadena

print(Name[-15])

# COMMAND ----------

# MAGIC %md
# MAGIC Para conocer la cantidad de caracteres en un cadena usamos <code>len</code>, que es la abreviación de length, en inglés significa longitud:

# COMMAND ----------

# Encuentra la longitud de la cadena

len("Michael Jackson")

# COMMAND ----------

# MAGIC %md
# MAGIC <h3 id="slice">Slicing</h3>

# COMMAND ----------

# MAGIC %md
# MAGIC Podemos obtener múltiples caracteres de una cadena usando el slicing, digamos desde primero hasta el cuarto y desde el octavo hasta el doceavo:

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%201/Images/StringsSlice.png" width="600" align="center" />

# COMMAND ----------

# MAGIC %md
# MAGIC <hr/>
# MAGIC <div class="alert alert-success alertsuccess" style="margin-top: 20px">
# MAGIC [Tip]: Para aplicar el slicing, el primer numero indica el índice del primer elemento, y el segundo numero indicara el índice del ultimo elemento de la sub-cadena que queremos obtener.
# MAGIC </div>
# MAGIC <hr/>

# COMMAND ----------

# Asigna una seccion de la cadena dentro de la variable Name usando los indices desde el 0 hasta el 3

Name[0:4]

# COMMAND ----------

# Asigna una seccion de la cadena dentro de la variable Name usando los indices desde el 8 hasta el 11

Name[8:12]

# COMMAND ----------

# MAGIC %md
# MAGIC <h3 id="stride">Stride</h3>

# COMMAND ----------

# MAGIC %md
# MAGIC Para usar la técnica del stride debemos asignar un valor que a continuación se explica, si usamos el '2' por ejemplo, estaremos indicando que queremos seleccionar solamente cada segundo elemento de la cadena:

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%201/Images/StringsStride.png" width="600" align="center" />

# COMMAND ----------

# Toma cada segundo elemento. Los elementos con índice 1, 3, 5 ...

Name[::2]

# COMMAND ----------

# MAGIC %md
# MAGIC También Podemos combinar el slicing con el stride. Para este caso, seleccionamos los primeros cinco elementos y después aplicamos stride:

# COMMAND ----------

# Toma cada segundo elemento desde el índice 0 al 4

Name[0:5:2]

# COMMAND ----------

# MAGIC %md
# MAGIC <h3 id="concat">Concatenar Cadenas</h3>

# COMMAND ----------

# MAGIC %md
# MAGIC Podemos concatenar o combinar cadenas usando el símbolo de suma, el resultado será una nueva cadena que surge de la combinación de ambas:

# COMMAND ----------

# Concatenar dos cadenas

Statement = Name + "is the best"
Statement

# COMMAND ----------

# MAGIC %md
# MAGIC Para replicar los valores en una cadena simplemente podemos multiplicarla por el numero de veces que deseemos. Para este caso, el numero de veces es tres. El resultado es una nueva cadena, la cual consiste en tres copias de la original:

# COMMAND ----------

# Imprime la cadena 3 veces

3 * "Michael Jackson"

# COMMAND ----------

# MAGIC %md
# MAGIC Se puede crear una nueva cadena añadiendo otra a la original contenida en la variable. Concatenada con una nueva cadena, el resultado es otra diferente, Michael Jackson pasó a ser “Michael Jackson is the best”.

# COMMAND ----------

# Concatenar cadenas

Name = "Michael Jackson"
Name = Name + " is the best"
Name

# COMMAND ----------

# MAGIC %md
# MAGIC <h2 id="escape">Secuencias de Escape</h2>

# COMMAND ----------

# MAGIC %md
# MAGIC Una barra invertida representa el inicio de una secuencia de escape. Estas representan cadenas que pudieran ser difíciles de introducir. Por ejemplo, una barra invertida seguida de una "n" representa un salto de línea. En la salida de pantalla tendremos un salto de línea cada vez que una barra invertida y la letra "n" sea encontrada.

# COMMAND ----------

# Secuencia de escape para un Salto de línea

print(" Michael Jackson \n is the best" )

# COMMAND ----------

# MAGIC %md
# MAGIC De igual forma, barra invertida "t" aplicará un espacio de tabulación:

# COMMAND ----------

# Secuencia de escape para un espacio de tabulación

print(" Michael Jackson \t is the best" )

# COMMAND ----------

# MAGIC %md
# MAGIC En caso de quieras que una barra invertida forme parte de una cadena, utiliza una doble barra invertida:

# COMMAND ----------

# Incluir una barra invertida en una cadena

print(" Michael Jackson \\ is the best" )

# COMMAND ----------

# MAGIC %md
# MAGIC Otra forma de hacer que se muestre la barra invertida de una cadena es colocando antes una “r”:

# COMMAND ----------

# La letra r le dirá a python que muestre la cadena tal cual e ignore lo que haya despues de la barra invertida

print(r" Michael Jackson \ is the best" )

# COMMAND ----------

# MAGIC %md
# MAGIC <h2 id="operations">Operaciones con Cadenas</h2>

# COMMAND ----------

# MAGIC %md
# MAGIC En Python existen muchos métodos para hacer operaciones con cadenas que pueden ser usados para manipular datos. Usaremos algunas operaciones básicas con cadenas.

# COMMAND ----------

# MAGIC %md
# MAGIC Usemos ahora el método <code>upper</code>; este método convierte los caracteres de minúsculas a mayúsculas:

# COMMAND ----------

# Convertir todos los caracteres de la cadena en mayúsculas

A = "Thriller is the sixth studio album"
print("before upper:", A)
B = A.upper()
print("After upper:", B)

# COMMAND ----------

# MAGIC %md
# MAGIC El método <code>replace</code> reemplaza un segmento de la cadena, p.ej. una sub-cadena por una nueva. Introducimos primero la parte de la cadena que queremos cambiar. En el segundo argumento pondremos el segmento que reemplazara al anterior, el resultado será una nueva cadena con una de sus partes modificada:

# COMMAND ----------

# Reemplazar la vieja sub-cadena por una nueva

A = "Michael Jackson is the best"
B = A.replace('Michael', 'Janet')
B

# COMMAND ----------

# MAGIC %md
# MAGIC La función del método <code>find</code> es encontrar una sub-cadena. El argumento del método es la sub-cadena que deseas encontrar, y el resultado será el numero del índice perteneciente al primer carácter de la sub-cadena. Podemos encontrar la sub-cadena <code>jack</code> o <code>el</code>.

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%201/Images/StringsFind.png" width="600" align="center" />

# COMMAND ----------

# Encontrar la sub-cadena. El resultado será unicamente el índice del primer elemente de la sub-cadena dentro de la cadena principal.

Name = "Michael Jackson"
Name.find('el')

# COMMAND ----------

# Encotrar la sub-cadena dentro de la cadena.

Name.find('Jack')

# COMMAND ----------

# MAGIC %md
# MAGIC Si la sub-cadena no se encuentra en la cadena principal el resultado será -1. Por ejemplo, la cadena 'Jasdfasdasdf' no es una sub-cadena:

# COMMAND ----------

# Si no se encuentra la sub-cadena en la cadena principal

Name.find('Jasdfasdasdf')

# COMMAND ----------

# MAGIC %md
# MAGIC <h2 id="quiz">Exámen sobre Cadenas</h2>

# COMMAND ----------

# MAGIC %md
# MAGIC ¿Cual es el valor de la variable <code>A</code> después de ejecutar el siguiente código?

# COMMAND ----------

A = "1"  # Asignación de una cadena de texto
print(A)  # Esto imprimirá: 1 (pero es una cadena)
print(type(A))  # Esto imprimirá: <class 'str'>



# COMMAND ----------

# MAGIC %md
# MAGIC Haz doble click <b>aquí</b> para ver la solución.
# MAGIC
# MAGIC <!-- Your answer is below:
# MAGIC "1"
# MAGIC -->

# COMMAND ----------

# MAGIC %md
# MAGIC ¿Cual es el valor de la variable <code>B</code> después de ejecutar el siguiente código?

# COMMAND ----------

B = "2"  # Asignación de una cadena de texto
print(B)  # Esto imprimirá: 2 (pero es una cadena)
print(type(B))  # Esto imprimirá: <class 'str'>



# COMMAND ----------

# MAGIC %md
# MAGIC Haz doble click <b>aquí</b> para ver la solución.
# MAGIC
# MAGIC <!-- Your answer is below:
# MAGIC "2"
# MAGIC -->

# COMMAND ----------

# MAGIC %md
# MAGIC ¿Cual es el valor de la variable <code>C</code> después de ejecutar el siguiente código?

# COMMAND ----------

A = "1"  # A es una cadena
B = "2"  # B es una cadena
C = A + B  # Concatenación de cadenas
print(C)  # Esto imprimirá: 12


C = A + B

# COMMAND ----------

# MAGIC %md
# MAGIC Haz doble click <b>aquí</b> para ver la solución.
# MAGIC
# MAGIC <!-- Your answer is below:
# MAGIC "12"
# MAGIC -->

# COMMAND ----------

# MAGIC %md
# MAGIC En la variable <code>D</code> haz uso del slicing para imprimir solo los primeros tres elementos:

# COMMAND ----------

D = "ABCDEFG"  # La variable D conserva su valor completo
print(D[:7])  # Imprime solo los primeros siete caracteres: "ABCDEFG"


D = "ABCDEFG"

# COMMAND ----------

# MAGIC %md
# MAGIC Haz doble click <b>aquí</b> para ver la solución.
# MAGIC
# MAGIC <!-- Your answer is below:
# MAGIC print(D[:3]) 
# MAGIC # or 
# MAGIC print(D[0:3])
# MAGIC -->

# COMMAND ----------

# MAGIC %md
# MAGIC Usa un valor de stride de 2 para imprimir cada segundo elemento de la cadena <code>E</code>:

# COMMAND ----------

E = " clockr1e1c1t"  # Incluye el espacio inicial
print(E)  # Esto imprimirá: " clockr1e1c1t"



E = 'clocrkr1e1c1t'

# COMMAND ----------

# MAGIC %md
# MAGIC Haz doble click <b>aquí</b> para ver la solución.
# MAGIC <!-- Your answer is below:
# MAGIC print(E[::2])
# MAGIC -->

# COMMAND ----------

# MAGIC %md
# MAGIC Imprime una barra invertida:

# COMMAND ----------

print("\\")  # Esto imprimirá una sola barra invertida: \

# COMMAND ----------

# MAGIC %md
# MAGIC Haz doble click <b>aquí</b> para ver la solución.
# MAGIC <!-- Your answer is below:
# MAGIC print("\\")
# MAGIC or
# MAGIC print(r" \ ")
# MAGIC -->

# COMMAND ----------

# MAGIC %md
# MAGIC Convierte el mayúsculas el contenido de la variable <code>F</code>:

# COMMAND ----------

F = "You are wrong"  # Contenido inicial de la variable
F_upper = F.upper()  # Convierte el contenido de F a mayúsculas
print(F_upper)  # Imprime: "YOU ARE WRONG"


F = "You are wrong"

# COMMAND ----------

# MAGIC %md
# MAGIC Haz doble click <b>aquí</b> para ver la solución.
# MAGIC
# MAGIC <!-- Your answer is below:
# MAGIC F.upper()
# MAGIC -->

# COMMAND ----------

# MAGIC %md
# MAGIC En la variable <code>G</code>, encuentra el primer índice de la sub-cadena <code>snow</code>:

# COMMAND ----------

G = """Mary had a little lamb little lamb, little lamb Mary had a little lamb 
Its fleece was white as snow And everywhere that Mary went Mary went 
Everywhere that Mary went The lamb was sure to go"""

index_snow = G.find("snow")  # Encuentra el primer índice de la subcadena "snow"
print(index_snow)  # Imprime el índice


G = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"

# COMMAND ----------

# MAGIC %md
# MAGIC Haz doble click <b>aquí</b> para ver la solución.
# MAGIC
# MAGIC <!-- Your answer is below:
# MAGIC G.find("snow")
# MAGIC -->

# COMMAND ----------

# MAGIC %md
# MAGIC En la variable <code>G</code>, reemplaza la sub-cadena <code>Mary</code> con <code>Bob</code>:

# COMMAND ----------

G = """Mary had a little lamb little lamb, little lamb Mary had a little lamb 
Its fleece was white as snow And everywhere that Mary went Mary went 
Everywhere that Mary went The lamb was sure to go"""

# Reemplazar "Mary" por "Bob"
G_replaced = G.replace("Mary", "Bob")

# Imprimir el resultado
print(G_replaced)


# COMMAND ----------

# MAGIC %md
# MAGIC Haz doble click <b>aquí</b> para ver la solución.
# MAGIC
# MAGIC <!-- Your answer is below:
# MAGIC G.replace("Mary", "Bob")
# MAGIC -->
