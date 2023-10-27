import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import re
from TDA.objeto import Objeto
from TDA.error import Error
from TDA.token import Token

# Constantes que definen el ancho y el alto de la ventana
WIDTH = 1089  # Ancho
HEIGHT = 600 # Alto

path = ""

#valore finales leidos del archivo
CARACTERES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ''""\",[]{.}1234567890 :(){};=*/#"
operacionesPermitidas = [
    "imprimir",
    "imprimirln",
    "conteo",
    "promedio",
    "contarsi",
    "datos",
    "sumar",
    "max",
    "min",
    "exportarReporte"
    ]
obj = Objeto()

#expresiones Regulares
ClavesRE = r'Claves\s*=\s*\['
ClavesRE2 = r'^\s*\]\s*$'
ValoresClavesRE = r'"{1}(.*?)",{0,1}'
ClavesRE3 = r'Claves\s*=\s*\[(.*?)\]'
ImprimirRE = r'imprimir\("([^"]*)"\);'
ImprimirlnRE = r'imprimirln\("([^"]*)"\);'
RegistrosRE = r'Registros\s*=\s*\['
RegistrosRE2 = r'^\s*\]\s*$'
ValoresRegistrosRE = r'\{([^}]+)\}'
ConteoRE = r'conteo\(\);'
PromedioRE = r'promedio\("([^"]*)"\);'
ContarSiRE = r'contarsi\((.*?)\);'
ValoresContarSiRE = r'\{([^}]+)\}'
DatosRE = r'datos\(\);'
SumarRE = r'sumar\("([^"]*)"\);'
MaxRE = r'max\("([^"]*)"\);'
MinRE = r'min\("([^"]*)"\);'
ReporteRE = r'exportarReporte\("([^"]*)"\);'

