'''
Created on Jan 18, 2016

@author: lathian
Button object is instantiated two different times in the Blastn view. What makes it complicated is that it has to use
tk.Text box for a single line. tk.Text supports advanced formatting including having part of the string explaining
what pressing the button be blue and part be regular text. The reason I wrote this is that it mimics the appearance of
the web page. The BLAST button calls self.controller.blast in Blastn_Controller which assembles the needed command line
string and uses subprocess.Popen to pass in the command.
'''
import tkinter as tk
from tkinter import ttk
import Blastn_Controller as BC

class BLAST_Button(tk.Frame):
    def __init__(self, parent, controller, left_row_limit = 2, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.ROW = 1
        self.controller = controller
        self.parent = parent
        #buildMargins allows easy frame expansion and makes gridding easier
        self.left_row_limit = left_row_limit 
        #self.controller.buildMargins(self, self.left_row_limit)
        #BLAST text can be replaced with graphics
        self.BLAST_button = tk.Button(self, text = 'BLAST', command = self.controller.blast, foreground = 'black', 
                                      background = 'light sky blue')
        self.BLAST_button.grid ( row = 1, column = 1)
        
        self.text = tk.Text(self, width = 200, height = 2, bd = -1)
        self.text.tag_config('blue', foreground = 'light sky blue', font = 'arial 10 bold')
        self.text.tag_config('normal', font = 'arial 10')
        self.text.grid( row =1, column = 2, columnspan = 8, sticky = 'W')

        #Default text reflects default options of chose search set and program selection
        self.text.insert('end', 'Search ', ('normal'))
        self.text.insert('end', 'database Nucleotide collection (nr/nt) ', ('blue'))
        self.text.insert('end', 'using ', ('normal'))
        self.text.insert('end', 'Megablast (Optimize for highly similar sequences)', ('blue'))
        self.text.configure(state = 'disabled')


if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    
    blast_controller = BC.Blastn_Controller()
    blast_button = BLAST_Button(root, blast_controller)
    blast_button.grid(row = 0, column = 0)
    root.mainloop()   
