'''
This program allow user to convert a text file to binary format. 
'''


import tkinter as tk
from tkinter import filedialog, messagebox
import os


class Text_Compression:
    def __init__(self, root):
        self.root = root
        self.root.title('Text Compression')
        self.root.geometry("400x300")

        self.file_path = tk.StringVar()
        self.file_path.set('No file selected')

        self.compressed_size = tk.StringVar()
        self.compressed_size.set('Compressed Size : N/A')

        self.create_widgets()


    def create_widgets(self):
        tk.Label(self.root, text = 'Select Text File').pack(pady=(25,5))

        file_entry = tk.Entry(self.root, textvariable=self.file_path, width=50, state = 'readonly')
        file_entry.pack()

        select_file_button = tk.Button(self.root, text = 'Browse File' , command=self.select_file)
        select_file_button.pack(pady = 5)

        compress_button = tk.Button(self.root, text = ' Compress ' , command=self.compress_and_save)
        compress_button.pack(pady=15)

        t = tk.Label(self.root, textvariable = self.compressed_size)
        t.pack()
        
    
    def select_file(self):
        # dialog box should open
        fileName = filedialog.askopenfilename(filetypes = [("Text files", "*.txt"), ("All files", "*.*")])
        if fileName:
            self.file_path.set(fileName)

    def save_file(self, text):
        file_path = filedialog.asksaveasfilename(filetypes=[("Binary files", "*.bin"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'wb') as file:
                bytes_arr = [int(text[i:i+8], 2) for i in range(0, len(text), 8)]
                file.write(bytes(bytes_arr))
            return file_path
        return None

    def compress_and_save(self):
        file_path = self.file_path.get()
        if not file_path or file_path == 'No file selected':
            messagebox.showerror('Please Select a file first! ')
            return
        
        with open(file_path, 'r') as file:
            text = file.read()

        data = compress(text)
        output_path = self.save_file(data)
        if output_path:
            comp_size = os.path.getsize(output_path)
            self.compressed_size.set(f'Compressed Size: {comp_size} bytes')
            messagebox.showinfo('Success', f'File is compressed and saved at {output_path}.')


# -----------Huffman's Coding Logic-----------

import heapq

class BinaryTreeNode:
    def __init__(self,value,freq):
        self.value=value
        self.freq=freq
        self.left=None
        self.right=None
    
    def __lt__(self,other):
        return self.freq<other.freq
    
    def __eq__(self,other):
        return self.freq==other.freq


heap=[]
codes={}
        
def make_frequency_dict(text):
    freq_dict={}
    for char in text:
        if char not in freq_dict:
            freq_dict[char]=0
        freq_dict[char]+=1
    return freq_dict


def buildHeap(freq_dict):
    for key in freq_dict:
        frequency=freq_dict[key]
        binary_tree_node = BinaryTreeNode(key,frequency)
        heapq.heappush(heap,binary_tree_node)


def buildTree():
    while(len(heap)>1):
        binary_tree_node_1=heapq.heappop(heap)
        binary_tree_node_2=heapq.heappop(heap)
        freq_sum=binary_tree_node_1.freq+binary_tree_node_2.freq
        newNode=BinaryTreeNode(None,freq_sum)
        newNode.left=binary_tree_node_1
        newNode.right=binary_tree_node_2
        heapq.heappush(heap,newNode)
    return

def buildCodesHelper(root,curr_bits):
    if root is None:
        return 
    if root.value is not None:
        codes[root.value] = curr_bits
        return
    buildCodesHelper(root.left,curr_bits+"0")
    buildCodesHelper(root.right,curr_bits+"1")


def buildCodes():
    root=heapq.heappop(heap)
    buildCodesHelper(root,"")


def getEncodedText(text):
    encoded_text=""
    for char in text:
        encoded_text+=codes[char]
    return encoded_text


def getPaddedEncodedText(encoded_text):
    padded_amount=8-(len(encoded_text)%8)
    for i in range(padded_amount):
        encoded_text+='0'
    padded_info="{0:08b}".format(padded_amount)
    encoded_text = padded_info+encoded_text
    return encoded_text
    
def compress(data):
    text=data.rstrip()
    freq_dict = make_frequency_dict(text)

    buildHeap(freq_dict)
    buildTree()
    buildCodes()
    encoded_text=getEncodedText(text)

    padded_encoded_text = getPaddedEncodedText(encoded_text)
    return padded_encoded_text





root = tk.Tk()
a = Text_Compression(root)
root.mainloop()