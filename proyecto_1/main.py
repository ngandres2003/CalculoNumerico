from menu import menu,menu_transformacion
from verificar import verificarTransformacion
from transformaciones import Transformaciones
from lu import Lu

while True:
    x = menu()
    if x[0] == "1":
        numero = x[1][2]
        base_inicial = x[1][0]
        base_convertir = x[1][1]

        if verificarTransformacion(numero,base_inicial) == True:
            t = Transformaciones(numero,base_inicial,base_convertir)
            t.transformar()
            
            
        else:
            print("Error de numeros")


    elif x[0] == "2":
        matriz_coheficientes = x[1][0]
        resultados = x[1][1]
        l = Lu(matriz_coheficientes,resultados)
        print(l.resolver_sistema())
        
        

        
    elif x[0] =="3":
        print("Has salido del programa")
        break
    
    

