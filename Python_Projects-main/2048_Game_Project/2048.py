from tkinter import *
import Logics_2048
import constants as c

class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title('2048')
        self.master.bind('<Key>', self.key_down)
        self.commands = {c.KEY_DOWN : Logics_2048.Move_down, c.KEY_LEFT: Logics_2048.Move_left,
                         c.KEY_RIGHT:Logics_2048.Move_right, c.KEY_UP:Logics_2048.Move_up}
        
        self.grid_cells = []
        self.initialise_grid()
        self.initialise_matrix()
        self.update_grid_cells()

        self.mainloop()

    def initialise_grid(self):
        bg = Frame(self, background=c.BACKGROUND_COLOR_GAME, width=c.SIZE, height=c.SIZE)
        bg.grid()
        # make 16 cells in grid
        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(bg, background=c.BACKGROUND_COLOR_CELL_EMPTY, width=100, height=100)
                # we can also use the defined variables in constants file
                #cell = Frame(bg, background=c.BACKGROUND_COLOR_CELL_EMPTY, width=c.SIZE/c.GRID_LEN, height=c.SIZE/c.GRID_LEN)
                cell.grid(row=i, column=j, padx=10, pady=10)
                # put label on cell
                t = Label(master=cell, text="", background=c.BACKGROUND_COLOR_CELL_EMPTY, justify=CENTER, font=c.FONT, width=5, height=2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)

    def initialise_matrix(self):
        self.matrix = Logics_2048.start_game()
        Logics_2048.add_new_2(self.matrix)
        Logics_2048.add_new_2(self.matrix)
    
    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                num = self.matrix[i][j]
                if num == 0:
                    self.grid_cells[i][j].configure(text='', background= c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text = (num), background = c.BACKGROUND_COLOR_DICT[num], foreground = c.CELL_COLOR_DICT[num])
        self.update_idletasks()

    # which function has to be executed acc to the key pressed
    def key_down(self, event):
        key = repr(event.char)
        if key in self.commands:
            self.matrix, changed = self.commands[key](self.matrix)
            if changed:
                Logics_2048.add_new_2(self.matrix)
                self.update_grid_cells()
                changed = False
                if Logics_2048.get_current_state(self.matrix) == 'WON':
                    self.grid_cells[1][1].configure(text='YOU', background = c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text='WON!', background = c.BACKGROUND_COLOR_CELL_EMPTY)
                if Logics_2048.get_current_state(self.matrix) == 'LOST':
                    self.grid_cells[1][1].configure(text='YOU', background = c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text='LOST!', background = c.BACKGROUND_COLOR_CELL_EMPTY)
game = Game2048()
