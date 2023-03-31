from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser

root=Tk()
root.title("Ejercicio A")
root.geometry("500x600")
ventanaPrincipal=Frame(root,width=1000,height=1000)
ventanaPrincipal.grid()


def color():
    res=(ColorRojo.get()+ColorVerde.get()+ColorAzul.get())
    rescolor=(len(res))

    if(rescolor==6): 
        ventanaPrincipal.config(bg=("#"+res))
        pass
    else:
         MessageBox.showwarning("Alerta","Limite de caracteres excedido")


Titulo=Label(ventanaPrincipal,
             text="CAMBIAR COLORES",font=("Times",14,"bold"),
             foreground="black", width=20,
             height=2, justify=CENTER,
             ).place(x=130,y=1)
letrasred=Label(ventanaPrincipal,
             text="Red", font=("Times",14,"bold"),
             foreground="red",
             width=8,
             height=2, 
             justify=CENTER,
             ).place(x=1,y=100)
ColorRojo=StringVar()
EntryRojo=Entry(ventanaPrincipal,font=("Times",12),textvariable=ColorRojo).place(x=160,y=110)
letrasgreen=Label(ventanaPrincipal,
             text="Green",
             font=("Times",14,"bold"),
             foreground="green", 
             width=8,
             height=2, 
             justify=CENTER,
             ).place(x=1,y=200)
ColorVerde=StringVar()
EntryVerde=Entry(ventanaPrincipal,font=("Times",12),textvariable=ColorVerde).place(x=160,y=210)
letrablue=Label(ventanaPrincipal,
             text="Blue",
             font=("Times",14,"bold"),
             foreground="blue",
             width=8,
             height=2, 
             justify=CENTER).place(x=1,y=300)
ColorAzul=StringVar()
EntryAzul=Entry(ventanaPrincipal,font=("Times",12),textvariable=ColorAzul).place(x=160,y=310)
ButtonRegistrar=Button(ventanaPrincipal,font=("Times",14,"bold"),text="Aplicar color",command=color).place(x=160,y=400)


root.mainloop()