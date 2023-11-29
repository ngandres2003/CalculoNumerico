class Matrices:
    def __init__(self,matriz_1,matriz_2):
        self.matriz_1 = matriz_1
        self.matriz_2 = matriz_2

    def comprobar(self):
        if len(self.matriz_1) == len(self.matriz_2):
            for x in range(len(self.matriz_1)):
                if len(self.matriz_1[x]) != len(self.matriz_2[x]):
                    return False
            return True
        
        elif len(self.matriz_1) != len(self.matriz_2):
            return False
        
        

    def suma(self):
        #Comprobamos que las 2 matrices se puedan sumar
        if self.comprobar() == True:
            matriz_sumada = []

            for x in range(len(self.matriz_1)):
                fila = []
                for y in range(len(self.matriz_2[x])):
                    resultado = self.matriz_1[x][y] + self.matriz_2[x][y]
                    fila.append(resultado)
                matriz_sumada.append(fila)
            print(matriz_sumada)
        else:
            print("Las matrices deben tener las mismas dimensiones")

        
        
