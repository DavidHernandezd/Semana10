
from cgitb import text
from msilib.schema import TextStyle
from platform import release
from tabnanny import check
import tkinter as tk
from tkinter import messagebox

def arietmetica():
    valor1 = caja1.get()
    valor2 = caja2.get()

    if x.get() == 1:
        resultado = float(valor1) + float(valor2)
        resultstr = str(resultado)
        messagebox.showinfo(title="resultado", message=resultstr)
    elif x.get() == 2:
        resultado = float(valor1) - float(valor2)
        resultstr = str(resultado)
        messagebox.showinfo(title="resultado", message=resultstr)
    elif x.get() == 3:
        resultado = float(valor1) * float(valor2)
        resultstr = str(resultado)
        messagebox.showinfo(title="resultado", message=resultstr)
    elif x.get() == 4:
        resultado = float(valor1) / float(valor2)
        resultstr = str(resultado)
        messagebox.showinfo(title="resultado", message=resultstr)
    else:
        messagebox.showinfo(title="resultado", message="No has puesto un valor correcto")

ventana = tk.Tk()
x = tk.IntVar()
ventana.geometry("500x500")
ventana.configure(bg="#616AFF")
caja1 = tk.Entry(ventana, bg="#989EFB")
caja2 = tk.Entry(ventana,bg="#989EFB")
btn1 = tk.Button(ventana, text="Calcular", height=5, width=5, command=arietmetica, bg="#989EFB")
lb1 = tk.Label(ventana, text="Valor 1", width=5, bg="#616AFF")
lb2 = tk.Label(ventana, text="Valor 2", width=5, bg="#616AFF")
rb1 = tk.Radiobutton(ventana, text="Suma", value=1, variable=x, bg="#616AFF")
rb2 = tk.Radiobutton(ventana, text="Resta", value=2, variable=x, bg="#616AFF")
rb3 = tk.Radiobutton(ventana, text="Multiplicación", value=3, variable=x, bg="#616AFF")
rb4 = tk.Radiobutton(ventana, text="División", value=4, variable=x, bg="#616AFF")

caja1.place(relx=0.3, rely=0.2, relwidth=0.3)
caja2.place(relx=0.3, rely=0.3, relwidth=0.3)
lb1.place(relx=0.62, rely=0.2)
lb2.place(relx=0.62, rely=0.3)
rb1.place(relx=0.2, rely=0.4)
rb2.place(relx=0.32, rely=0.4)
rb3.place(relx=0.44, rely=0.4)
rb4.place(relx=0.65, rely=0.4)
btn1.place(relx=0.23, rely=0.5, relwidth=0.5)

ventana.mainloop()