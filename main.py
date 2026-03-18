'''
helpful notes:

families:
    a, k, u
    b, l, v
    c, m, x

g: f pattern + dot 5 -> g 

braille square:
    1 4
    2 5
    3 6
'''

import random

braille_visual = {
    'a': '⠁',
    'b': '⠃',
    'c': '⠉',
    'd': '⠙',
    'e': '⠑',
    'f': '⠋',
    'g': '⠛',
    'h': '⠓',
    'i': '⠊',
    'j': '⠚',
}

letters = list(braille_visual.keys())

# track mistakes per letter
wrong_counts = {letter: 0 for letter in letters}

streak = 0
total = 0
correct = 0

while True:
    # weighted selection (focus on mistakes)
    weights = [1 + wrong_counts[l] for l in letters]
    letter = random.choices(letters, weights=weights)[0]

    print(f'\nBraille: |{braille_visual[letter]}|')

    user_choice = input('Your answer (or "quit"): ').lower().strip()

    if user_choice == 'quit':
        break

    total += 1

    if user_choice == letter:
        correct += 1
        streak += 1
        print('Correct')
    else:
        wrong_counts[letter] += 1
        streak = 0
        print(f'Wrong. It was {letter}')

    accuracy = (correct / total) * 100

    print(f'Streak: {streak}')
    print(f'Accuracy: {accuracy:.1f}%')

    # Optional: show problem letters occasionally
    if total % 10 == 0:
        print('\nMistake breakdown:')
        for l, count in sorted(wrong_counts.items(), key=lambda x: -x[1]):
            if count > 0:
                print(f'{l}: {count}')
        print('-' * 20)
