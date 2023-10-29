# LABORATORIO LENGUAJES FORMALES Y DE PROGRAMACION Sección B- 🖥️
## Manual de Tecnico 📚
### SEGUNDO SEMESTRE 2023 📅

```js
Universidad San Carlos de Guatemala 🎓
Programador: Dominic Juan pablo Ruano Perez 🧑‍💻
Carne: 202200075 🆔
```
---
## Descripción del Proyecto📋
Para este proyecto, se requiere que el estudiante desarrolle un analizador sintáctico y lexico, diseñado para procesar archivos con extensión **.bizdata**. Estos archivos se someterán a un análisis, a partir del cual se ejecutaran los comandos estipulados acontinuacion, y generando archivos en formato HTLM de los errores detectados.

El programa empleará la biblioteca tkinter para crear una interfaz gráfica intuitiva, lo que permitirá que los usuarios poco familiarizados con la línea de comandos y se sientan cómodos para poder utilizarlo con facilidad.

Entre las capacidades destacadas del programa se encuentran la capacidad de generar informes, abrir y editar el archivo seleccionado, y guardar los cambios de manera que se conserven las propiedades originales del archivo. Además, se ofrece la opción de guardar una copia del archivo original con un nombre diferente.

> **Expresiones regulaes.**
<img src="https://i.ibb.co/8skHYwq/re.png">
> # gramatica libre de contexto
> **Terminales** = {tkClave, tkRegistro, tkIgual, tkImprimir, tkImprimirln, tkConteo, tkPromedio, tkContarsi, tkDatos, tkSumar, tkMin, tkMax, tkMin, tkPa, tkPc, tkPuntoycoma, tkCa, tkCc, tkLa, tkLc, tkcoma, tkPalabra, tkNum}
> **estados** = {q0,q1,q2,q3}
> **Pila** = {\<inicio>,\<imprimir>,\<imprimirln>,\<Claves>,\<registros>,\<conteo>,\<promedio>,\<contaris>,\<datos>,\<sumar>,\<min>,\<max>, tkClave, tkRegistro, tkIgual, tkImprimir, tkImprimirln, tkConteo, tkPromedio, tkContarsi, tkDatos, tkSumar, tkMin, tkMax, tkMin, tkPa, tkPc, tkPuntoycoma, tkCa, tkCc, tkLa, tkLc, tkcoma, tkPalabra, tkNum}
> **Inicio** = \<inicio> 
> **Producciones**
> \<inicio> ::= \<imprimir>|\<imprimirln>|\<Claves>|\<registros>|\<conteo>|\<promedio>|\<contarsi>|
<datos>|\<sumar>|\<min>|\<max> 
> \<imprimir> ::= tkImprimir tkPa tkPalabra tkPc tkPuntoycoma
> \<imprimirln> ::= tkImprimir tkPa tkPalabra tkPc tkPuntoycoma
> \<Claves> ::= tkClaves tkPa \<elementos> tkPc 
> \<Registros> ::= tkClaves tkCa \<elementos> tkPc 
> \<elementos> ::= tkPalabra \<otroelemento>
> \<otroelemento> tkComa <elementos> | ε
> \<conteo> ::= tkConteo tkPA tkPc tkPuntoycoma
> \<Promedio> ::= tkPromedio tkPa tkPalabra tkPc tkPuntoycoma
> \<contarsi> ::= tkContarsi tkPa tkPalabra tkNum tkPc tkPuntoycoma
> \<datos> ::= tkdatos tkPa tkPc tkPuntoycoma
> \<sumar> ::= tkSumar tkPa tkPalabra tkPc tkPuntoycoma
> \<min> ::= tkMin tkPa tkPalabra tkPc tkPuntoycoma
> \<max> ::= tkMax tkPa tkPalabra tkPc tkPuntoycoma

<img src="https://i.ibb.co/YDXWHsw/automata.jpg">



>**variables**
<img src="https://i.ibb.co/bPvdgbN/variables.png">
- se definene las listas con todos los caracteres permitidos para el sistema.
- se define una lista c on todas las operaciones que el sistema podria realizar.

## Objetivos 🎯
* Objetivo General
    * El objetivo general de este proyecto es desarrollar un analizador sintáctico capaz de procesar archivos con extensión .bizdata y generar informes tanto de datos como de errores. Además, se busca proporcionar una interfaz gráfica amigable utilizando la biblioteca tkinter, para hacer que el programa sea accesible incluso para usuarios no familiarizados con la línea de comandos.
