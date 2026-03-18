import random

braille_visual = {
    "a": "⠁",
    "b": "⠃",
    "c": "⠉",
    "d": "⠙",
    "e": "⠑",
    "f": "⠋",
    "g": "⠛",
    "h": "⠓",
    "i": "⠊",
    "j": "⠚",
}

letters = list(braille_visual.keys())

while True:
    letter = random.choice(letters)
    print(f"Braille: {braille_visual[letter]}")
    
    user = input("Your answer: ").lower()
    
    if user == letter:
        print("Correct\n")
    else:
        print(f"Wrong. It was {letter}\n")