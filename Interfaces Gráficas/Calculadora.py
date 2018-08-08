from tkinter import *

raiz=Tk()

raiz.title("Calculadora")

miFrame=Frame(raiz)

miFrame.pack()

operacion=""

resultado=0


#-------------pantalla-----------------

numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="black", fg="#03f943", justify="right")

#--------------------Pulsaciones teclado-------------------

def numeroPulsado(num):

	global operacion

	if operacion!="":

		numeroPantalla.set(num)

		operacion=""

	else:

		numeroPantalla.set(numeroPantalla.get() + num)



#-----------------------funcion suma------------------------

def suma(num):

	global operacion

	global resultado

	resultado+=int(num)#resultado=resultado+int(num)

	operacion="suma"

	numeroPantalla.set(resultado)



#----------------------funcion el_resultado--------------------

def el_resultado():

	global resultado


	numeroPantalla.set(resultado+int(numeroPantalla.get()))

#---------------------------fila 1-----------------------------

boton7=Button(miFrame, text="7", width=6, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=6, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=6, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDivi=Button(miFrame, text="/", width=6)
botonDivi.grid(row=2, column=4)

#------------------fila 2----------------------

boton4=Button(miFrame, text="4", width=6, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width=6, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=6, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMulti=Button(miFrame, text="*", width=6)
botonMulti.grid(row=3, column=4)

#------------------fila 3----------------------

boton1=Button(miFrame, text="1", width=6, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=6,command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width=6, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest=Button(miFrame, text="-", width=6)
botonRest.grid(row=4, column=4)

#------------------fila 4----------------------
botonComa=Button(miFrame, text=",", width=6, command=lambda:numeroPulsado(","))
botonComa.grid(row=5, column=1)
botonZero=Button(miFrame, text="0", width=6, command=lambda:numeroPulsado("0"))
botonZero.grid(row=5, column=2)
botonIgual=Button(miFrame, text="=", width=6, command=lambda:el_resultado())
botonIgual.grid(row=5, column=3)
botonSum=Button(miFrame, text="+", width=6, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)



raiz.mainloop()