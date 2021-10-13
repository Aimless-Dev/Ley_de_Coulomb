from math import inf
from ttkbootstrap import Style
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import backend

def Cargas(car):
    if car == 2:
        try:
            if pesoUno.get() != 0 and pesoDos.get() != 0 and posxUno.get() != 0 and posxDos.get() != 0 and posyUno.get() != 0 and posyDos.get() != 0:
                backend.peso.append(pesoUno.get())
                backend.peso.append(pesoDos.get())
                backend.x.append(posxUno.get())
                backend.y.append(posyUno.get())
                backend.x.append(posxDos.get())
                backend.y.append(posyDos.get())
                pesoUno.set(0)
                pesoDos.set(0)
                posxUno.set(0)
                posyUno.set(0)
                posxDos.set(0)
                posyDos.set(0)
                try:
                    messagebox.showinfo(message=backend.magnitudYvector(1, 0), title = 'Resultado')
                    #messagebox.showinfo(message=backend.magnitudYvector(0, 1), title = 'Resultado')
                except:
                    messagebox.showerror(message='Los campos no fueron llenados', title='ERROR!!!')
                backend.peso.clear()
                backend.x.clear()
                backend.y.clear()
                backend.V.clear()
                backend.fuerza.clear()
            else:
                messagebox.showerror(message='Favor de ingresar numeros mayores a 0', title='ERROR!!!')
        except:
            messagebox.showerror(message='No se admiten letras', title='ERROR!!!')

    elif car == 3:
        try:
            if pesoUno.get() != 0 and pesoDos.get() != 0 and pesoTres.get() != 0 and posxUno.get() != 0 and posxDos.get() != 0 and posxTres.get() != 0 and posyUno.get() != 0 and posyDos.get() != 0 and posyTres.get() != 0:
                backend.peso.append(pesoUno.get())
                backend.peso.append(pesoDos.get())
                backend.peso.append(pesoTres.get())
                backend.x.append(posxUno.get())
                backend.y.append(posyUno.get())
                backend.x.append(posxDos.get())
                backend.y.append(posyDos.get())
                backend.x.append(posxTres.get())
                backend.y.append(posyTres.get())
                pesoUno.set(0)
                pesoDos.set(0)
                pesoTres.set(0)
                posxUno.set(0)
                posyUno.set(0)
                posxDos.set(0)
                posyDos.set(0)
                posxTres.set(0)
                posyTres.set(0)
                try:
                    #messagebox.showinfo(message=backend.magnitudYvector(1, 0), title = 'Resultado')
                    messagebox.showinfo(message=backend.magnitudYvector(0, 1), title = 'Resultado')
                    messagebox.showinfo(message=backend.magnitudYvector(1, 2), title = 'Resultado')
                    #messagebox.showinfo(message=backend.magnitudYvector(2, 1), title = 'Resultado')
                    messagebox.showinfo(message=backend.magnitudYvector(0, 2), title = 'Resultado')
                    #messagebox.showinfo(message=backend.magnitudYvector(2, 0), title = 'Resultado')
                    # print(backend.FN)
                    backend.FF.append(backend.FN[0] + backend.FN[2] + backend.FN[4])
                    backend.FF.append(backend.FN[1] + backend.FN[3] + backend.FN[5])
                    # print(backend.FF)
                    messagebox.showinfo(message=f'Carga Neta: \n{backend.FF}', title='Carga Neta')
                except:
                    messagebox.showerror(message='Los campos no fueron llenados', title='ERROR!!!')
                backend.peso.clear()
                backend.x.clear()
                backend.y.clear()
                backend.V.clear()
                backend.fuerza.clear()
            else:
                messagebox.showerror(message='Favor de ingresar numeros mayores a 0', title='ERROR!!!')
        except:
            messagebox.showerror(message='No se admiten letras', title='ERROR!!!')
    else:
        messagebox.showerror(message='No hay datos', title='ERROR!!!')
    pesoUno.set(0)
    pesoDos.set(0)
    pesoTres.set(0)
    posxUno.set(0)
    posyUno.set(0)
    posxDos.set(0)
    posyDos.set(0)
    posxTres.set(0)
    posyTres.set(0)


