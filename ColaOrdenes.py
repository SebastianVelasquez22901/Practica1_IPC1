from audioop import reverse
from turtle import color
from graphviz import Digraph
from re import subn


class ColaOrdenes:

    def __init__(self):
        self.datos = []
        self.tiempos = []
    def cantidad(self):
        return len(self.datos)
    
    def insertar(self, dato):
        tiempo = 0
        if dato.lower() == 'pepperoni':
            ingrediente =  dato.lower()
            tiempo += 3
            self.datos.insert(0, ingrediente)
            self.tiempos.insert(0, tiempo)
            
        elif dato.lower() == 'salchicha':
            ingrediente =  dato.lower()
            tiempo += 4
            print("Gracias por generar su orden: "+ " Nombre del ingrediente agregado -> "+ ingrediente)
            print("Tiempo de espera -> " + str(tiempo))
            self.datos.insert(0, ingrediente)
            self.tiempos.insert(0, tiempo)
        
        elif dato.lower() == 'carne':
            ingrediente =  dato.lower()
            tiempo += 10
            print("Gracias por generar su orden: "+ " Nombre del ingrediente agregado -> "+ ingrediente)
            print("Tiempo de espera -> " + str(tiempo))
            self.datos.insert(0, ingrediente)
            self.tiempos.insert(0, tiempo)
        
        elif dato.lower() == 'queso':
            ingrediente =  dato.lower()
            tiempo += 5
            print("Gracias por generar su orden: "+ " Nombre del ingrediente agregado -> "+ ingrediente)
            print("Tiempo de espera -> " + str(tiempo))
            self.datos.insert(0, ingrediente)
            self.tiempos.insert(0, tiempo)
            
        elif dato.lower() == 'piña':
            ingrediente =  dato.lower()
            tiempo += 2
            print("Gracias por generar su orden: "+ " Nombre del ingrediente agregado -> "+ ingrediente)
            print("Tiempo de espera -> " + str(tiempo))
            self.datos.insert(0, ingrediente)
            self.tiempos.insert(0, tiempo)
            
        else: 
            print("Disculpe el ingrediente -> " + dato + " no se encuentra en nuestro menu" )
            
    
    
    def primer_dato(self):
        if self.cantidad():
            print("Su tiempo: -->"+ str(self.tiempos[-1]))
            print("Primera orden: -->")
            return  self.datos[-1]
    
    def ultimo_dato(self):
        if self.cantidad():
            print("Su tiempo: -->"+ str(self.tiempos[0]))
            print("Ultima orden: -->")
            return self.datos[0]
    
    def graficarLista(self):
        dot = Digraph(
        name='Graphtest',
        comment='Orden para el consumidor',
        filename='ordenes',
        directory=None,
        format="svg",
        engine=None,
        encoding='utf8',
        graph_attr={'rankdir':'TB'},
        node_attr={'color':'black','fontcolor':'black','fontname':"arial",'fontsize':'15','style':'rounded','shape':'box'},
        edge_attr={'color':'#999999','fontcolor':'#888888','fontsize':'15'},
        body=None,
        strict=False)
        for i in range(self.cantidad()):
            if i != self.cantidad():
                dot.node('Orden'+ str(i),self.datos[i])    
                dot.node('Tiempo'+ str(i), str(self.tiempos[i]))
            else: 
                pass
        dot.view()
