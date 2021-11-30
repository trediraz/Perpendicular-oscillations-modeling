import matplotlib as plt
import matplotlib.pyplot as pl
import numpy as np
import matplotlib.animation as animation
import tkinter
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

z = 5

root = tkinter.Tk()
root.wm_title("Test")
t = np.arange(0,100,0.01)
x= np.sin(t)
y = np.sin(t)
fig = Figure(figsize=(5,4),dpi=100)
fig2 = Figure(figsize=(5,4),dpi =100)
ax = fig.add_subplot(111)
line, = ax.plot(x,y,'g-')

#komentarz komentarz1111111111111111111111111111111111111111111
canvas = FigureCanvasTkAgg(fig,master = root)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=1)

def animate(i):
    line2.set_ydata(np.sin(x2+i/z))
    return line2,

#komenatarz komentarz 11111111111111111111111111111111111111111
canvas2 = FigureCanvasTkAgg(fig2,master = root)
canvas2.get_tk_widget().pack(side=tkinter.BOTTOM)

ax2 = fig2.add_subplot(111)
x2 = np.arange(0,2*np.pi,0.01)
line2,= ax2.plot(x2,np.sin(x2))
a = animation.FuncAnimation(fig2,animate,np.arange(1,200),interval = 25,blit=False)


def on_key_press(event):
    print(f'Pressed {event.key}')
    updateGraph(event.key)
    z+=int(event.key)
    plt.backend_bases.key_press_handler(event,canvas,canvas2)

canvas.mpl_connect("key_press_event",on_key_press)
canvas2.mpl_connect("key_press_event",on_key_press)

def _quit():
    root.quit()
    root.destroy()

def updateGraph(n):
    line.set_ydata(np.sin(int(n)*t))
    fig.canvas.draw()
    fig.canvas.flush_events()

button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()

#TEST GITA
