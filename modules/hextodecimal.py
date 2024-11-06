import data.hexmapping as hexmapping

class Hex_to_decimal():
    
    mappedValue: str
    mappedValues: list[int] = []

    def __init__(self, hex:str) -> None:
        if(type(hex) != str):
            raise ValueError('value not a str')
        
        if(hex[:2] == "0x"):
            hex = hex[2:]

        self.hex = hex
    
    def mapValue(self,valueToMap:str) -> int:
        self.mappedValue = hexmapping.numDict[valueToMap.upper()]

    def createValuesToMap(self) -> list[str]:
        self.mappedValues = [0]
        valuesToMap = [i for i in self.hex]
        for i in range(len(valuesToMap)): 
            self.mapValue(valuesToMap[i])
            self.mappedValues.append(self.mappedValue)

    def convertToDec(self) -> int:
        
        self.createValuesToMap()

        if(len(self.mappedValues) == 0):
            raise ValueError('no values to convert')

        i: int = 0
        finalValue: int = 0
        for value in self.mappedValues:
            finalValue = finalValue * 16 + value
            i+=1
            if(i == len(self.mappedValues)):
               break
               
        return finalValue