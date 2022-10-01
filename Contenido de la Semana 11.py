import PIL 
from PIL import Image, ImageTk, ImageFilter
from tkinter import Tk, Button, Label, filedialog, messagebox

#se crea la funcion para cargar la imagen
def cargar():
    archivo = filedialog.askopenfilename()
    global imagen4
    imagen4 = Image.open(archivo)
    imagenresiz2 = imagen4.resize((400,200),Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(imagenresiz2)
    Label2.configure(image=render2)
    Label2.image = render2
    
    

    
#Se crea la funcion para el filtro blanco y negro
def Blanco_Negro():
    global image2
    image2 = imagen4.convert("L")
    imagenresiz2 = image2.resize((400,200),Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(imagenresiz2)
    Label2.configure(image=render2)
    Label2.image = render2
     
    
#Se crea la funcion para el filtro de desenfoque
def desenfoque():
    global image2
    #se aplica el filtro a la imagen
    image2= imagen4.filter(ImageFilter.BLUR)
    imagenresiz2 = image2.resize((400,200),Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(imagenresiz2)
    Label2.configure(image=render2)
    Label2.image = render2
    
#Se crea la funcion para el filtro de controrno
def controrno():
    global image2
    #se aplica el filtro a la imagen
    image2= imagen4.filter(ImageFilter.CONTOUR)
    imagenresiz2 = image2.resize((400,200),Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(imagenresiz2)
    Label2.configure(image=render2)
    Label2.image = render2
    
#Se crea la funcion para el filtro resaltar
def resaltar():
    global image2
    #se aplica el filtro a la imagen
    image2= imagen4.filter(ImageFilter.DETAIL)
    imagenresiz2 = image2.resize((400,200),Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(imagenresiz2)
    Label2.configure(image=render2)
    Label2.image = render2

#Se crea la funcion para guardar la imagen
def guardar():

    # se elige el nombre del archivo
    image2.save("guardar.jpg")
    # se crea un messagebox para informar que la imagen se a guardado
    messagebox.showinfo(title="Imagen Guardada",message="Se ha guardado la imagen")
    
ventana = Tk()
#se estable las dimension de la ventana
ventana.geometry("500x400")



#se define el titulo
ventana.title("Filtros de imagenes")
#se define el color
ventana.configure(bg='gray')
Label2 =Label(ventana, image="")
#se crean los botones
btnsape=Button(ventana, bg = "yellow",text="Cargar", command=cargar)
btn3=Button(ventana,bg = "yellow", text="Blanco/Negro", command=Blanco_Negro)
btn1=Button(ventana,bg = "yellow", text="Desenfoque", command=desenfoque)
btn2=Button(ventana,bg = "yellow", text="Controrno", command=controrno)
btn3_1=Button(ventana,bg = "yellow", text="Resaltar", command=resaltar)
btn_guardar=Button(ventana,bg = "red", text="Guardar Imagen", command=guardar)
btnsape.pack()
btn3.pack()
btn1.pack()
btn2.pack()
btn3_1.pack()
btn_guardar.pack()
Label2.pack()
ventana.mainloop()