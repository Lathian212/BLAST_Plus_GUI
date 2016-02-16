import tkinter as tk
from tkinter import ttk

class BLAST_Model(object):
    def __init__(self, controller, *args, **kwargs):
        #Default label frame width reset by setter in controller
        self.frame_width = 1500

