import numpy as np
import scipy.linalg as lg
import scipy


class Lu:
    def __init__(self,matriz,matriz_coheficientes,resultados):
        #Asume que la matriz es nxn y de rango completo
        self.resultados = np.array(resultados)
        self.matriz_coheficientes = np.array(matriz_coheficientes)
        self.L =0
        self.U =0
        self.P = 0
        # print("primer")
        # print(self.matriz_coheficientes)
        # print("segundo")
        # print(self.matriz)
        # print("tercer")
        # print(self.resultados)
        
    

    def factorizacion(self):
        self.P,self.L,self.U = lg.lu(self.matriz_coheficientes)

       
    def resolver_sistema(self):
        self.factorizacion()
        resultados_permutados = np.dot(self.P, self.resultados)
        y = scipy.linalg.solve(self.L,resultados_permutados)
        # Resuelve Ux = y
        x = scipy.linalg.solve(self.U, y)

        return x




