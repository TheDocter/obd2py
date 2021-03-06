"""
Programmer: JR Padfield
Description: Creates the entire gui and allows it to be updated
Version: 1
Date: 07/15/2014
"""
from tkinter import *
from tkinter import ttk
from obddata import *



class GUI(object):
    """ Handles all gui for the program """
    def create_gui(self):
        """ Initialize the root window of the program """
        # lets create a frame to hold out labels
        self.superframe = LabelFrame(self, padx=5, pady=5)
        self.superframe.grid(row=2, column=1)
        # create the notebook in master
        self.notebook = ttk.Notebook(self.superframe)
        self.notebook.grid(row=1, column=1)
        self.basicBook = ttk.Frame(self.notebook)
        self.advancedBook = ttk.Frame(self.notebook)
        self.notebook.add(self.basicBook, text="Basic Info")
        self.notebook.add(self.advancedBook, text="Advanced Info")

        # create mph/kph label
        self.mphLabel = Label(self.basicBook, text="0.0 MPH")
        self.mphLabel.grid(row=2, column=1)

        # create rpm label
        self.rpmLabel = Label(self.basicBook, text="0.0 RPM")
        self.rpmLabel.grid(row=2, column=2)

        # create oil temp label
        self.oilTempLabel = Label(self.basicBook, text="0.0 Degrees")
        self.oilTempLabel.grid(row=3, column=1)

        # create coolent temp label
        self.coolantTempLabel = Label(self.basicBook, text="0.0 Degrees")
        self.coolantTempLabel.grid(row=3, column=2)

        # create intake temp label
        self.intakeTempLabel = Label(self.basicBook, text="0.0 Degrees")
        self.intakeTempLabel.grid(row=4, column=1)

        # create engine load label
        self.engineLoadLabel = Label(self.basicBook, text="0.0 Engine Load")
        self.engineLoadLabel.grid(row=4, column=2)

        print("gui set up finished")

        # TODO: create a book to set new settings that can be saved

    def update_gui(self):
        """ Updates the text of the labels. This happens """
        print("Updating Text")

        self.mphLabel.config(text=str(OBDValues[0]) + " MPH")
        self.rpmLabel.config(text=str(OBDValues[1]) + " RPM")
        self.oilTempLabel.config(text=str(OBDValues[2]) + " Oil Temp")
        self.coolantTempLabel.config(text=str(OBDValues[3]) + " Coolant Temp")
        self.intakeTempLabel.config(text=str(OBDValues[4]) + " Intake Temp")
        self.engineLoadLabel.config(text=str(OBDValues[5]) + " Engine Load")
