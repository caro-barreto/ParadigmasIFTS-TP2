import operator
from tkinter import *
import random
from tkinter import messagebox
from openpyxl import Workbook
from operator import itemgetter


#configuracion de la raiz
root= Tk()
root.config(width=360, height=380, bg="peach puff")
root.title('Ingreso de participantes')

datos = []
def guardar():

    id = random.randint(1, 998)
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()
    genero = seleccionar()
    disparo1 = int(entry_disparo1.get())
    disparo2 = int(entry_disparo2.get())
    disparo3 = int(entry_disparo3.get())

    if disparo1 < disparo2 and disparo1 < disparo3:
        mejordisparo = disparo1
    elif disparo2 < disparo1 and disparo2 < disparo3:
        mejordisparo = disparo2
    else:
        mejordisparo = disparo3

    participante = [id, nombre, apellido, edad, genero, disparo1, disparo2, disparo3, mejordisparo]

    datos.append(participante)
    borrar()
    print(datos)



def borrar():
    entry_edad.delete(0, 'end')
    entry_nombre.delete(0, 'end')
    entry_disparo3.delete(0, 'end')
    entry_disparo2.delete(0, 'end')
    entry_disparo1.delete(0, 'end')
    entry_apellido.delete(0, 'end')

def exportar():

    workbook = Workbook()
    sheet = workbook.active

    headers = ['ID', 'Nombre', 'Apellido', 'Edad', 'Genero 1=F 2=M', 'Disparo1', 'Disparo2', 'Disparo3', 'Mejor disparo']
    sheet.append(headers)
    for participante in datos:
        sheet.append(participante)

    workbook.save(filename= 'Registro de participantes.xlsx')

    borrar()


def mostrar_ganador():
    mejores = sorted(datos, key=operator.itemgetter(-1))
    print(mejores)
    ganador = mejores[0]
    messagebox.showinfo('Ganador', ganador)

label_nombre = Label(root, text="Nombre", font="Candara 10", bg="peach puff")
label_nombre.place(x=20, y=25)

entry_nombre = Entry(root, width=35)
entry_nombre.place(x=100, y=25)

label_2 = Label(root, text="Apellido", font="Candara 10", bg="peach puff")
label_2.place(x=20, y=65)

entry_apellido = Entry(root, width=35)
entry_apellido.place(x=100, y=65)

label_edad = Label(root, text="Edad", font="Candara 10", bg="peach puff")
label_edad.place(x=20, y=105)

entry_edad = Entry(root, width=35)
entry_edad.place(x=100, y=105)

def seleccionar():
    return genero.get()

genero = IntVar()

rb_1 = Radiobutton(root, text="Femenino", value=1, command=seleccionar, variable=genero, bg="peach puff")
rb_1.place(x=20, y=145)

rb_2 = Radiobutton(root, text="Masculino", value=2, command=seleccionar, variable=genero, bg="peach puff")
rb_2.place(x=120, y=145)

label_disparo1 = Label(root, text="Disparo 1", font="Candara 10", bg="peach puff")
label_disparo1.place(x=20, y=185)

entry_disparo1 = Entry(root, width=35)
entry_disparo1.place(x=100, y=185)

label_disparo2 = Label(root, text="Disparo 2", font="Candara 10", bg="peach puff")
label_disparo2.place(x=20, y=225)

entry_disparo2 = Entry(root, width=35)
entry_disparo2.place(x=100, y=225)

label_disparo3 = Label(root, text="Disparo 2", font="Candara 10", bg="peach puff")
label_disparo3.place(x=20, y=265)

entry_disparo3 = Entry(root, width=35)
entry_disparo3.place(x=100, y=265)

button_guardar = Button(root, text="Guardar", command=guardar, font="Candara 8")
button_guardar.place(x=50, y=305)

button_ganador = Button(root, text="Ganador", font="Candara 8", command=mostrar_ganador)
button_ganador.place(x=130, y=305)

button_exportar = Button(root, text="Exportar .xlsx", font="Candara 8", command=exportar)
button_exportar.place(x=210, y=305)




root.mainloop()