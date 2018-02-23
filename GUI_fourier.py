import numpy as np
import scipy.integrate as integrate
import signals as sig
import coeff_fourier as cf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler #Gestion de matplotlib dans Tk
from matplotlib.figure import Figure
from tkinter import *


################

def frequency_value(event):
    redraw()
        
def draw_coeff():
    global n
    nu = frequency_slider.get()
    c = v.get()
    graph_f2.clear()
    if c ==1:##Dent de scie
        function2=[0]*len(t)
        for i in range(1,n):
            function2 =   function2 + np.sin(2*np.pi*nu*t*i)*cf.coeff_sawtooth(i)
    elif c==2: ##Créneau
        function2=[1]*len(t)
        for i in range(0,n):
            function2 =   function2 + np.sin((2*i+1)*2*np.pi*nu*t)*cf.coeff_square(i)
    else:
        function2=[0]*len(t)
        for i in range(0,n):
            function2 =   function2 + np.sin((2*i+1)*2*np.pi*nu*t)*cf.coeff_triangle(i)
    graph_f2.set_title("Décomposition en série de Fourier:")
    graph_f2.plot(t, function2)
    fig2.draw()
    print(n)
    """
    try:
        n_coeff(text=str(n))
    except UnboundLocalError:
        n_coeff=Label(text=str(n))
        n_coeff.pack(side=RIGHT)
    """
    n = n + 1
        
def redraw():
    global n
    n = 0 
    c = v.get()
    nu = frequency_slider.get()
    print(c)
    if c==1:
        f = sig.sawtooth
    elif c==2:
        f = sig.square
    else:
        f = sig.triangle
    graph_f.clear()
    function = [f(1/nu,e) for e in t]
    graph_f.set_title("Fonction:")
    graph_f.plot(t, function)
    fig1.draw()
    
################

master = Tk()

#Slider de Frequence
frequency_slider = Scale(master, from_=1, to=200, command=frequency_value, length=600,label = "Fréquence")
frequency_slider.pack(side=RIGHT)
frequency_slider.bind("<ButtonRelease-1>",frequency_value)
#Dessin du premier canvas
graph_function = Figure(figsize=(1,1), dpi=50)
graph_f = graph_function.add_subplot(111)
graph_f.set_title("Fonction:")
t = np.arange(-2,2,0.01)
function = [sig.sawtooth(1,e) for e in t]
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
function2 = [0]*len(t)
n = 1
graph_f2.plot(t, function2)

fig2 = FigureCanvasTkAgg(graph_function2,master=master)
fig2.show()
fig2.get_tk_widget().pack( fill=BOTH,expand = 1)
toolbar2 = NavigationToolbar2TkAgg(fig2,master)
toolbar2.update()
fig2._tkcanvas.pack(side=BOTTOM, fill=BOTH, expand=1)

add_coeff = Button(cadre,text="Ajouter un coefficient")
add_coeff.bind('<Button-1>',lambda x:draw_coeff())
add_coeff.pack(side=RIGHT)
cadre.pack(side = BOTTOM)




################
master.title("Série de Fourier")
master.minsize(width=1000, height = 600)
#master.maxsize(width=1100,height=650)
master.mainloop()