def tresCargas():
    main.geometry('1170x220')
    title.config(width=90)
    backend.c = 3
    close.place(x=800, y=170)
    dos.place(x=400, y=170)
    submit.place(x=1000, y=170)
    
    

def salir():
    main.destroy()

def informacion():
    messagebox.showinfo(message='Desarrollado por: \nLibni Uziel Gabriel Linares \nIng. En Software \n4°A \nUPPE @ 2021', title='Desarrollador')

def dosCargas():
    main.geometry('770x220')
    backend.c = 2
    close.place(x=400, y=170)
    dos.place(x=800, y=170)
    submit.place(x=600, y=170)

style = Style(theme='sandstone')
main = style.master
pesoUno = IntVar()
pesoDos = IntVar()
pesoTres = IntVar()
posxUno = IntVar()
posyUno = IntVar()
posxDos = IntVar()
posyDos = IntVar()
posxTres = IntVar()
posyTres = IntVar()
x = 770
y = 220
main.geometry(f'{x}x{y}')
main.title('Ley de Coulomb')
main.resizable(0,0)
# main.iconbitmap('logo.ico')
title = ttk.Label(main, text='Calculadora de Ley de Coulomb', style='primary.Inverse.TLabel', width = 60, font=('Verdana',16))
title.place(x=0, y=0)
ttk.Label(main, text='MicroCoulombs: ', style='TLabel', width = 50, font=('Verdana',12)).place(x=10, y=50)
pes = ttk.Entry(main, textvariable=pesoUno)
pes.place(x=200, y=50)
ttk.Label(main, text='Posicion en X: ', style='TLabel', width = 50, font=('Verdana',12)).place(x=10, y=90)
px = ttk.Entry(main, textvariable=posxUno)
px.place(x=200, y=90)
ttk.Label(main, text='Posicion en Y: ', style='TLabel', width = 50, font=('Verdana',12)).place(x=10, y=130)
py = ttk.Entry(main, textvariable=posyUno)
py.place(x=200, y=130)

ttk.Label(main, text='MicroCoulombs:', style='TLabel', width = 50, font=('Verdana',12)).place(x=400, y=50)
peso2 = ttk.Entry(main, textvariable=pesoDos)
peso2.place(x=600, y=50)
ttk.Label(main, text='Posicion en X:', style='TLabel', width = 50, font=('Verdana',12)).place(x=400, y=90)
px2 = ttk.Entry(main, textvariable=posxDos)
px2.place(x=600, y=90)
ttk.Label(main, text='Posicion en Y:', style='TLabel', width = 50, font=('Verdana',12)).place(x=400, y=130)
py2 = ttk.Entry(main, textvariable=posyDos)
py2.place(x=600, y=130)

ttk.Label(main, text='MicroCoulombs:', style='TLabel', width = 50, font=('Verdana',12)).place(x=800, y=50)
peso3 = ttk.Entry(main, textvariable=pesoTres)
peso3.place(x=1000, y=50)
ttk.Label(main, text='Posicion en X:', style='TLabel', width = 50, font=('Verdana',12)).place(x=800, y=90)
px3 = ttk.Entry(main, textvariable=posxTres)
px3.place(x=1000, y=90)
ttk.Label(main, text='Posicion en Y:', style='TLabel', width = 50, font=('Verdana',12)).place(x=800, y=130)
py3 = ttk.Entry(main, textvariable=posyTres)
py3.place(x=1000, y=130)


submit = ttk.Button(main, text='Calcular',style='success.TButton', width=19, command=lambda: Cargas(backend.c))
submit.place(x=600, y=170)

close = ttk.Button(main, text='Cerrar', style='danger.TButton', width=19, command=salir)
close.place(x=400, y=170)

info = ttk.Button(main, text='info', style='info.TButton', width=19, command=informacion)
info.place(x=10, y=170)

tres = ttk.Button(main, text='3 cargas', style='secondary.TButton', width=19, command=tresCargas)
tres.place(x=200, y=170)

dos = ttk.Button(main, text='2 cargas', style='secondary.TButton', width=19, command=dosCargas)
dos.place(x=800, y=170)

main.mainloop()