'''
This is not my code. I found it at the below web sight. It is necessary because the default area that
tkinter tacks widgets to has a maximum size limit that is the size of the screen. So if you have 
widgets that go off the bottom of the screen you cannot have a scrollbar to scroll you down to them.
The answer is to use the tk.Canvas object along with a scrollbar.

Note:I did not bind the mouse wheel to the scrollbar as that is dicey; it turns out to be plaftform
dependent.
'''
# http://stackoverflow.com/questions/3085696/adding-a-scrollbar-to-a-grid-of-widgets-in-tkinter
# on Mac sometimes scrollbar sticks when window size is small.
import tkinter as tk
class ScrollableCanvas(tk.Frame):
    def __init__(self, root):

        tk.Frame.__init__(self, root)
        self.parent = root
        self.canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw", 
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        #self.populate()
    
    def populate(self):
        '''Put in some fake data'''
        for row in range(100):
            tk.Label(self.frame, text="%s" % row, width=3, borderwidth="1", 
                     relief="solid").grid(row=row, column=0)
            t="this is the second column for row %s" %row
            tk.Label(self.frame, text=t).grid(row=row, column=1)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    def getScrFrame(self):
        return self.frame

if __name__ == "__main__":
    root=tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    ScrollableCanvas(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
