def verificarTransformacion(n,base_inicial):
    #opciones = {"1":"Decimal","2":"Binario","3":"Octal","4":"Hexadecimal"}

    if base_inicial == "1":
        try:
            n = int(n)
            return True
        except:
            return False
        
        
    elif base_inicial == "2":
        validos = ["1","0"]

        for x in n:
            if x not in validos:
                return False
        return True
    
    elif base_inicial == "3":
        validos = ["0","1","2","3","4","5","6","7"]
        for x in n:
            if x not in validos:
                return False
        return True
    
    elif base_inicial == "4":
        validos = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        n = n.upper()
        for x in n:
            if x not in validos:
                return False
        return True
        



