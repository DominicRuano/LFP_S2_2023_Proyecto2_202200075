# LABORATORIO LENGUAJES FORMALES Y DE PROGRAMACION Sección B- 🖥️
## Manual de usuario 📚
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
    * ~~Graphviz~~
* Git  📜
* Github
---

## Enlaces de Utilidad  🔗
*  [instalacion de Python y VSC](https://www.youtube.com/watch?v=bZjulmpBIGk) 📹
*  [~~sitio oficial de graphviz~~](https://graphviz.org/)

___
## Guia de la interfaz grafica para un usuario

>   **Menu.**
    se puede observar el menu inicial del sistema donde se observa el campo de texto vacio.
>*   *1.* Combo donde se puede acceder a distintas opciones que se explicaran mas adelante.
>* *2.* Boton analizar donde se analizara unicamente si se detecta un archivo abierto y que el campo de texto no haya sigo borrado.
>* *3.* Combo 2 donde se puede acceder a distintas opciones que se explicaran mas adelante.
>*  *4.* campo de texto donde se cargara el texto del archivo leido
>* *5.* la consola donde se mostraran los comandos ejecutados
<img src="https://i.ibb.co/4VW81JW/GIUI.png" alt="funcion main" style="width:500px;"/>

---
>   **Combo**
    Este combobox contiene algunas de ls funciones del programa, se acede dando click para desplegar las opciones y seleccionando una de ellas.
>*   *1.1* Abrir, abre una ventana para seleccionar que archivo deseamos abrir en el programa.
>* *1.2* Guardar, guarda los cambios en le mismo archivo que se abrio.
>* *1.3* Abre un menu donde debemos elegir el nombre y la ubicacion del archivo.
>*  *1.4* Salir, cierra el programa.
<img src="https://i.ibb.co/XXTL2SQ/combo.png" alt="funcion main" style="width:500px;"/>

---
>   **Combo 2**
    Este combobox contiene algunas de ls funciones del programa, se acede dando click para desplegar las opciones y seleccionando una de ellas.
>*   *1* Genera un archivo llamado reporte de tokens.
>* *2* Genera un reposrte de errores.
>* *3* Genera un arbol de derivacion usando grapviz.
<img src="https://i.ibb.co/VDZPFw1/combo2.png" alt="funcion main" style="width:500px;"/>
---
>*   **Menu para Abrir un archivo.**
    esta ventana se muestra al seleccionar abrir, esta misma requiere que se seleccione un archivo para abrirlo, esta ventana cuenta con un filtro para visualizar unicamente los archivos con extencions **.json**
<img src="https://i.ibb.co/JQgfyBc/abrir.png" alt="funcion main" style="width:500px;"/>

---
>*   **Error en caso de errores.**
    En casi de detectarse un error ya sea porque no se seleccciono un archivo o cualquier otro error se mostrara este mensaje de error, seguido se podri volver a intentar abrir un archivo.
<img src="https://i.ibb.co/VVpp9tN/error-abrir.png" alt="funcion main" style="width:400px;"/>

---
>*   **Confirmacion de archivo.**
    Si se abrio al archivo sin errores mostrar este mensaje para asegurarse que esa sea la ruta correcta.
<img src="https://i.ibb.co/k06MfyP/conifirmacion-abrir.png" alt="funcion main" style="width:400px;"/>

---
>*   **Vista del menu para editar el archivo abierto.**
    si se abre correctamente el archivo este mismo se mostrara en el campo de texto en el programa.
<img src="https://i.ibb.co/p0rmrBC/GIU.png" alt="funcion main" style="width:500px;"/>

---
>*   **Ventana de confirmacion de guardado.**
    En casi se guarde el archivo se mostrar este mensaje que confirmara que se guardo correctamente el archivo.
<img src="https://i.ibb.co/gvfHxJ5/guardar.png" alt="funcion main" style="width:400px;"/>

---
>*   **Ventana de Guardar como.**
    Para guardar como es necesario que se determine un nombre para el archivo y una ubicacion.
<img src="https://i.ibb.co/jRrR0xJ/guardar-como.png" alt="funcion main" style="width:500px;"/>

---
>*   **Muchas gracias eso seria todo**
    gracias por leer todo este documento tenga un buen dia aux.
<img src="https://i.ibb.co/nB08qk2/1ac04daf-e3d7-4dbd-8c43-8877808ec602.jpg" alt="funcion main" style="width:200px;"/>