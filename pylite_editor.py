from tkinter import *
from tkinter import messagebox
import os
import sys
from tkinter.filedialog import *

class editor(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        #Preference Variables
        self.textspace_bg=StringVar(self)
        self.textspace_bg.set("#ffffff")
        self.textspace_fg=StringVar(self)
        self.textspace_fg.set("#000000")
        self.current_file="None"
        
        #Editor window begins
        self.title("Untitled"+" - "+"pylite")
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

        #Test Menu Configs
        testmenu = Menu(menubar, tearoff=0)
        testmenu.add_command(label="Test action", command=self.testaction)
        menubar.add_cascade(label="Test", menu=testmenu)
        
        #Shortcut Mapping
        self.bind_all("<Control-n>", self.file_new)
        self.bind_all("<Control-o>", self.file_open)
        self.bind_all("<Control-s>", self.file_save)
        self.bind_all("<Control-c>", self.edit_copy)
        
        self.config(menu=menubar) #Enable menubar
        
        #Introduce self.textspace
        self.textspace=Text(self, bg=self.textspace_bg.get(), fg=self.textspace_fg.get())
        self.textspace.pack(expand=True, fill=BOTH, side=LEFT)
    
        #Introduced Y Scrollbar   
        scrolly=Scrollbar(self, command=self.textspace.yview)
        scrolly.pack(side=LEFT, fill=Y)
        self.textspace['yscrollcommand'] = scrolly.set
        
        #Info Label
        #Pending
        self.current_line=StringVar(self, value=self.textspace.index(INSERT))
        self.infolabel=Label(self, textvariable=self.current_line).pack()
        self.bind_all("<Key>", self.update_line)
        self.bind_all("<Button-1>", self.update_line)
                
    #File Methods
    def file_new(self, *args):
        print("New file")
    def file_open(self, *args):
        print("Open file")
        print(self.current_file)
        self.current_file=askopenfilename(defaultextension=".py", filetypes=[("Python Files","*.py"),("Text Documents","*.txt"),("All Files","*.*")])
        print(self.current_file)
        print(type(self.current_file))
        print(self.textspace)
        if(self.current_file==""):
            self.current_file="None"
        else:
            file=open(self.current_file, 'r')
            self.textspace.insert(INSERT, file.read())
        self.update_line()
        self.title(self.current_file.split("/")[-1]+" - "+"pylite")
    def file_save(self, *args):
        print("Save file")
    def file_saveas(self):
        print("Save As file")
    def file_exit(self):
        exit_decision=messagebox.askquestion("Exit", "Do you want to exit pylite?")
        if exit_decision == "yes":
            self.destroy()
        else:
            pass
            
    
    #Edit Methods
    def edit_copy(self, *args):
        self.focus_get().event_generate('<<Copy>>')
    def edit_cut(self, *args):
        self.focus_get().event_generate('<<Cut>>')
    def edit_paste(self, *args):
        self.focus_get().event_generate('<<Paste>>')

    #Help Methods
    def help_about(self):
        messagebox.showinfo("About", "Welcome to pylite! Developed by sanketp60")

    #Test Methods
    def testaction(self):
        print("Test")
    def print_test(self, *args):
        print("Test")
        
    #Update Method (Annonymous)
    update_line=lambda self, *args: self.current_line.set(self.textspace.index(INSERT))
        
        
#Initialize editor
if __name__ == "__main__":
    app = editor()
    app.protocol("WM_DELETE_WINDOW", app.file_exit)
    app.mainloop()
