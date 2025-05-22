def to_uppercase(text: str) -> str:
    return text.upper()

def to_lowercase(text: str) -> str:
    return text.upper()
    lenght = len(str)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(to_uppercase(sys.argv[1]))
    else:
        print("USAGE: uppercase.py <string_to_convert>")
