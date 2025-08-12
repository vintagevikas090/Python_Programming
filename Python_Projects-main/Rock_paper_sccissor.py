import tkinter as tk
from tkinter import messagebox
import random

label_font = ('Arial', 11)
Button_font = ('Cambria', 12)

class RockPaperSccissor:
    def __init__(self, root):
        self.root = root
        self.root.title('Rock Paper Scissors')
        self.root.geometry("450x330")
        self.root.configure(bg = "#F0F8FF")

        self.choice_info_label = tk.Label(self.root, text = 'Choose Rock, Paper or Scissors:', font = label_font, bg = "#F0F8FF")
        self.choice_info_label.pack(pady=10)

        # frame for the rock, paper, scissor buttons
        self.frame = tk.Frame(self.root, bg = "#F0F8FF")
        self.frame.pack()

        # rock button 
        self.rock_button = tk.Button(self.frame, text = 'Rock(1)', width=10, command=self.choose_rock, font = Button_font, bg = '#FFB90F')
        self.rock_button.pack(side = tk.LEFT, padx=10, pady=(10, 35))
        self.root.bind('1', self.choose_rock)

        # paper button 
        self.paper_button = tk.Button(self.frame, text = "Paper(2)", width=10, command=self.choose_paper, font = Button_font, bg = '#1E90FF')
        self.paper_button.pack(side= tk.LEFT, padx=10, pady=(10, 35))
        self.root.bind('2', self.choose_paper)

        # scissor button
        self.scissor_button = tk.Button(self.frame, text="Scissor(3)", width=10, command=self.choose_scissor, font = Button_font, bg = '#00CD00')
        self.scissor_button.pack(side = tk.LEFT, padx=10, pady=(10, 35))
        self.root.bind('3', self.choose_scissor)

        # label for showing the result each time
        self.result_label = tk.Label(self.root, text='', font= ('Verdana', 12, 'bold', 'italic'), bg = "#F0F8FF")
        self.result_label.pack(pady=20)

        # your score label
        self.your_score_label = tk.Label(self.root, text= 'Your Score: 0', font = label_font, bg = "#F0F8FF")
        self.your_score_label.pack(pady=(10, 9))

        # comp score label
        self.comp_score_label = tk.Label(self.root, text= 'Computer score: 0', font = label_font, bg = "#F0F8FF")
        self.comp_score_label.pack(pady = (1, 10))

        # quit Button
        self.quit_button = tk.Button(self.root,text='Quit(Q)', width=10, command=self.quit, font = Button_font, bg = '#EE0000')
        self.quit_button.pack(pady = 10)
        self.root.bind('q', self.quit)

        self.user_score = 0
        self.computer_score = 0


    def play(self, user_choice):
        comp_choice = random.choice(['Rock', 'Paper', 'Scissor'])
        result = ''
        if user_choice == comp_choice:
            result = "It's a Tie"
        elif (user_choice == 'Rock' and comp_choice == 'Scissor') or \
            (user_choice == 'Paper' and comp_choice == 'Rock') or \
            (user_choice == 'Scissor' and comp_choice=='paper'):
            result = 'You Win!'
            self.user_score+= 1
        else:
            result = 'Computer Win!'
            self.computer_score += 1

        self.update_score(result)

    def choose_rock(self, event = None):
        self.play('Rock')
    def choose_paper(self, event = None):
        self.play('Paper')
    def choose_scissor(self, event = None):
        self.play('Scissor')

    def update_score(self, res):
        self.result_label.config(text = res)
        self.your_score_label.config(text = f'Your Score: {self.user_score}')
        self.comp_score_label.config(text = f'Computer Score: {self.computer_score}')

    def quit(self, event = None):
        if self.user_score > self.computer_score:
            messagebox.showinfo('Congratulation!', f'You Won!\n\nYour Score: {self.user_score}\nComputer Score: {self.computer_score}')
        elif self.user_score < self.computer_score:
            messagebox.showinfo('Oops!', f'You Lost!\n\nYour Score: {self.user_score}\nComputer Score: {self.computer_score}')
        else:
            messagebox.showinfo('Bingo!', f"Game Tied!\n\nYour Score: {self.user_score}\nComputer Score: {self.computer_score}")
        self.root.destroy()



root = tk.Tk()
window = RockPaperSccissor(root)
root.mainloop()