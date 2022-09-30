from PIL import Image, ImageTk, ImageFilter 
from tkinter import Place, Tk, Button, Label, filedialog,messagebox


def cargar():
    archivo = filedialog.askopenfilename()
    global imagen4
    imagen4 = Image.open(archivo)
    imagenresiz2 = imagen4.resize((400,200),Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(imagenresiz2)
    Label2.configure(image=render2)
    Label2.image = render2
    
    

    

def Blanco_Negro():
    global image2
    image2 = imagen4.convert("L")
    imagenresiz2 = image2.resize((400,200),Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(imagenresiz2)
    Label2.configure(image=render2)
    Label2.image = render2
     
    

def desenfoque():
    global image2
    image2= imagen4.filter(ImageFilter.BLUR)
    imagenresiz2 = image2.resize((400,200),Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(imagenresiz2)
    Label2.configure(image=render2)
    Label2.image = render2
    

def controrno():
    global image2
    image2= imagen4.filter(ImageFilter.CONTOUR)
    imagenresiz2 = image2.resize((400,200),Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(imagenresiz2)
    Label2.configure(image=render2)
    Label2.image = render2
    

def resaltar():
    global image2
    image2= imagen4.filter(ImageFilter.DETAIL)
    imagenresiz2 = image2.resize((400,200),Image.Resampling.LANCZOS)
    render2 = ImageTk.PhotoImage(imagenresiz2)
    Label2.configure(image=render2)
    Label2.image = render2

def guardar():
 
    image2.save("guardar.jpg")
    messagebox.showinfo(title="Imagen Guardada",message="Se ha guardado la imagen")
    
ventana = Tk()
ventana.geometry("500x400")




ventana.title("Filtros de imagenes")
ventana.configure(bg='gray')
Label2 =Label(ventana, image="")
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