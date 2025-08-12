'''
This program allow user to generate a random password of the given password length..
'''

import tkinter as tk
from tkinter import messagebox
import random
import string

label_font = ('Helvetica', 11)
button_font = ('Cambria', 12)
entry_font = ('Arial', 9)


class RandomPasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title('Random Password Generator')
        self.root.geometry('400x350')
        self.root.configure(bg = "#F0F8FF")

        # frame to contain all buttons and labels
        self.frame = tk.Frame(self.root, bg = "#F0F8FF")
        self.frame.pack(pady=20)

        # password_len label
        self.entry_label = tk.Label(self.frame, text='Password Length', font = label_font, bg = "#F0F8FF")
        self.entry_label.grid(row=0, column=0, padx=8, pady=10, sticky='w')

        # password entry area
        self.length_entry = tk.Entry(self.frame, font = entry_font, width=20, bg = '#F8F8FF')
        self.length_entry.grid(row=0, column=1, padx=8, pady=10, sticky='w')
        self.length_entry.bind('<Return>', self.generate_password)
        # set focus by default on entry len area
        self.length_entry.focus()

        # generate password Button
        self.generate_password_button = tk.Button(self.frame, text='Generate Password', padx=20, font=button_font, bg = '#00C957', command=self.generate_password)
        self.generate_password_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        # Your password Label
        self.your_password_label = tk.Label(self.frame, text='Your Password:', font = label_font, bg = "#F0F8FF")
        self.your_password_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')

        # your password entry area
        self.user_password = tk.StringVar()
        self.user_password.set('')
        self.password_entry = tk.Entry(self.frame, textvariable=self.user_password, font = entry_font, bg = '#F8F8FF')
        self.password_entry.grid(row=2, column=1, padx=10, pady=5, sticky='w')

        # strength label
        self.strength_val = tk.StringVar()
        self.strength_val.set('N/A')
        self.strength_label = tk.Label(self.frame, text ='Strength: ', font = label_font, bg = "#F0F8FF")
        self.strength_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')

        # strength value label -->> to show the value of the strength of the password
        self.str_val_label = tk.Label(self.frame, textvariable = self.strength_val, font = ('Helvetica', 11, 'bold'), bg = '#F0F8FF')
        self.str_val_label.grid(row=3, column=1, padx=10, pady=5, sticky='w')

        # regeneration info label
        self.reg_info_label = tk.Label(self.frame, text = 'Press "R" to regenerate the password.', font = ('Arial', 9), bg = "#F0F8FF")
        self.reg_info_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        # regeneration button
        self.reg_button = tk.Button(self.frame, text='Regenerate Password', font=button_font, bg = '#FFC125', command=self.generate_password)
        self.reg_button.grid(row = 5, column=0, columnspan=2, padx=10, pady=5)
        self.root.bind('<r>', self.generate_password)


    def generate_password(self, event = None):
        len = self.length_entry.get().strip()
        if not len.isdigit():
            messagebox.showerror('Error', 'Please Enter a valid positive Integer!')
            return
        try:
            input_len = int(len)
        except ValueError:
            messagebox.showerror('Error', 'Please Enter a Valid positive integer')
            return
        # string.punctuation constant contains all the standard punctuation characters.
        base_sequence = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(base_sequence, k = input_len)) # choose 'k' character from the base_seq

        # update strength
        strength = self.check_strength_of_password(password)
        self.strength_val.set(strength)

        # update password
        self.user_password.set(password)
        # remove focus from length entry box
        self.frame.focus_set()
        

    def check_strength_of_password(self, password):
        num_type = 0
        for char in password:
            if char >= 'A' and char <= 'Z' or char >='a' and char <= 'z' or char >= '0' and char <='9':
                num_type += 1
            else:#special char
                num_type += 1

        if num_type >= 3 and len(password) >=12 :
            return 'Very Strong'
        elif num_type >= 2 and len(password) >=8:
            return 'Strong'
        elif num_type >= 2:
            return  'Medium'
        else:
            return 'Weak'

root = tk.Tk()
p = RandomPasswordGenerator(root)
root.mainloop()