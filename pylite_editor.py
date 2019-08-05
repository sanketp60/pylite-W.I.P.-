from tkinter import *
from tkinter import messagebox
import os
import sys

class editor(Tk):
    
    def __init__(self):
        Tk.__init__(self)

        #Preference Variables
        textspace_bg=StringVar()
        textspace_bg.set("#000066")
        textspace_fg=StringVar()
        textspace_fg.set("#ffffff")
        #Editor window begins
        self.title("pylite")
    
        menubar = Menu(self)

        #File Menu Configs
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New          CTRL+N", command=self.file_new)
        filemenu.add_command(label="Open...     CTRL+O", command=self.file_open)
        filemenu.add_command(label="Save          CTRL+S", command=self.file_save)
        filemenu.add_command(label="Save As...", command=self.file_saveas)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.file_exit)
        menubar.add_cascade(label="File", menu=filemenu)

        #Edit Menu Configs
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Copy      CTRL+C", command=self.edit_copy)
        editmenu.add_command(label="Cut         CTRL+X", command=self.edit_cut)
        editmenu.add_command(label="Paste      CTRL+V", command=self.edit_paste)
        menubar.add_cascade(label="Edit", menu=editmenu)

        #Help Menu COnfigs
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.help_about)
        menubar.add_cascade(label="Help", menu=helpmenu)
        
        #Shortcut Mapping
        self.bind_all("<Control-n>", self.file_new)
        self.bind_all("<Control-o>", self.file_open)
        self.bind_all("<Control-s>", self.file_save)
        self.bind_all("<Control-c>", self.edit_copy)
        
        self.config(menu=menubar) #Enable menubar

        
        #Introduce textspace
        textspace=Text(self, bg=textspace_bg.get(), fg=textspace_fg.get())
        textspace.pack(expand=True, fill=BOTH, side=LEFT)

        scrolly=Scrollbar(self, command=textspace.yview)
        scrolly.pack(side=RIGHT, fill=Y)
        textspace['yscrollcommand'] = scrolly.set


        
    #File Methods
    def file_new(self, *args):
        print("New file")
    def file_open(self, *args):
        print("Open file")
    def file_save(self, *args):
        print("Save file")
    def file_saveas(self):
        print("Save As file")
    def file_exit(self):
        exit_decision=messagebox.askquestion("Exit", "Do you want to exit pylite?")
        if exit_decision == "yes":
            self.destroy()
        else:
            return
            
    
    #Edit Methods
    def edit_copy(self, *args):
        self.focus_get().event_generate('<<Copy>>')
    def edit_cut(self, *args):
        self.focus_get().event_generate('<<Cut>>')
    def edit_paste(self, *args):
        self.focus_get().event_generate('<<Paste>>')

    #Help Methods
    def help_about(self):
        messagebox.showinfo("About",
        """Welcome to pylite! Developed by sanketp60""")
    
        
        
#Initialize editor
if __name__ == "__main__":
    app = editor()
    app.mainloop()
