import tkinter as tk

ventana = tk.Tk()
ventana.title("Netflix")
ventana.geometry("250x400")
ventana.resizable(False,False)

etiqueta = tk.Label(ventana,text="ingresa nombre de usuario")
etiqueta.pack()
ingreso_usuario = tk.Entry(ventana)
ingreso_usuario.pack()

etiqueta = tk.Label(ventana,text="ingresa conteraseña")
etiqueta.pack()
ingreso_contrasenia = tk.Entry(ventana)
ingreso_contrasenia.pack()

usuario_correcto = "mati123"
contrasenia_correcta = "2468"

def iniciar_sesion ():
    usuario = ingreso_usuario.get()
    contrasenia = ingreso_contrasenia.get()

    if usuario == usuario_correcto and contrasenia == contrasenia_correcta:
        mensajeBienvenida.config(text=f"inicio sesion exitosamente")
    else:
        mensajeBienvenida.config(text=f"acceso denegado")

mensajeBienvenida = tk.Label(ventana) 
mensajeBienvenida.pack()

boton = tk.Button(ventana,text="ingresar",command=iniciar_sesion,bg="green")
boton.pack()

ventana.mainloop()