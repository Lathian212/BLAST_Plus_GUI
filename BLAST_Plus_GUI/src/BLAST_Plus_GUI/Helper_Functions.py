'''
Created on Jan 18, 2016

@author: lathian
'''
import tkinter as tk
from tkinter import ttk

def buildMargins(self, left_row_limit):
        """This method makes cells along the top and right side of the frame so that gridding can easier when it's time to place widgets""" 
        for col in range(10):
            ttk.Label(self, text= '%s' % (col+1) , width =10).grid(row = 0, column = (col+1))
        for row in range(left_row_limit):
            ttk.Label(self, text= '%s' % row, width = 3).grid(row = row, column = 0)
            
def makeWidgetWidthEven (self, set_width, widget):
    """Resizes widget to set_width"""
    self.parent.update()
    widget_height = widget.winfo_height()
    #Turn off propagate which sets widget size based on what it contains and what it is contained in
    widget.grid_propagate(0)
    widget.configure (width = set_width, height = widget_height)
    return widget