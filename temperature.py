
class celsius:
    def __init__(self , value=23.0):
        self.cel = float(value)
        
    def __get__(self , instance , owner):
        return self.cel

    def __set__(self , instance , value):
        #self.cel=float(value)

class fahrenheit:
    def __get__(self , instance , owner):
        self.fah = instance.cel *1.8 +32.0
        return self.fah

    def __set__(self , instance , value):
        #self.fah=float(value)
        instance.cel = (float(value) - 32.0) / 1.8

class temperature:
    #celsius , fahrenheit
    cel=celsius( )
    fah=fahrenheit( )
    
    
