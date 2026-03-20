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

import tkinter as tk
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
wrong_counts = {letter: 0 for letter in letters}

current_letter = None
streak = 0
total = 0
correct = 0


def next_question():
    global current_letter

    weights = [1 + wrong_counts[l] for l in letters]
    current_letter = random.choices(letters, weights=weights)[0]

    braille_label.config(text=braille_visual[current_letter])
    entry.delete(0, tk.END)
    feedback_label.config(text='')


def check_answer():
    global streak, total, correct

    user = entry.get().strip().lower()
    total += 1

    if user == current_letter:
        correct += 1
        streak += 1
        feedback_label.config(text='Correct', fg='green')
    else:
        wrong_counts[current_letter] += 1
        streak = 0
        feedback_label.config(text=f'Wrong (was {current_letter})', fg='red')

    accuracy = (correct / total) * 100
    stats_label.config(text=f'Streak: {streak} | Accuracy: {accuracy:.1f}%')

    root.after(800, next_question)


# GUI setup
root = tk.Tk()
root.title('Braille Trainer')

# BIG font for Braille
braille_label = tk.Label(root, text='', font=('Segoe UI Symbol', 100))
braille_label.pack(pady=20)

entry = tk.Entry(root, font=('Arial', 20))
entry.pack()
entry.bind('<Return>', lambda event: check_answer())

feedback_label = tk.Label(root, text='', font=('Arial', 16))
feedback_label.pack(pady=10)

stats_label = tk.Label(root, text='Streak: 0 | Accuracy: 0%', font=('Arial', 12))
stats_label.pack(pady=5)

next_question()

root.mainloop()