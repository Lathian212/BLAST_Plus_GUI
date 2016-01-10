'''
Created on Jan 9, 2016

@author: lathian
'''
import BLASTn as bn
import tkinter as tk
from tkinter import ttk
import ScrollableCanvas as sc 


root = tk.Tk()
root.title('GUI for NCBI Blast+')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
"""Use scrollable canvas case in case widgets go vertical past the height of the screen"""
sCanvas = sc.ScrollableCanvas(root)
sFrame = sCanvas.getScrFrame()
"""Put in cell blocks that will later be made invisible to get grid manager to be more predictable"""
for col in range(20):
    ttk.Label(sFrame, text= '%s' % (col+1) , width =10).grid(row = 0, column = (col+1))
for row in range(100):
    ttk.Label(sFrame, text= '%s' % row, width = 3).grid(row = row, column = 0)
    
ttk.Label(sFrame, text = 'For using NCBI command line BLAST+ tools in remote batch configuration:').grid(row =2 , column = 7,
                                                                                                        columnspan = 10, sticky = 'W')

"""Use notebook widget to create tabs for each of the 5 Blast tools"""
#Template code for tabs from Python GUI Programming CookBook by Burkhard A. Meier 
# Tab Control introduced here -----------------------------------------
tabControl = ttk.Notebook(sFrame)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text='blastn')

tab2 = ttk.Frame(tabControl)            
tabControl.add(tab2, text='blastp')

tab3 = ttk.Frame(tabControl)            
tabControl.add(tab3, text='blastx')  

tab4 = ttk.Frame(tabControl)            
tabControl.add(tab4, text='tblastn')

tab5 = ttk.Frame(tabControl)            
tabControl.add(tab5, text='tblastx')      

tabControl.grid(row = 4, column = 1, rowspan = 200, columnspan = 20,  sticky = 'NW')  # Pack to make visible

#Now associate each BLAST page with its appropriate tab
blastn = bn.BLASTn(tab1)
#Has to bee gridded onto tab1 to show
blastn.grid(row = 0, column = 0)

root.mainloop() 