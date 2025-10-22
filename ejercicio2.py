import tkinter as tk

ventana = tk.Tk()
ventana.title("Netflix")
ventana.geometry("250x400")
ventana.resizable(False,False)

frame1 = tk.Frame(ventana,bg="violet",width= 300 ,height=500,bd=5 ,relief="ridge")
frame1.pack()

etiqueta = tk.Label(frame1,text="ingresa nombre de usuario",bg="yellow")
etiqueta.pack(pady=10)
ingreso_usuario = tk.Entry(frame1)
ingreso_usuario.pack()

etiqueta = tk.Label(frame1,text="ingresa conteraseña",bg="yellow")
etiqueta.pack(pady=10)
ingreso_contrasenia = tk.Entry(frame1)
ingreso_contrasenia.pack(pady=10)

usuario_correcto = "mati123"
contrasenia_correcta = "2468"

def iniciar_sesion ():
    usuario = ingreso_usuario.get()
    contrasenia = ingreso_contrasenia.get()

    if usuario == usuario_correcto and contrasenia == contrasenia_correcta:
        mensajeBienvenida.config(text=f"inicio sesion exitosamente")
    else:
        mensajeBienvenida.config(text=f"acceso denegado")

mensajeBienvenida = tk.Label(frame1) 
mensajeBienvenida.pack()

boton = tk.Button(ventana,text="ingresar",command=iniciar_sesion,bg="green")
boton.pack()

frame1.mainloop()