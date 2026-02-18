import base64

ALPHA_MAP = {
    "a": "█▀▀█ \n█▄▄█ \n▀──▀ ",
    "b": "█▀▀▄ \n█▀▀▄ \n▀▀▀─ ",
    "c": "█▀▀ \n█── \n▀▀▀ ",
    "d": "█▀▀▄ \n█──█ \n▀▀▀─ ",
    "e": "█▀▀ \n█▀▀ \n▀▀▀ ",
    "f": "█▀▀ \n█▀▀ \n▀── ",
    "g": "█▀▀▀ \n█─▀█ \n▀▀▀▀ ",
    "h": "█──█ \n█▀▀█ \n▀──▀ ",
    "i": "─▀─ \n▀█▀ \n▀▀▀ ",
    "j": "──▀ \n──█ \n█▄█ ",
    "k": "█─█ \n█▀▄ \n▀─▀ ",
    "l": "█── \n█── \n▀▀▀ ",
    "m": "█▀▄▀█ \n█─▀─█ \n▀───▀ ",
    "n": "█▀▀▄ \n█──█ \n▀──▀ ",
    "o": "█▀▀█ \n█──█ \n▀▀▀▀ ",
    "p": "█▀▀█ \n█──█ \n█▀▀▀ ",
    "q": "█▀▀█ \n█──█ \n▀▀▀█ ",
    "r": "█▀▀█ \n█▄▄▀ \n▀─▀▀ ",
    "s": "█▀▀ \n▀▀█ \n▀▀▀ ",
    "t": "▀▀█▀▀ \n──█── \n──▀── ",
    "u": "█──█ \n█──█ \n─▀▀▀ ",
    "v": "▀█─█▀ \n─█▄█─ \n──▀── ",
    "w": "█───█ \n█▄█▄█ \n─▀─▀─ ",
    "x": "█─█ \n▄▀▄ \n▀─▀ ",
    "y": "█──█ \n█▄▄█ \n▄▄▄█ ",
    "z": "▀▀█ \n▄▀─ \n▀▀▀ ",
    ",": "── \n▄▄ \n─█ ",
    " ": "   \n   \n   ",
    "@": "▀ ▄ ▀\n▄   ▄\n ▀▀▀ ",
}  #'▄ ▀▄ \n─ ─█ \n▀ ▄▀',
PW = b"RkEyNQ=="


def b64_to_s(input):
    return str(base64.b64decode(input), encoding="utf-8")


def welcome_message():
    if input("Password: ").upper() != b64_to_s(PW):
        print("Incorrect password :(")
        return

    name = input("Enter your name (will search for [name].txt): ")
    try:
        file = open(f"{name}.txt", "r")
        preferred_name = file.readline().strip()
        if not preferred_name.isalpha():
            raise ValueError

        display_data = [
            b64_to_s(b"V0VMQ09NRQ=="),
            b64_to_s(b"VE8gQVBQREVW"),
            f"{preferred_name}@",
        ]
        for word in display_data:
            output = [""] * 3
            for letter in word:
                top, middle, bottom = ALPHA_MAP[letter.lower()].split("\n")
                output[0] += top
                output[1] += middle
                output[2] += bottom
            print("\n".join(output), end="\n\n")

    except FileNotFoundError:
        print(f"The file ./{name}.txt doesn't exist!")
    except ValueError:
        print(
            "Please ensure the file contains only characters from the English alphabet"
        )

if __name__ == "__main__":
    welcome_message()