import tkinter as tk
import csv
import random

# Load flashcards
flashcards = []
with open('flashcards.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        flashcards.append(row)

# Extract unique categories
categories = sorted(list(set(card['Category'] for card in flashcards)))

# Session variables
current_index = 0
score = 0
filtered_flashcards = flashcards.copy()

# Functions
def show_answer():
    answer_label.config(text=filtered_flashcards[current_index]['Answer'])

def next_card():
    global current_index
    current_index += 1
    if current_index >= len(filtered_flashcards):
        question_label.config(text="End of Flashcards!")
        answer_label.config(text=f"Your score: {score}/{len(filtered_flashcards)}")
        next_button.config(state="disabled")
        show_button.config(state="disabled")
        correct_button.config(state="disabled")
        return
    question_label.config(text=filtered_flashcards[current_index]['Question'])
    answer_label.config(text="")
    category_label.config(text=f"Category: {filtered_flashcards[current_index]['Category']}")

def mark_correct():
    global score
    score += 1
    next_card()

def select_category(event):
    global filtered_flashcards, current_index, score
    selected = category_var.get()
    if selected == "All":
        filtered_flashcards = flashcards.copy()
    else:
        filtered_flashcards = [card for card in flashcards if card['Category'] == selected]
    random.shuffle(filtered_flashcards)
    current_index = 0
    score = 0
    question_label.config(text=filtered_flashcards[current_index]['Question'])
    answer_label.config(text="")
    category_label.config(text=f"Category: {filtered_flashcards[current_index]['Category']}")
    next_button.config(state="normal")
    show_button.config(state="normal")
    correct_button.config(state="normal")

# GUI
root = tk.Tk()
root.title("A&P Flashcards")

category_var = tk.StringVar(root)
category_var.set("All")
category_menu = tk.OptionMenu(root, category_var, "All", *categories, command=select_category)
category_menu.pack(pady=5)

category_label = tk.Label(root, text=f"Category: {filtered_flashcards[current_index]['Category']}", font=('Arial', 12, 'italic'))
category_label.pack(pady=5)

question_label = tk.Label(root, text=filtered_flashcards[current_index]['Question'], font=('Arial', 16), wraplength=500)
question_label.pack(pady=20)

answer_label = tk.Label(root, text="", font=('Arial', 14), fg='blue', wraplength=500)
answer_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

show_button = tk.Button(button_frame, text="Show Answer", command=show_answer)
show_button.grid(row=0, column=0, padx=5)

correct_button = tk.Button(button_frame, text="I Knew This", command=mark_correct)
correct_button.grid(row=0, column=1, padx=5)

next_button = tk.Button(button_frame, text="Next Card", command=next_card)
next_button.grid(row=0, column=2, padx=5)

root.mainloop()
