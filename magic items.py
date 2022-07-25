

class Numstr:
    def __init__(self , value):
        self.value = str(value)
    def __str__(self ):
         return self.value
    def __int__(self):
        return int(self.value)
    def __float__(self):
        return __float__(self.value)
    