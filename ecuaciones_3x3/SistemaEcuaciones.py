import numpy as np
import matplotlib.pyplot as plt

class SistemaEcuaciones:
    def __init__(self,sistema_ecuaciones):
        self.a = sistema_ecuaciones
        self.b = self.formatear()
    
    def formatear(self):#Retorna los terminos independientes y los elimina de a
        terminos_independientes = []
        for x in self.a:
            terminos_independientes.append(x.pop())
        return terminos_independientes
    
    def resolver_sistema_ecuaciones(self):#Resolvemos sistema de ecuaciones 3x3
        a = np.array(self.a)
        b = np.array(self.b)
        x = np.linalg.solve(a, b)
        z = 0
        y1 = (1 + 2*x - 9*z)/5
        y2 = 6 - 7*x - z
        print(y1,y2)
        self.grafica(x,y1,y2)
        
        
    
    def grafica(self,x,y1,y2):
        fig, ax = plt.subplots()
        ax.plot(x, y1, label='y1=(1 + 2*x - 9*z) / 5')
        ax.plot(x, y2, label='y2=(6 - 7*x - z)')
        plt.legend()
        plt.grid(ls="--", color="black")
        plt.show()
    
   
            
    
    
    def __str__(self):
        return f'a: {self.a}, b:{self.b}'
    

