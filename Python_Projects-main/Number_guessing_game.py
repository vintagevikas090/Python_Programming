import random
import tkinter as tk
from tkinter import messagebox

button_font = ("Helvetica", 12)
window_bg = '#F0F8FF'


class NumberGuessingGame:
    def __init__(self, root, max_attempts=10):
        self.root = root
        self.root.title('Number Guessing Game')
        self.root.geometry('500x300')
        self.root.configure(bg = window_bg)

        self.comp_guess = random.randint(1, 100)
        self.max_attempts = max_attempts
        self.remaining_attempts = max_attempts

        self.label = tk.Label(self.root, text = 'Guess the number between 1 and 100:', font=('Cambria', 13), bg = window_bg)
        self.label.pack(pady=(10, 5))

        self.entry = tk.Entry(self.root, width=35, font=('High Tower Text(bold)', 11))
        self.entry.pack(pady=(10))
        self.entry.bind('<Return>', self.check_guess)

        # frame for the submit, hint button
        frame = tk.Frame(self.root)
        frame.pack(pady=5)

        self.submit_button = tk.Button(frame, text = 'Submit', font=button_font, command=self.check_guess, padx=10, pady=5, bg = '#228B22')
        self.submit_button.pack(side = tk.LEFT, padx=10)

        self.hint_button = tk.Button(frame, text='Hint', command=self.show_hint, font=button_font, padx=10, pady=5, bg = '#436EEE')
        self.hint_button.pack(side = tk.LEFT, padx=10)

        self.quit_button = tk.Button(self.root, text = 'Quit', command=self.exit_game, font=button_font, padx=10, pady=5, bg = '#FF4040')
        self.quit_button.pack(pady = 10)

        self.attempt_label = tk.Label(self.root, text= f'Remaining attempts: {self.remaining_attempts}', font=('Arial', 11), bg = window_bg)
        self.attempt_label.pack(pady = 10)

    # event is req becz when enter key is pressed, it implicitly passes an event object to the event handler function (check_guess)
    def check_guess(self, event = None):
        user_guess = self.entry.get().strip()
        if len(user_guess) == 0:
            # .showinfo takes two arguments
            # 1st is the title  of the dialog box and 2nd is the message to be displayed in the dialog box
            messagebox.showinfo('Error', 'Please Enter a Number!')
            self.reset_game()
            return
        
        try:
            guess = int(user_guess)
        except ValueError:
            messagebox.showinfo('Error', 'Please Enter a valid Number!')
            self.reset_game()
            return
        
        # ensure the number is in the range
        if guess < 0 or guess >= 100:
            messagebox.showinfo('Error', f'The Number must be in between 1 to 100')
            self.reset_game()
            return
        
        # take care of the remaining attempts
        self.remaining_attempts -= 1
        self.attempt_label.configure(text=f'Remaining attempts:{self.remaining_attempts}')

        if self.remaining_attempts == 0:
            messagebox.showinfo('Game Over!', f'You have exhausted all {self.max_attempts}. The correct  number was {self.comp_guess}.')
            self.reset_game()
            return
        
        if guess < self.comp_guess:
            messagebox.showinfo('Hint', 'The Number you chose is Low')
        elif guess > self.comp_guess:
            messagebox.showinfo('Hint', 'The Number you chose is High')
        else:
            messagebox.showinfo("Congratulations!", f"That's the Correct Guess You Guessed it in {self.max_attempts-self.remaining_attempts} attempts.")
            self.reset_game()

        self.entry.delete(0, tk.END)


    def show_hint(self):
        lower_limit = self.comp_guess-10
        higher_limit = self.comp_guess+10
        if lower_limit < 0:
            lower_limit = 0
        if higher_limit > 100:
            higher_limit = 100
        messagebox.showinfo('Hint', f'The Number is in the Range of {lower_limit} and {higher_limit}')

    def exit_game(self):
        # .askyesno -->> creates a dialog box asking for the choice between yes and no
        answer = messagebox.askyesno("Exit Game", "Do You Want to Exit?")
        if answer:
            root.destroy()

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.remaining_attempts = self.max_attempts
        self.attempt_label.config(text=f"Remaining attempts: {self.remaining_attempts}")
        self.entry.delete(0, tk.END)
        


root = tk.Tk()
window = NumberGuessingGame(root)
root.mainloop()