def Leer(path):
    obj.iniciliza()
    guardar()
    contador = 0
    entry2.config(state="normal")
    entry2.delete(1.0, tk.END)
    with open(path, "r") as file:
        linea = file.readline()
        while linea:
            contador += 1

            imprimir = None
            imprimirLN = None
            claves = None
            claves2 = None
            registro = None
            conteo = None
            promedio = None
            contarsi = None
            datos = None
            sumar = None
            maxi = None
            mini = None
            reporte = None

            imprimir = re.findall(ImprimirRE, linea)
            imprimirLN = re.findall(ImprimirlnRE, linea)
            claves2 = re.findall(ClavesRE3, linea)
            claves = re.findall(ClavesRE, linea)
            registro = re.findall(RegistrosRE, linea)
            conteo = re.findall(ConteoRE, linea)
            promedio = re.findall(PromedioRE, linea)
            contarsi = re.findall(ContarSiRE, linea)
            datos = re.findall(DatosRE, linea)
            sumar = re.findall(SumarRE, linea)
            maxi = re.findall(MaxRE, linea)
            mini = re.findall(MinRE, linea)
            reporte = re.findall(ReporteRE, linea)

            if "'''" in linea or '"""' in linea:
                obj.tokens.append(Token("Identificador","'''",contador,linea.index("'''") + 1))
                linea = file.readline()
                contador += 1
                while ("\'\'\'" not in linea or '"""' in linea) and linea != "":
                    linea = file.readline()
                    contador += 1
                    continue
                obj.tokens.append(Token("Identificador","'''",contador,linea.index("'''") + 1))
                linea = file.readline()
                continue
            elif "#" in linea:
                obj.tokens.append(Token("Identificador","#",contador,linea.index("#")))
                linea = file.readline()
                continue
            elif imprimir:
                obj.tokens.append(Token("Identificador","imprimir",contador,linea.index("imprimir")+ 1))
                obj.tokens.append(Token("Delimitador","(",contador,linea.index("(")+ 1))
                obj.tokens.append(Token("Cadena",imprimir[0],contador,linea.index(imprimir[0])+ 1))
                obj.tokens.append(Token("Delimitador",")",contador,linea.index(")")+ 1))
                obj.tokens.append(Token("Delimitador",";",contador,linea.index(";")+ 1))
                entry2.insert(tk.END, str(imprimir[0]).replace("/", "\n"))
                linea = file.readline()
                continue
            elif imprimirLN:
                obj.tokens.append(Token("Identificador","imprimirln",contador,linea.index("imprimirln")+ 1))
                obj.tokens.append(Token("Delimitador","(",contador,linea.index("(")+ 1))
                obj.tokens.append(Token("Cadena",imprimirLN[0],contador,linea.index(imprimirLN[0])+ 1))
                obj.tokens.append(Token("Delimitador",")",contador,linea.index(")")+ 1))
                obj.tokens.append(Token("Delimitador",";",contador,linea.index(";")+ 1))
                valor = imprimirLN[0].replace("/", "\n")
                entry2.insert(tk.END, f"{valor}\n")
                linea = file.readline()
                continue
            elif claves2:
                obj.tokens.append(Token("Identificador","Claves",contador,linea.index("Claves")+ 1))
                obj.tokens.append(Token("Asignacion","=",contador,linea.index("=")+ 1))
                obj.tokens.append(Token("Delimitador","[",contador,linea.index("[")+ 1))
                extraer = re.findall(ValoresClavesRE, claves2[0])
                obj.addClaves(extraer)
                for a in extraer:
                    obj.tokens.append(Token("Literal de cadena",a,contador,linea.index(a)+ 1))
                obj.tokens.append(Token("Delimitador","]",contador,linea.index("]")+ 1))
                linea = file.readline()
                continue
            elif claves:
                obj.tokens.append(Token("Identificador","Claves",contador,linea.index("Claves")+ 1))
                obj.tokens.append(Token("Asignacion","=",contador,linea.index("=")+ 1))
                obj.tokens.append(Token("Delimitador","[",contador,linea.index("[")+ 1))
                linea = file.readline()
                contador += 1
                extraer = re.findall( ValoresClavesRE, linea)
                while extraer:
                    obj.addClaves(extraer)
                    for a in extraer:
                        obj.tokens.append(Token("Literal de cadena",a,contador,linea.index(a)+ 1))
                    linea = file.readline()
                    contador += 1
                    extraer = re.findall( ValoresClavesRE, linea)
                extraer = None
                extraer = re.findall(ClavesRE2, linea)
                if extraer:
                    obj.tokens.append(Token("Delimitador","]",contador,linea.index("]")+ 1))
                    linea = file.readline()
                    continue
            elif registro:
                obj.tokens.append(Token("Identificador","Regsitros",contador,linea.index("Registros")+ 1))
                obj.tokens.append(Token("Asignacion","=",contador,linea.index("=")+ 1))
                obj.tokens.append(Token("Delimitador","[",contador,linea.index("[")+ 1))
                linea = file.readline()
                contador += 1
                extraer = re.findall(ValoresRegistrosRE, linea)
                while extraer:
                    obj.addRegistros(extraer[0].replace(" ","").replace('"', "").split(","))
                    cosa = extraer[0].replace(' "', "").replace('"', "").split(",")
                    cosa = [valor.strip() for valor in cosa]
                    for a in cosa:
                        obj.tokens.append(Token("Literal de cadena",a,contador,linea.index(a)+ 1))
                    linea = file.readline()
                    contador += 1
                    extraer = re.findall(ValoresRegistrosRE, linea)
                extraer = None
                extraer = re.findall(RegistrosRE2, linea)
                if extraer:
                    obj.tokens.append(Token("Delimitador","]",contador,linea.index("]")+ 1))
                    linea = file.readline()
                    continue
            elif conteo:
                obj.tokens.append(Token("Identificador","conteo",contador,linea.index("conteo")+ 1))
                obj.tokens.append(Token("Delimitador","(",contador,linea.index("(")+ 1))
                obj.tokens.append(Token("Delimitador",")",contador,linea.index(")")+ 1))
                obj.tokens.append(Token("Delimitador",";",contador,linea.index(";")+ 1))
                entry2.insert(tk.END, f"{obj.conteo()}\n")
                linea = file.readline()
                continue
            elif promedio:
                obj.tokens.append(Token("Identificador","promedio",contador,linea.index("promedio")+ 1))
                obj.tokens.append(Token("Delimitador","(",contador,linea.index(")")+ 1))
                obj.tokens.append(Token("Literal de cadena",promedio[0],contador,linea.index(promedio[0])+ 1))
                obj.tokens.append(Token("Delimitador",")",contador,linea.index(")")+ 1))
                obj.tokens.append(Token("Delimitador",";",contador,linea.index(";")+ 1))
                entry2.insert(tk.END, f"{obj.promedio(promedio[0])}\n")
                linea = file.readline()
                continue
            elif contarsi:
                var = contarsi[0].replace(" ","").replace('"', "").split(",")
                obj.tokens.append(Token("Identificador","contarsi",contador,linea.index("contarsi")+ 1))
                obj.tokens.append(Token("Delimitador","(",contador,linea.index(")")+ 1))
                obj.tokens.append(Token("Literal de cadena",var[0],contador,linea.index(var[0])+ 1))
                obj.tokens.append(Token("Literal de cadena",var[1],contador,linea.index(var[1])+ 1))
                obj.tokens.append(Token("Delimitador",")",contador,linea.index(")")+ 1))
                obj.tokens.append(Token("Delimitador",";",contador,linea.index(";")+ 1))
                if len(var) == 2:
                    entry2.insert(tk.END, f"{obj.contarsi(var[0], var[1])}\n")
                    linea = file.readline()
                    continue
            elif datos:
                obj.tokens.append(Token("Identificador","datos",contador,linea.index("datos")+ 1))
                obj.tokens.append(Token("Delimitador","(",contador,linea.index("(")+ 1))
                obj.tokens.append(Token("Delimitador",")",contador,linea.index(")")+ 1))
                obj.tokens.append(Token("Delimitador",";",contador,linea.index(";")+ 1))
                for valor in obj.claves:
                    entry2.insert(tk.END, f"{valor}".ljust(15))
                entry2.insert(tk.END, "\n")
                for valor in obj.registros:
                    for registro in valor:
                        entry2.insert(tk.END, f"{registro}".ljust(15))
                    entry2.insert(tk.END, "\n")
                linea = file.readline()
                continue
            elif sumar:
                obj.tokens.append(Token("Identificador","sumar",contador,linea.index("sumar")+ 1))
                obj.tokens.append(Token("Delimitador","(",contador,linea.index("(")+ 1))
                obj.tokens.append(Token("Literal de cadena",sumar[0],contador,linea.index(sumar[0])+ 1))
                obj.tokens.append(Token("Delimitador",")",contador,linea.index(")")+ 1))
                obj.tokens.append(Token("Delimitador",";",contador,linea.index(";")+ 1))
                entry2.insert(tk.END, f"{obj.sumar(sumar[0])}\n")
                linea = file.readline()
                continue
            elif maxi:
                obj.tokens.append(Token("Identificador","max",contador,linea.index("max")+ 1))
                obj.tokens.append(Token("Delimitador","(",contador,linea.index("(")+ 1))
                obj.tokens.append(Token("Literal de cadena",maxi[0],contador,linea.index(maxi[0])+ 1))
                obj.tokens.append(Token("Delimitador",")",contador,linea.index(")")+ 1))
                obj.tokens.append(Token("Delimitador",";",contador,linea.index(";")+ 1))
                entry2.insert(tk.END, f"{obj.max(maxi[0])}\n")
                linea = file.readline()
                continue
            elif mini:
                obj.tokens.append(Token("Identificador","min",contador,linea.index("min")+ 1))
                obj.tokens.append(Token("Delimitador","(",contador,linea.index("(")+ 1))
                obj.tokens.append(Token("Literal de cadena",mini[0],contador,linea.index(mini[0])+ 1))
                obj.tokens.append(Token("Delimitador",")",contador,linea.index(")")+ 1))
                obj.tokens.append(Token("Delimitador",";",contador,linea.index(";")+ 1))
                entry2.insert(tk.END, f"{obj.min(mini[0])}\n")
                linea = file.readline()
                continue
            elif reporte:
                obj.tokens.append(Token("Identificador","exportarReporte",contador,linea.index("exportarReporte")+ 1))
                obj.tokens.append(Token("Delimitador","(",contador,linea.index("(")+ 1))
                obj.tokens.append(Token("Literal de cadena",reporte[0],contador,linea.index(reporte[0])+ 1))
                obj.tokens.append(Token("Delimitador",")",contador,linea.index(")")+ 1))
                obj.tokens.append(Token("Delimitador",";",contador,linea.index(";")+ 1))
                obj.reporte(reporte[0])
                linea = file.readline()
                continue
            if (linea[0] != "\n") and (linea[0].replace(" ","") != ""):
                errorsintactico(contador, linea)
            linea = file.readline()
    entry2.config(state="disabled")
    getErrores(path)

