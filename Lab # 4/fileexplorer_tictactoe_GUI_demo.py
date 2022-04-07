'''
Lab 4 PostLab 2
Explore the Tkinter.filedialog module to get the name of a text file

Name: Jason Ray M. Moslares
Course: CPE106L_B2

This is a modified version of the Tic-Tac-Toe GUI program from . 
The modification was made to allow the program to browse and read
a text file. The askopenfile() method from the module of filedialog 
is used in the program.
'''

import tkinter as tk
import tkinter.messagebox as mb
import oxo_logic

#import all components from the tkinter library
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile #imports filedialog module to use the askopenfile function

top = tk.Tk()

def buildMenu(parent): 
    #Added Open as another selection in the File dropdown menu
    menus = ( 
        ("File",( ("New", evNew), 
            ("Resume", evResume), 
            ("Save", evSave),
            ("Open", evOpen), 
            ("Exit", evExit))),
        ("Help",( ("Help", evHelp), 
            ("About", evAbout)))
         )

    menubar = tk.Menu(parent) 
    for menu in menus: 
        m = tk.Menu(parent) 
        for item in menu[1]: 
            m.add_command(label=item[0], command=item[1])
        menubar.add_cascade(label=menu[0], menu=m) 
    
    return menubar

def evNew(): 
    status['text'] = "Playing game" 
    game2cells(oxo_logic.newGame())

def evResume ():
    status['text'] = "Playing game" 
    game = oxo_logic.restoreGame() 
    game2cells(game)

def evSave():
    game = cells2game() 
    oxo_logic.saveGame(game)

#Function for Open or the File Explorer
def evOpen():
    #Allows only .txt files to be read
    #Sets the default directory to the OS drive
    filename = askopenfile(mode = 'r', initialdir = "/", 
        title = "Select a Text File", 
        filetypes = (("Text files", "*.txt*"),
        ("all files", "*.*")))

    #Prints content if .txt exist
    if filename is not None:
        content = filename.read()
        print(content)

def evExit (): 
    if status['text'] == "Playing game":
        if mb.askyesno("Quitting","Do you want to save the game before quitting?"): 
            evSave()
    top.quit() 

#Added Open in the Help Selection
def evHelp ():
    mb.showinfo("Help",''' 
    File‐>New: starts a new game of tic‐tac‐toe 
    File‐>Resume: restores the last saved game and commences play
    File‐>Save: Saves current game.
    File‐>Open: Opens the File Explorer and allows text file read
    File‐>Exit: quits, prompts to save active game 
    Help‐>Help: shows this page
    Help‐>About: Shows information about the program and author''') 

def evAbout(): 
    mb.showinfo("About","Tic‐tac‐toe game GUI demo by Jason Moslares")

def evClick(row,col): 
    if status['text'] == "Game over": 
        mb.showerror("Game over", "Game over!") 
        return

    game = cells2game() 
    index = (3*row) + col 
    result = oxo_logic.userMove(game, index) 
    game2cells(game)

    if not result:
        result = oxo_logic.computerMove(game) 
        game2cells(game)
    if result == "D": 
        mb.showinfo("Result", "It's a Draw!") 
        status['text'] = "Game over"
    else: 
        if result =="X" or result == "O": 
            mb.showinfo("Result", "The winner is: {}".format(result))
            status['text'] = "Game over" 

def game2cells(game):
    table = board.pack_slaves()[0] 
    for row in range(3): 
        for col in range(3): 
            table.grid_slaves(row=row,column=col)[0]['text'] = game[3*row+col]

def cells2game(): 
    values = []
    table = board.pack_slaves()[0] 
    for row in range(3): 
        for col in range(3): 
            values.append(table.grid_slaves(row=row, column=col)[0]['text'])
    return values 

def buildBoard(parent):
    outer = tk.Frame(parent, border=2, relief="sunken") 
    inner = tk.Frame(outer) 
    inner.pack()
    
    for row in range(3): 
        for col in range(3): 
            cell = tk.Button(inner, text=" ", width="5", height="2", 
            command=lambda r=row, c=col : evClick(r,c) )
            cell.grid(row=row, column=col) 
    return outer


mbar = buildMenu(top) 
top["menu"] = mbar
    
board = buildBoard(top) 
board.pack() 
status = tk.Label(top, text="Playing game", border=0, background="lightgrey", foreground="red")
status.pack(anchor="s", fill="x", expand=True) 

tk.mainloop()