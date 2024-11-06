from modules.decimaltohex import Decimal_to_hex
from modules.hextodecimal import Hex_to_decimal
import sys

def main() -> None:
    #Refactor to be SOLID
    if(sys.argv[1] == "num"):
        text: str = input("num:")
        while text != "exit":
            try:
                decimalToHex = Decimal_to_hex(int(text))
                print(decimalToHex.createHex())
            except ValueError as error:
                print("An error occurred:", type(error).__name__, "–", error)
            except OverflowError as error:
                print("An error occurred:", type(error).__name__, "–", error)
            finally:
                text: str = input("num:")
    elif(sys.argv[1] == 'hex'):
        text: str = input("hex:")
        while text != "exit":
            try:
                hextodecimal = Hex_to_decimal(text)
                print(hextodecimal.convertToDec())
            except KeyError as error:
                print("An error occurred:", type(error).__name__, "–", error)
            except ValueError as error:
                print("An error occurred:", type(error).__name__, "–", error)
            finally:
                text: str = input("hex:")
    else:
        print("Unknown argument")

if __name__ == "__main__":
    main()   
