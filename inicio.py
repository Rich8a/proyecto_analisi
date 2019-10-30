from tkinter import *
from tkinter import messagebox

raiz=Tk()
raiz.title("Nueva pestaña")
raiz.resizable(0,0)
raiz.geometry("700x450")
raiz.config(bg="#d5daff")
raiz.configure(cursor="trek")
raiz.iconbitmap()

def validar():
	if contraseña.get()=="Pelusa Caligari": 
		abrirventana2()
	else:
		contraseña.delete(0,END) 
		messagebox.showwarning("Advertencia.", "Contraseña incorrecta.") 

def abrirventana2():
	raiz.withdraw() 
	raiz2=Tk()
	raiz2.title("Nueva pestaña")
	raiz2.resizable(0,0)
	raiz2.geometry("700x450")
	raiz2.config(bg="#d5daff")
	raiz2.configure(cursor="trek") 
	raiz2.iconbitmap()

miFrame = Frame()
miFrame.pack(pady=30,ipadx=70,ipady=100)

Frame2 = Frame(miFrame)
Frame2.pack(side=TOP,padx=70)
 
img1=PhotoImage(file="imagen.gif")
etimg1=Label(Frame2, image=img1, ) 
etimg1.grid(row=0,column=0, sticky="e",pady=20)


Frame1 = Frame(miFrame)
Frame1.pack(side=BOTTOM,pady=35)

nombre=Entry(Frame1)
nombre.grid(row=0,column=1,sticky="e", padx=10, pady=11)
minombre = Label(Frame1,text="Nombre:")
minombre.grid(row=0,column=0,sticky="e", padx=10, pady=11)

correo = Entry(Frame1)
correo.grid(row=1,column=1,sticky="e", padx=10, pady=11)
micorreo = Label(Frame1,text="Correo:")
micorreo.grid(row=1,column=0,sticky="e", padx=10, pady=11)

contraseña = Entry(Frame1,)
contraseña.config(show="*")
contraseña.grid(row=2,column=1,sticky="e", padx=10, pady=11)
micontraseña = Label(Frame1, text="Contraseña:")
micontraseña.grid(row=2,column=0,sticky="e", padx=10, pady=11)

iniciar = Button(Frame1, text="Iniciar sesión.",command=validar, activebackground="#d5daff", activeforeground="white")
iniciar.grid(row=3, column=1)
h
raiz.mainloop()
