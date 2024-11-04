
class Decimaltohex():
    
    integer: int
    modulo: int
    mappedModulo: str

    hexDict = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
        }

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
        self.mappedModulo = self.hexDict[self.modulo]

    def createHex(self) -> str:
        hexList = list()
        completeHex: str = "0x"

        while self.num > 16:
            self.setInteger()
            self.setModulo()
            self.mapModulo()
            hexList.append(self.mappedModulo)
            self.num = self.integer
        

        
        hexList.append(str(self.num))
        hexList.reverse()

        for char in hexList:
            completeHex += char

        return completeHex