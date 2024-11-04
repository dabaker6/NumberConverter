import unittest
from modules.decimaltohex import Decimaltohex

class TestCalculations(unittest.TestCase):

    def setUp(self):

        self.num: int = 2012
        self.expectedInteger: int = int(self.num / 16)
        self.expectedModulo: int = self.num % 16
        self.FirstexpectedHexValue: str = "C"
        self.CompleteHex: str = "0x7DC"
        self.decimaltohex = Decimaltohex(self.num)        

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
        smalldecimaltohex = Decimaltohex(num)
        self.assertEqual(smalldecimaltohex.createHex(),'0xF')

    def test_SmallerNumber(self):
        num = 2 #less than 16
        smalldecimaltohex = Decimaltohex(num)
        self.assertEqual(smalldecimaltohex.createHex(),'0x'+str(num))

    def test_LargeNumber(self):
        num = 2147483647
        smalldecimaltohex = Decimaltohex(num)
        self.assertEqual(smalldecimaltohex.createHex(),'0x7FFFFFFF')
    
    def test_notanint(self):
        num = 24.3
        self.assertRaises(ValueError,Decimaltohex,num)
        
    def test_inttoolarge(self):
        num = 2147483648
        self.assertRaises(OverflowError,Decimaltohex,num)

    

if __name__ == '__main__':
    unittest.main()