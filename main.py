from modules.decimaltohex import Decimaltohex
import cmd

def main() -> None:
    
    text: str = input("num:")

    while text != "exit":
        try:
            decimalToHex = Decimaltohex(int(text))
            print(decimalToHex.createHex())
        except ValueError as error:
            print("An error occurred:", type(error).__name__, "–", error)
        except OverflowError as error:
            print("An error occurred:", type(error).__name__, "–", error)
        finally:
            text: str = input("num:")

if __name__ == "__main__":
    main()   
