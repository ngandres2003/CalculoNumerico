class Transformaciones:
    opciones = {"1":"Decimal","2":"Binario","3":"Octal","4":"Hexadecimal"}
    def __init__(self,n,base_inicial,base_convertir):
        self.n = n
        self.base_inicial = base_inicial
        self.base_convertir = base_convertir

    def transformar(self):
        if self.base_inicial == "1" and self.base_convertir == "2":
            print(f"Decimal: {self.n}, Binario: {self.decimal_a_binario()}")
        elif self.base_inicial == "1" and self.base_convertir == "3":
            print(f"Decimal: {self.n}, Octal: {self.decimal_a_octal()}")
        elif self.base_inicial == "1" and self.base_convertir == "4":
            print(f"Decimal: {self.n}, Hexadecimal: {self.decimal_a_hexadecimal()}")  
        elif self.base_inicial == "2" and self.base_convertir== "1":
            print(f"Binario: {self.n}, Decimal{self.binario_a_decimal()}")
        elif self.base_inicial == "3" and self.base_convertir == "1":
            print(f"Octal: {self.n}, Decimal: {self.octal_a_decimal()}")
        elif self.base_inicial == "4" and self.base_convertir == "1":
            print(f"Hexadecimal: {self.n}, Decimal: self.hexadecimal_a_decimal()")
        elif self.base_inicial == "2" and self.base_convertir == "3":
            print(f"Binario: {self.n}, Octal: {self.binario_a_octal()}")
        elif self.base_inicial == "2" and self.base_convertir == "4":
            print(f"Binario: {self.n}, Hexadecimal: {self.binario_a_hexadecimal()}")
        elif self.base_inicial == "3" and self.base_convertir == "2":
            print(f"Octal: {self.n}, Binario: {self.octal_a_binario()}")
        elif self.base_inicial == "3" and self.base_convertir == "4":
            print(f"Octal: {self.n}, Hexadecimal: {self.octal_a_hexadecimal()}")
        elif self.base_inicial == "4" and self.base_convertir == "2":
            print(f"Hexadecimal: {self.n}, Binario: {self.hexadecimal_a_binario()}")
        elif self.base_inicial == "4" and self.base_convertir == "3":
            print(f"Hexadecimal: {self.n}, Octal: {self.hexadecimal_a_octal()}")
        
    def decimal_a_binario(self):
        self.n = int(self.n)
        binario = ""

        if self.n == 0:
            return 0
       
        
        while self.n > 0:
        
            residuo = int(self.n % 2)
            self.n = int(self.n / 2)
        
            binario = str(residuo) + binario
        return binario
    
    def decimal_a_octal(self):

        self.n  = int(self.n)
        octal = ""

        if self.n <=0:
            return 0
        
        while self.n > 0:
            residuo = int(self.n % 8)
            self.n = int(self.n/8)
            octal = str(residuo) + octal
        return octal

    def decimal_a_hexadecimal(self):
        hexadecimal_conversion = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}
        self.n = int(self.n)
        hexadecimal = ""
        
        if self.n == 0:
            return 0
        
        while self.n > 0:
            residuo = int(self.n%16)
            self.n = int(self.n/16)
            hexadecimal = str(hexadecimal_conversion[residuo] + hexadecimal)
        return hexadecimal

    def binario_a_decimal(self):
        decimal = 0
        i = 0
        self.n = int(self.n)
        while(self.n != 0):
            residuo = self.n % 10
            self.n = self.n//10
            decimal = decimal + residuo * pow(2, i)
            i += 1
        return decimal

    def octal_a_decimal(self):
        decimal = 0
        i = 0
        self.n = int(self.n)

        while (self.n != 0):
            residuo = self.n % 10
            self.n = self.n//10
            decimal = decimal + residuo * pow(8,i)
            i +=1
        return decimal

    def hexadecimal_a_decimal(self):
        hexadecimal_conversion = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                                   '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
                                   'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

        decimal = 0
        i = 0

        while(len(self.n) > 0):
            residuo = hexadecimal_conversion[self.n[-1:]]
            self.n = self.n[:-1]
            decimal = decimal + residuo * pow(16,i)
            i +=1


        return decimal

    def binario_a_octal(self):
        self.n = self.binario_a_decimal()
        octal = self.decimal_a_octal()
        return octal

    def binario_a_hexadecimal(self):
        self.n = self.binario_a_decimal()
        hexadecimal = self.decimal_a_hexadecimal()
        return hexadecimal
    
    def octal_a_binario(self):
        self.n = self.octal_a_decimal()
        binario = self.decimal_a_binario()
        return binario
    
    def octal_a_hexadecimal(self):
        self.n = self.octal_a_decimal()
        hexadecimal = self.decimal_a_hexadecimal()
        return hexadecimal
    
    def hexadecimal_a_binario(self):
        self.n = self.hexadecimal_a_decimal()
        binario = self.decimal_a_binario()
        return binario
    
    def hexadecimal_a_octal(self):
        self.n = self.hexadecimal_a_decimal()
        octal = self.decimal_a_octal()
        return octal

        