def getErrores(path):
    try:
        with open(path, "r") as file:
            lineas = file.read().splitlines()
            for numero, linea in enumerate(lineas, start=1):
                for caracter in linea:
                    if caracter not in CARACTERES:
                        #print(f"Error sintactico en la linea {numero} y columna {linea.index(caracter) + 1} el caracter es {caracter}")
                        obj.errores.append(Error(numero, "lexico", caracter, linea.index(caracter) + 1 ))
    except AttributeError as e:
        messagebox.showinfo("Error", "Error al buscar arrores lexicos.")

def errorsintactico(fila, caracter ):
    obj.errores.append(Error(fila, "sintactico", caracter))


def abrir():
    try:
        global path
        path = filedialog.askopenfile(title="Seleccione el archivo",filetypes=(("bizdata files", ".bizdata"),("all files", ".*")))
        path = path.name
        with open(path, "r") as obj:
            entry.delete(1.0, tk.END)
            entry.insert(tk.END, obj.read())
            button.config(state="normal")
    except:
        messagebox.showerror("Error", "Error al abrir el archivo o se cerro la ventana, intentelo de nuevo")

def guardar():
        contenido = entry.get("1.0", "end-1c")
        try:
            with open(path, "w") as file:
                file.write(contenido)
        except:
            print("se produjo un error al guardar el archivo")

