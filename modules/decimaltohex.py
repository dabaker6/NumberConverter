import data.hexmapping as hexmapping

class Decimaltohex():
    
    integer: int
    modulo: int
    mappedModulo: str

    def __init__(self, num:int) -> None:
        if (int(num) != num):
            raise ValueError('number not an int')
        elif (num > 2147483647):
            raise OverflowError('number too large')
        
        self.num = int(num)
        
    def setInteger(self) -> None:
        self.integer = int(self.num / 16)

    def setModulo(self) -> None:
        self.modulo = self.num % 16

    def mapModulo(self) -> None:
        self.mappedModulo = hexmapping.hexDict[self.modulo]

    def createHex(self) -> str:
        hexList = list()
        completeHex: str = "0x"

        while self.num > 16:
            self.setInteger()
            self.setModulo()
            self.mapModulo()
            hexList.append(self.mappedModulo)
            self.num = self.integer
        
        self.modulo = self.num
        self.mapModulo()

        hexList.append(self.mappedModulo)
        hexList.reverse()

        for char in hexList:
            completeHex += char

        return completeHex