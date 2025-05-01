def to_uppercase(text: str) -> str:
    return text.upper()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(to_uppercase(sys.argv[1]))
    else:
        print("USAGE: uppercase.py <string_to_convert>")
