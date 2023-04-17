class ViajeroFrecuente:
    __num=0
    __dni=""
    __nombre=""
    __apellido=""
    __millas=0


    def __init__(self,num,dni,nom,ape,millas):
        self.__nombre=nom
        self.__num=num
        self.__dni=dni
        self.__apellido=ape
        self.__millas=millas

    def cantidadYotaldeMillas(self):
        return self.__millas
    

    def acumularMillas(self, millasA):
        self.__millas=self.__millas+millasA

    def canjearMillas(self,canje):
        if canje<=self.__millas:
            print("Se pueden canjear las millas")
            self.__millas=self.__millas-canje
        else:
            print("no se pueden canjear las millas")