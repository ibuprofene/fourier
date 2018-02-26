import numpy as np
from door import door
import scipy.integrate as integrate
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler #Gestion de matplotlib dans Tk
from matplotlib.figure import Figure
from tkinter import *


################

def scale_value(event):
    redraw()

def fourier_transform(f):
    if f!=0:
        T = scale_slider.get()
        return np.sin(np.pi*f*T)/(np.pi*f)
    else:
        return T
        
def redraw():
    c = v.get()
    l = scale_slider.get()
    graph_f.clear()
    function = [door(l,e) for e in t]
    graph_f.set_title("Fonction:")
    graph_f.plot(t, function)
    fig1.draw()
    graph_f2.clear()
    function2 = [fourier_transform(f) for f in t]
    graph_f2.plot(t,function2)
    fig2.draw()
    
################

master = Tk()

#Slider de Frequence
scale_slider = Scale(master, from_=1, to=16, command=scale_value, length=600,label = "Largeur de la porte")
scale_slider.pack(side=RIGHT)
scale_slider.bind("<ButtonRelease-1>",scale_value)

#Dessin du premier canvas
graph_function = Figure(figsize=(1,1), dpi=50)
graph_f = graph_function.add_subplot(111)
graph_f.set_title("Fonction:")
t = np.arange(-10,10,0.01)
function = [door(1,e) for e in t]
graph_f.plot(t, function)
fig1 = FigureCanvasTkAgg(graph_function,master=master)
fig1.show()
fig1.get_tk_widget().pack(side=TOP, fill=BOTH,expand = 1)

toolbar1 = NavigationToolbar2TkAgg(fig1,master)
toolbar1.update()
fig1._tkcanvas.pack(side=TOP,fill=BOTH, expand=1)

cadre = Frame(master)
#Choix de la fonction
available_functions = [("Dent de scie",1),("Créneau",2),("Triangle",3)]
v = IntVar()
v.set(1)

for function, k in available_functions:
    b = Radiobutton(cadre, text=function, variable=v, value=k,borderwidth = 2,command=redraw)
    b.pack(side=LEFT)

graph_function2 = Figure(figsize=(1,1), dpi=50)
graph_f2 = graph_function2.add_subplot(111)
graph_f2.set_title("Décomposition en série de Fourier:")
function2 = [fourier_transform(f) for f in t]
graph_f2.plot(t, function2)

fig2 = FigureCanvasTkAgg(graph_function2,master=master)
fig2.show()
fig2.get_tk_widget().pack( fill=BOTH,expand = 1)
toolbar2 = NavigationToolbar2TkAgg(fig2,master)
toolbar2.update()
fig2._tkcanvas.pack(side=BOTTOM, fill=BOTH, expand=1)

add_coeff = Button(cadre,text="Ajouter un coefficient")
add_coeff.bind('<Button-1>',print("r"))
add_coeff.pack(side=RIGHT)
cadre.pack(side = BOTTOM)

master.title("Série de Fourier")
master.minsize(width=1000, height = 600)
#master.maxsize(width=1100,height=650)
master.mainloop()
