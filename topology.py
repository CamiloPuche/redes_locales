from mininet.topo import Topo
from tkinter import *
#from tkinter import messagebox
from tkinter.simpledialog import askinteger, askstring

class MyTopo(Topo):
    "Simple topology example."


    def __init__(self):

        
        "create custom topo."
        Topo.__init__(self)
        root = Tk()
        s = []
        h = []

        switches = askinteger('input',"¿Cuantos Switches?")
        Host = askinteger('input',"¿Cuantos Host?")
        print(Host)
        print(switches)

        for m in range(int(Host)):
            h.append(self.addHost('h' + str((m))))

        
        for m in range(int(switches)):
            s.append(self.addSwitch('s' + str((m))))       
        
        while True:
            print("switches")
            print(s)
            print('Host')
            print(h)
            
            e_host = askstring('input',"Quiere agregar enlace para un host(h) o entre switches(s): ").lower()

            if e_host == 'h':
                i = askinteger('input',"numero del host que quieres conectar: ")
                j = askinteger('input',"numero del switche con el que quiere conectar: ")
                self.addLink(h[int(i)],s[int(j)])
            if e_host == 's':
                i = askinteger('input',"numero del switche que quiere conectar: ")
                j = askinteger('input',"numero del switche con el que quiere conectar: ")
                self.addLink(s[int(i)],s[int(j)])
            word = askstring('input',"¿Quieres seguir agregando enlaces?  No(n)/ Si(s)" ).lower()
            if word == 'n':
                break
        root.destroy()
        root.mainloop()

topos = {'mytopo': (lambda:MyTopo())}