def guardarComo():
    if entry.get("1.0", "end-1c"):
        try:
            contenido = entry.get("1.0", "end-1c")
            nombre_archivo = filedialog.asksaveasfilename(defaultextension=".bizdata", filetypes=[("Archivos BIZDATA", "*.bizdata")])
            try:
                with open(nombre_archivo, "w") as salida:
                    salida.write(contenido)
                messagebox.showinfo("Guardado correcto", f"El archivo llamado {nombre_archivo} se guardo correctamente")
            except:
                print("se produjo un error al guardar el archivo")
        except:
            messagebox.showinfo("Error al Guardar Como", "Ocurrio un error inesperado al guardar el archivo como.")
    else:
        messagebox.showinfo("Campo Vacio", "El espacio de Texto esta Vacio o no se ha cargado un archivo, no se puede guardar.")

# Funcion que se ejecuta al seleccionar una opcion del combobox
def ejecutar_funcion(event):
    seleccion = combobx.get()
    if seleccion == "Abrir":
        abrir()
    elif seleccion == "Guardar":
        try:
            if entry.get("1.0", "end-1c"):
                guardar()
                messagebox.showinfo("Guardado correcto", "El archivo se guardo correctamente")
            else:
                messagebox.showinfo("Campo Vacio", "El espacio de Texto esta Vacio o no se ha cargado un archivo, no se puede guardar.")
        except:
            messagebox.showinfo("se produjo un error al guardar el archivo")
    elif seleccion == "Guardar como":
        guardarComo()
    elif seleccion == "Salir":
        root.destroy()

