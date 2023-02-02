import sys

class CaesarCipher:
    def __init__(self, char_list) -> None:
        self.char_list = char_list

    def encode(self, text: str, shift: int, mode: str) -> str:
        if mode != "encrypt" and mode != "decrypt":
            sys.exit("Valid values of mode argument are: 'encrypt', 'decrypt'")
        # Handle 'shift' parameter values > than maximum index 
        new_shift = shift % (len(self.char_list) - 1) if shift > len(self.char_list) -1 else shift
        if isinstance(text, str):
            encoded_text = ""
            for letter in text:
                for index, char in enumerate(self.char_list):
                    if letter.lower() == char and mode == "encrypt":
                        newIndex = index + new_shift if index + new_shift < len(self.char_list) - 1 else index + new_shift - len(char_list)
                        encoded_text += str(self.char_list[newIndex]).capitalize()
                        break
                    elif letter.lower() == char and mode == "decrypt":
                        newIndex = index - new_shift
                        encoded_text += str(self.char_list[newIndex]).capitalize()
                        break
                    elif index == len(self.char_list) - 1:
                        print(f"Character {letter} not known.")
            return encoded_text
        else:
            sys.exit("Funtion argument 'text' must be of value string")
                


char_list = [
    "a", "b" ,"c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", 
    "o", "p", "q", "r", "s", "t" ,"u", "v", "w", "x", "y", "z", "1", "2", 
    "3", "4", "5", "6", "7", "8", "9", " ", "'", "\"", ".", ",", "!", "~", 
    "@", "#", "$", "%", "(", ")",
]
