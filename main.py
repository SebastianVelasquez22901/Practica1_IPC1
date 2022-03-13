from tkinter import *
from PIL import Image, ImageTk
import xml.etree.ElementTree as ET
from tkinter import *
from PIL import Image, ImageTk,Image
from tkinter import messagebox
from ColaOrdenes import ColaOrdenes

orden = ColaOrdenes()

ventana=Tk()
ventana.geometry('900x500')
ventana.configure(bg='orange')
ventana.resizable(0,0)
ventana.title('Menu para pizzeria Pizza de Don Cangrejo')


l1=Label(ventana,text='Pizza de Don Cangrejo',fg='white',bg='orange')
l1.config(font=('Times new roman',60))
l1.pack(expand=True)

def Ordenes():
    ordenes = 'si'
    while ordenes != 'no':
        if ordenes == 'si':
            OrdenTemporal = input("Ingrese por favor el ingrediente para su pizza: ")
            orden.insertar(OrdenTemporal)
            OrdenTemporal = ''
            ordenes = input("Desdea Ordenar una pizza nueva? "+ "Por favor conteste si o no ->  ").lower()
        
        else:
            print("Le pido por favor que colabore en ingresar las opciones validas gracias")
            ordenes = input("Desdea Ordenar una pizza nueva? "+ "Por favor conteste si o no ->  ").lower()
            
    
    
    


def Interfaz():
    f1=Frame(ventana,width=300,height=500,bg='#FDDF7E')
    f1.place(x=0,y=0)
    
    def VerOrdenes():
        print("--------Primera orden--------")
        print(orden.primer_dato()) 

        print("--------Ultima orden--------")
        print(orden.ultimo_dato())
        
        print("--------Cantidad de ordenes--------")
        print(orden.cantidad())
    
    def Graficar():
        orden.graficarLista()

    def Salida():
        respuesta = messagebox.askyesno("Salir", "¿Desea salir del programa?")
        if (respuesta): 
            ventana.destroy()

    #buttons
    def boton(x,y,text,bcolor,fcolor,cmd):
     
        def on_entera(e):
            myButton1['background'] = bcolor #ffcc66
            myButton1['foreground']= '#FDDF7E'  #000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground']= 'black'

        myButton1 = Button(f1,text=text,
                       width=42,
                       height=2,
                       fg='white',
                       border=0,
                       bg=fcolor,
                       activeforeground='white',
                       activebackground=bcolor,            
                        command=cmd)
                      
        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x,y=y)

    boton(0,80,'Generar mi orden','#0f9d9a','#F7BD56', Ordenes)
    boton(0,117,'Ver primera y ultima orden','#0f9d9a','#F7BD56', VerOrdenes)
    boton(0,154,'Generar orden para ver','#0f9d9a','#F7BD56',Graficar)
    boton(0,191,'Salida','#0f9d9a','#F7BD56', Salida)

    #
    def dele():
        f1.destroy()

    global img2
    img2 = ImageTk.PhotoImage(Image.open("close.png"))

    Button(f1,
           image=img2,
           border=0,
           command=dele,
           bg='#12c4c0',
           activebackground='#12c4c0').place(x=5,y=10)
    
    
img1 = ImageTk.PhotoImage(Image.open("pizza.jpg"))

Button(ventana,image=img1,
       command=Interfaz,
       border=0,
       bg='white',
       activebackground='white').place(x=5,y=10)


ventana.mainloop()