def ejecutar_funcion2(event):
    seleccion = combobx2.get()
    if seleccion == "Reporte de Tokens":
        try:
            if entry.get("1.0", "end-1c"):
                obj.imprimirTokens()
                messagebox.showinfo("Errores generados", "El archivo de tokens se guardo correctamente")
            else:
                messagebox.showinfo("Campo Vacio", "El espacio de Texto esta Vacio.")
        except:
            messagebox.showinfo("se produjo un error")
    elif seleccion == "Reporte de Errores":
        try:
            if entry.get("1.0", "end-1c"):
                obj.imprimirErrores()
                messagebox.showinfo("Errores generados", "El archivo de errores se guardo correctamente")
            else:
                messagebox.showinfo("Campo Vacio", "El espacio de Texto esta Vacio.")
        except:
            messagebox.showinfo("se produjo un error")
    elif seleccion == "Arbol de derivacion":
        pass

# Creacion de la ventana
root = tk.Tk()
root.title("Analizador - Editor de texto")
root.resizable(False, False)
root.configure(bg="#444654")

# Centrar la ventana en la pantalla
ancho_pantalla = (root.winfo_screenwidth() - WIDTH) // 2 
alto_pantalla = (root.winfo_screenheight() - HEIGHT - 50) // 2 # 50 es la altura de la barra de tareas
root.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT,ancho_pantalla, alto_pantalla))

# Colorea el fondo de la ventana
label_fondo = tk.Label(root, background="#343541")
label_fondo.place(x=0, y=0, width=WIDTH, height=37)

# Crearcion de estilo para los combobox
style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "#3E447D", background= "#3E447D", foreground= "white", 
                bordercolor= "#343541", arrowcolor= "white", borderwidth= 0.5, lightcolor= "white", 
                darkcolor= "black")

# Creacion del combobox
combobx = ttk.Combobox(root)
combobx.place(x=100, y=100)
combobx["values"] = ["Abrir", "Guardar", "Guardar como", "Salir"] # Valores del combobox
combobx.current(0) # Valor por defecto del combobo
combobx.configure(foreground='#E0E0E0')
combobx.place(x=10, y=7, width=100, height=23)

combobx2 = ttk.Combobox(root)
combobx2.place(x=100, y=100)
combobx2["values"] = ["Reporte de Tokens", "Reporte de Errores", "Arbol de derivacion"] # Valores del combobox
combobx2.current(0) # Valor por defecto del combobo
combobx2.configure(foreground='#E0E0E0')
combobx2.place(x=270, y=7, width=150, height=23)

# Evento que se ejecuta al seleccionar una opcion del combobox
combobx.bind("<<ComboboxSelected>>", ejecutar_funcion)
combobx2.bind("<<ComboboxSelected>>", ejecutar_funcion2)

# Creacion de los botones
button = tk.Button(root, text="Analizar", bg="#333766", fg="white", borderwidth=0.5, state="disabled" , command= lambda: Leer(path))
#button2 = tk.Button(root, text="Errores", bg= "#333766", fg="white", borderwidth=0.5)
#button3 = tk.Button(root, text="Reporte", bg="#333766", fg="white", borderwidth=0.5)

# Posicion de los botones
button.place(x=140, y=7, width=100, height=23)
#button2.place(x=270, y=7, width=100, height=23, )
#button3.place(x=400, y=7, width=100, height=23)

# Creacion del tetxbox
entry = tk.Text(root, bg="#343541", fg="white")
entry.place(x=15, y=60, width=504, height=524)
entry2 = tk.Text(root, bg="#343541", fg="white", state="disabled")
entry2.place(x=520, y=60, width=554, height=524)

# Creacion de una etiqueda de advertencia
etiqueta = tk.Label(root, text="Esta ventana no se puede maximizar ni redimensionar.", bg="#444654", fg="white")
etiqueta.pack(padx=20, pady=37)

# Main
root.mainloop()