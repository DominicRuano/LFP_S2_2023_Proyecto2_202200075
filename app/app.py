import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import re
from TDA.objeto import Objeto

# Constantes que definen el ancho y el alto de la ventana
WIDTH = 1300  # Ancho
HEIGHT = 600 # Alto

path = ""

#valore finales leidos del archivo
claves = []
obj = Objeto()

#expresiones Regulares
ClavesRE = r'Claves\s*=\s*\['
ClavesRE2 = r'^\s*\]\s*$'
ValoresClavesRE = r'"{1}(.*?)",{0,1}'
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
    entry2.config(state="normal")
    with open(path, "r") as file:
        linea = file.readline()
        while linea:

            imprimir = None
            imprimirLN = None
            claves = None
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
                linea = file.readline()
                while "\'\'\'" not in linea or '"""' in linea:
                    linea = file.readline()
                    continue
                linea = file.readline()
                continue
            elif "#" in linea:
                linea = file.readline()
                continue
            elif imprimir:
                entry2.insert(tk.END, str(imprimir[0]).replace("/", "\n"))
                linea = file.readline()
                continue
            elif imprimirLN:
                valor = imprimirLN[0].replace("/", "\n")
                entry2.insert(tk.END, f"{valor}\n")
                linea = file.readline()
                continue
            elif claves:
                linea = file.readline()
                extraer = re.findall(ValoresClavesRE, linea)
                while extraer:
                    obj.addClaves(extraer)
                    linea = file.readline()
                    extraer = re.findall( ValoresClavesRE, linea)
                extraer = None
                extraer = re.findall(ClavesRE2, linea)
                if extraer:
                    linea = file.readline()
                    continue
                print("error en claves")
            elif registro:
                linea = file.readline()
                extraer = re.findall(ValoresRegistrosRE, linea)
                while extraer:
                    obj.addRegistros(extraer[0].replace(" ","").replace('"', "").split(","))
                    linea = file.readline()
                    extraer = re.findall(ValoresRegistrosRE, linea)
                extraer = None
                extraer = re.findall(RegistrosRE2, linea)
                if extraer:
                    linea = file.readline()
                    continue
                print("error en Registros")
            elif conteo:
                entry2.insert(tk.END, f"{obj.conteo()}\n")
                linea = file.readline()
                continue
            elif promedio:
                entry2.insert(tk.END, f"{obj.promedio(promedio[0])}\n")
                linea = file.readline()
                continue
            elif contarsi:
                var = contarsi[0].replace(" ","").replace('"', "").split(",")
                if len(var) == 2:
                    entry2.insert(tk.END, f"{obj.contarsi(var[0], var[1])}\n")
                    linea = file.readline()
                    continue
            elif datos:
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
                entry2.insert(tk.END, f"{obj.sumar(sumar[0])}\n")
                linea = file.readline()
                continue
            elif maxi:
                entry2.insert(tk.END, f"{obj.max(maxi[0])}\n")
                linea = file.readline()
                continue
            elif mini:
                entry2.insert(tk.END, f"{obj.min(mini[0])}\n")
                linea = file.readline()
                continue
            elif reporte:
                obj.reporte(reporte[0])
                linea = file.readline()
                continue
            if linea != "\n":
                print("XX",linea.replace("\n", ""))
            linea = file.readline()
    entry2.config(state="disabled")

def abrir():
    try:
        global path
        path = filedialog.askopenfile(title="Seleccione el archivo",filetypes=(("bizdata files", ".bizdata"),("all files", ".*")))
        if messagebox.askquestion("Archivo", f"¿Está seguro que {path.name} es el archivo correcto?") == "yes":
            path = path.name
            with open(path, "r") as obj:
                entry.delete(1.0, tk.END)
                entry.insert(tk.END, obj.read())
    except:
        messagebox.showerror("Error", "Error al abrir el archivo o se cerro la ventana, intentelo de nuevo")

# Funcion que se ejecuta al seleccionar una opcion del combobox
def ejecutar_funcion(event):
    seleccion = combobx.get()
    if seleccion == "Abrir":
        abrir()
    elif seleccion == "Guardar":
        pass
    elif seleccion == "Guardar como":
        pass
    elif seleccion == "Salir":
        root.destroy()


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
label_fondo.place(x=0, y=0, width=900, height=37)

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

# Evento que se ejecuta al seleccionar una opcion del combobox
combobx.bind("<<ComboboxSelected>>", ejecutar_funcion)

# Creacion de los botones
button = tk.Button(root, text="Analizar", bg="#333766", fg="white", borderwidth=0.5, command= lambda: Leer(path))
button2 = tk.Button(root, text="Errores", bg= "#333766", fg="white", borderwidth=0.5)
button3 = tk.Button(root, text="Reporte", bg="#333766", fg="white", borderwidth=0.5)

# Posicion de los botones
button.place(x=140, y=7, width=100, height=23)
button2.place(x=270, y=7, width=100, height=23, )
button3.place(x=400, y=7, width=100, height=23)

# Creacion del tetxbox
entry = tk.Text(root, bg="#343541", fg="white")
entry.place(x=15, y=60, width=634, height=524)
entry2 = tk.Text(root, bg="#343541", fg="white", state="disabled")
entry2.place(x=651, y=60, width=634, height=524)

# Creacion de una etiqueda de advertencia
etiqueta = tk.Label(root, text="Esta ventana no se puede maximizar ni redimensionar.", bg="#444654", fg="white")
etiqueta.pack(padx=20, pady=37)

# Main
root.mainloop()