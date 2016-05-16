'''
Created on Jan 9, 2016

@author: lathian
Main implements the NoteBook widget that comes from the more advanced ttk extension of tk. This would
have allowed increased performance because flipping between the tabs does not require TCL to call
'forget' or 'destroy' methods on the widgets that need to be hidden and so metadata such as whether
there is text in an Entry Box is also preserved.

tk.Styles is a prowerful; albiet arcanely implemented; way of changing the global appearance of the
widgets. Here I just used it to thinken up the frame borders so each view object is clearly 
deliniated from the other as in the web page.
'''
import BLASTn as bn
import tkinter as tk
from tkinter import ttk
import ScrollableCanvas as SC 

root = tk.Tk()
root.title('GUI for NCBI Blast+')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
#Set up a style modification for labelframe objects so their border is visible in the mac
styles = ttk.Style()
#print('TFrame layout = ' + str(self.styles.layout('TFrame')))
#print('Frame.border options = ' + str(self.styles.element_options('Frame.border')))
styles.configure('TLabelframe', borderwidth = '5')

"""Use scrollable canvas case in case widgets go vertical past the height of the screen"""
sCanvas = SC.ScrollableCanvas(root)
sFrame = sCanvas.getScrFrame()
#HF.buildMargins(sFrame, 100)

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
"""
themes = ttk.Style()
print (themes.theme_names())
print('From main: Theme Being Used' + themes.theme_use())
"""

root.mainloop() 
