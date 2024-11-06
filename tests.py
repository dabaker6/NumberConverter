import unittest
from modules.decimaltohex import Decimal_to_hex
from modules.hextodecimal import Hex_to_decimal

class Test_decimaltohex(unittest.TestCase):

    def setUp(self):

        self.num: int = 2012
        self.expectedInteger: int = int(self.num / 16)
        self.expectedModulo: int = self.num % 16
        self.FirstexpectedHexValue: str = "C"
        self.CompleteHex: str = "0x7DC"
        self.decimaltohex = Decimal_to_hex(self.num)        

    def test_input(self):
        self.assertEqual(self.decimaltohex.num,int(self.num),'Num is not an int')

    def test_integerdivision(self):
        self.decimaltohex.setInteger()
        self.assertEqual(self.decimaltohex.integer,self.expectedInteger,'Integer not correct')

    def test_modulo(self):
        self.decimaltohex.setModulo()
        self.assertEqual(self.decimaltohex.modulo,self.expectedModulo,'Modulo not correct')

    def test_mapping(self):
        self.decimaltohex.setInteger()
        self.decimaltohex.setModulo()
        self.decimaltohex.mapModulo()
        self.assertEqual(self.decimaltohex.mappedModulo,self.FirstexpectedHexValue,'Hex value not correct')

    def test_CreateHex(self):
        
        self.assertEqual(self.decimaltohex.createHex(),self.CompleteHex)

    def test_SmallNumber(self):
        num = 15 #must be > 9 to test letters
        smalldecimaltohex = Decimal_to_hex(num)
        self.assertEqual(smalldecimaltohex.createHex(),'0xF')

    def test_SmallerNumber(self):
        num = 2 #less than 16
        smalldecimaltohex = Decimal_to_hex(num)
        self.assertEqual(smalldecimaltohex.createHex(),'0x'+str(num))

    def test_LargeNumber(self):
        num = 2147483647
        smalldecimaltohex = Decimal_to_hex(num)
        self.assertEqual(smalldecimaltohex.createHex(),'0x7FFFFFFF')
    
    def test_notanint(self):
        num = 24.3
        self.assertRaises(ValueError,Decimal_to_hex,num)
        
    def test_inttoolarge(self):
        num = 2147483648
        self.assertRaises(OverflowError,Decimal_to_hex,num)

class Test_hextodecimal(unittest.TestCase):    

    def setUp(self):
        
        self.hexvalue = "0x7DC"
        self.formattedhexvalue = "7DC"
        self.expectedNum = 2012
        self.hextodecimal = Hex_to_decimal(self.hexvalue)

    def test_inputasstring(self):
        self.assertEqual(self.hextodecimal.hex,self.formattedhexvalue)

    def test_inputasint(self):
        num = 77
        self.assertRaises(ValueError,Hex_to_decimal,num)

    def test_formattingwithprefix(self):        
        hexvalue = "0x33"
        hextodecimal = Hex_to_decimal(hexvalue)
        self.assertEqual(hextodecimal.hex,"33")

    def test_formattingnoprefix(self):        
        hexvalue = "fh44"
        hextodecimal = Hex_to_decimal(hexvalue)
        self.assertEqual(hextodecimal.hex,hexvalue)

#    def test_validhexcharacters(self):
#        hexvalue = "fh44"        
#        self.assertRaises(ValueError,Hex_to_decimal,hexvalue)

    def test_mapvalidvalues(self):
        self.hextodecimal.mapValue("7")
        self.assertEqual(self.hextodecimal.mappedValue,7)
        self.hextodecimal.mapValue("F")
        self.assertEqual(self.hextodecimal.mappedValue,15)
    
    def test_mapinvalidvalues(self):
        self.assertRaises(KeyError,self.hextodecimal.mapValue,"77")
        self.assertRaises(KeyError,self.hextodecimal.mapValue,"G")

    def test_createValuesToMap(self):
        self.hextodecimal.createValuesToMap()
        self.assertEquals(self.hextodecimal.mappedValues,[0,7,13,12])

    def test_createFinalValue(self):
        self.assertEqual(self.hextodecimal.convertToDec(),self.expectedNum)

    def test_createFinalValueWithNoValues(self):
        hextodecimal = Hex_to_decimal("0")
        self.assertEquals(hextodecimal.convertToDec(),0)

    def test_lowercase(self):
        self.hextodecimal.mapValue('f')
        self.assertEqual(self.hextodecimal.mappedValue,15)
        self.hextodecimal.mapValue('F')
        self.assertEqual(self.hextodecimal.mappedValue,15)
        self.hextodecimal.mapValue('a')
        self.assertEqual(self.hextodecimal.mappedValue,10)
 
if __name__ == '__main__':
    unittest.main()