import sys

def convert_text(text, mode="/toupper"):
    if mode == "/tolower":
        return text.lower()
    return text.upper()  # Domyślnie konwersja na wielkie litery

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Użycie: script.py <tekst> [/toupper|/tolower]")
        sys.exit(1)

    text = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else "/toupper"

    result = convert_text(text, mode)
    print(result)



#  VERSION 1

# def to_uppercase(text: str) -> str:
#     return text.upper()

# if __name__ == "__main__":
#     import sys
#     if len(sys.argv) > 1:
#         print(to_uppercase(sys.argv[1]))
#     else:
#         print("USAGE: uppercase.py <string_to_convert>")