* Objetivos Específicos
    * Crear un analizador sintáctico y lexico eficiente y preciso que pueda identificar y analizar correctamente los comandos contenidos en archivos .bizdata, registrando cualquier error sintáctico y/o lexico encontrado.
    * Desarrollar una interfaz gráfica intuitiva utilizando tkinter que permita a los usuarios abrir, editar y guardar archivos .bizdata de manera sencilla y que preserve las propiedades originales del archivo. También, proporcionar la funcionalidad de guardar una copia del archivo con un nombre diferente.
---


## Herramientas Principales a Utilizar 🛠️
* Visual Studio Code 💻
* Python 🐍
* Bibliotecas de Python
    * tkinter 🖼️
    * Graphviz
* Git  📜
* Github
---

## Enlaces de Utilidad  🔗
*  [instalacion de Python y VSC](https://www.youtube.com/watch?v=bZjulmpBIGk) 📹
*  [sitio oficial de graphviz](https://graphviz.org/)
*  [Documentacion de tkinter](https://docs.python.org/3/library/tk.html)

___
## Metodo del arbol
<img src="https://i.ibb.co/B60V4FL/Calves.png
" style="width:400px;"/>
<img src="https://i.ibb.co/dtz9ysk/contarsi.png" style="width:400px;"/>
<img src="https://i.ibb.co/CQ7qrjR/conteo.png" style="width:400px;"/>
<img src="https://i.ibb.co/6y0wKKW/datos.png" style="width:400px;"/>
<img src="https://i.ibb.co/1sjBhBX/exportar-reporte.png" style="width:400px;"/>
<img src="https://i.ibb.co/CwjZ0P6/imprimir.png" style="width:400px;"/>
<img src="https://i.ibb.co/7VvMVF4/imprimir-LN.png" style="width:400px;"/>
<img src="https://i.ibb.co/my2xjJW/min.png" style="width:400px;"/>
<img src="https://i.ibb.co/gZQpDhD/promedio.png" style="width:400px;"/>
<img src="https://i.ibb.co/Cz699yk/Registros.png" style="width:400px;"/>
<img src="https://i.ibb.co/9c2D172/sumar.png" style="width:400px;"/>


___
## Funciones dentro del codigo

>*   Funcion addclaves()
    agrega las claves leidas al objeto
<img src="https://i.ibb.co/ftjgqMp/addclaves.png" style="width:700px;"/>

---
>*   Funcion addRegistro()
    agrega los registros leido al objeto
<img src="https://i.ibb.co/tHmnD4p/addregistro.png" style="width:700px;"/>

---
>*   Funcion contarsi()
    ejecuta el comando contarsi
<img src="https://i.ibb.co/TmcsgHw/contarsi.png" style="width:700px;"/>

---
>*   Funcion conteo()
    ejecuta la funcion conteo
<img src="https://i.ibb.co/tCgQq9F/conteo.png" style="width:700px;"/>

---
>*   Funcion ejecutar_funcion()
    ejecuta lo seleccionado en el primer combobox
<img src="https://i.ibb.co/hDbdJG6/ejecutar1.png" style="width:700px;"/>

---
>*   Funcion ejecutar_funcion2()
    ejecuta lo seleccionado en el segundo combobox
<img src="https://i.ibb.co/BtZ569V/ejecutar2.png
" style="width:700px;"/>

---
>*   Funcion errorsintactico()
    al detectar un error sintactico genera error
<img src="https://i.ibb.co/2Nw2m1n/errorsintactico.png" style="width:700px;"/>

---
>*   Funcion getErrores()
    genera todos los errores lexicos
<img src="https://i.ibb.co/n3Qmtzg/geterrores.png" style="width:700px;"/>
---
>*   Funcion imprimirErrores()
    genera un archivo html con todos los errores
<img src="https://i.ibb.co/vYqyDNd/imprimirerrores.png" style="width:700px;"/>

---
>*   Funcion imprimirtokens()
    genera un archivo html con todos los tokens
<img src="https://i.ibb.co/n891n0R/imprimirtokens.png" style="width:700px;"/>

>*   Muchas gracias eso seria todo
    gracias por leer todo este documento tenga un buen dia aux. 
<img src="https://i.ibb.co/nB08qk2/1ac04daf-e3d7-4dbd-8c43-8877808ec602.jpg" alt="funcion main" style="width:200px;"/>