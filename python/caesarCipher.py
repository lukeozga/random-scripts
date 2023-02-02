import sys

class CaesarCipher:
    def __init__(self, char_list) -> None:
        self.char_list = char_list

    def encode(self, text: str, shift: int, mode: str) -> str:
        if mode != "encrypt" and mode != "decrypt":
            sys.exit("Valid values of mode argument are: 'encrypt', 'decrypt'")
        if isinstance(text, str):
            encoded_text = ""
            for letter in text:
                isUpper = letter.isupper()
                for index, char in enumerate(self.char_list):
                    if letter.lower() == char and mode == "encrypt":
                        newIndex = index + shift if index + shift <= len(char_list) - 1 else index + shift - len(char_list) - 1
                        encoded_text += self.char_list[newIndex] if not isUpper else str(self.char_list[newIndex]).upper()
                        break
                    elif letter.lower() == char and mode == "decrypt":
                        newIndex = index - shift
                        encoded_text += self.char_list[newIndex] if not isUpper else str(self.char_list[newIndex]).upper()
                        break
                    elif index == len(char_list) - 1:
                        print(f"Character {letter} not known.")
            return encoded_text
        else:
            sys.exit("Funtion argument 'text' must be of value string")

char_list = [
    "a", "b" ,"c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", 
    "o", "p", "q", "r", "s", "t" ,"u", "v", "w", "x", "y", "z", "1", "2", 
    "3", "4", "5", "6", "7", "8", "9", " ", "'", "\"" ".", ",", "!", "~", 
    "@", "#", "$", "%", "(", ")", "~",
]