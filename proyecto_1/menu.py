def menu():
    while True:
        print("")
        print('''Elige una opcion:
            1.Transformacion entre sistema numericos
            2.Resolucion de sistema de ecuaciones
            3.Salir''')
        opcion = input("->")

        if opcion == "1":
           return "1",menu_transformacion()
        elif opcion =="2":
            return "2",menuLu()
        elif opcion == "3":
            return "3"
        else:
            print('Selecciona una opcion valida')



def menu_transformacion():
    while True:
        x = ["1","2","3","4"]

        print("")
        print("""Elige sistema numerico a ingresar
              1.Decimal
              2.Binario
              3.Octal
              4.Hexadecimal""")
        opcion_ingresar = input("->")
        if opcion_ingresar in x:

            numero = input("Ingrese el numero en la base numerica seleccionada: ")
            numero = numero.upper()


            print("")
            print("""Elige sistema numerico a convertir
              1.Decimal
              2.Binario
              3.Octal
              4.Hexadecimal""")
            opcion_convertir = input("->")

        

            if opcion_ingresar == opcion_convertir:
                print("No puedes convertir en la misma base numerica")
            elif opcion_convertir in x:
                return opcion_ingresar,opcion_convertir,numero
        
            else:
                print('Ingresa un sistema numerico valido')
        else:
            print("Selecciona una sistema numerico valido")
    

def menuLu():
    while True:
        print("Ingresa la dimension nxn de tu matriz: ")
        try:
            n = int(input("n-> "))
            matriz = []
            resultados = []
            for x in range(n):
                aux = []
                for y in range(n):
                    elemento = int(input(f'Ingresa [{x}][{y}]: '))
                    aux.append(elemento)
                matriz.append(aux)
            print("Ingresa los resultados: ")
            for x in range(n):
                r = int(input(f"Ingresa resultado[{x}]: "))
                resultados.append(r)


            
            return matriz,resultados

        except:
            print("Solo numeros admitidos")
            

            












                