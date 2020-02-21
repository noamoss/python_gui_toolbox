class IntputOutputPath:
    """"
        Gui to ask for input and output files path.
    initiate:
            import InputOutputPath
            a = InputOutputPath()
    output:
        a.inputfile
        a.outputfile
    """
    def __init__(self, window_title="Please choose file(s) path", **kwargs):
        import tkinter
        from tkinter.filedialog import askopenfilename, asksaveasfilename

        self.__dict__.update(kwargs)
        self.window_title = window_title

        if "dir" not in kwargs:
            self.dir = "ltr"                    # default direction is left to right

        if 'types' not in kwargs:
            self.types = ["input", "output"]          # default behvaior: input + output path

        if 'label1' not in kwargs:                     # default labels per direction
            if self.dir == "ltr":
                self.label1 = "Choose input file path:"
            else:
                self.label1 = "בחר/י מיקום קובץ קלט:"
        
        if 'label2' not in kwargs:
            if self.dir == "ltr":
                self.label2 = "Choose output file path:"
            else:
                self.label2 = "בחר/י מיקום קובץ פלט:"

        if 'button1' not in kwargs:                  # default button text per direction
            if self.dir == "ltr":
                self.button1 = "Browse"
            else:
                self.button1 = "בחר/י"

        if 'button2' not in kwargs:
            if self.dir == "ltr":
                self.button2 = "Browse"
            else:
                self.button2 = "בחר/י"                

        if 'button_submit' not in kwargs:
            if self.dir == "ltr":
                self.button_submit = "Submit"
            else:
                self.button_submit = "אישור"

        if self.dir == "rtl":
            for key in ["label1","button1","label2","button2","button_submit"]:
                self.__dict__[key] = self.__dict__[key][::-1]


        if 'input' in self.types:
            self.inputfile = None
        if 'output' in self.types:
            self.outputfile = None
        print(vars(self))

        def submit(self):
            if 'input' in self.types:
                self.inputfile =  inputFilePath.get()
            if 'output' in self.types:
                self.outputfile = outputFilePath.get()
            screen.destroy()
    

        def getFileName(self, window_title, EntryName):
            varName = askopenfilename(title=window_title)
            EntryName.insert(0, varName)

        screen = tkinter.Tk(className= self.window_title)
        screen.minsize(300, 80)
        if self.dir == "rtl":                                      # set the gui direction (ltr/rtl)
            self.direction = tkinter.RIGHT
        else:
            self.direction = tkinter.LEFT

        if len(self.types) == 0 or "input" in self.types:
            inputFrame = tkinter.Frame(screen)
            inputFrame.pack(expand = 1, fill=tkinter.X)
            label1 = tkinter.Label(inputFrame, text= self.label1)
            label1.pack(side = self.direction)
            inputFilePath = tkinter.Entry(inputFrame)
            inputFilePath.pack(side = self.direction, expand = 1, fill=tkinter.X)
            btn1 = tkinter.Button(inputFrame, text=self.button1, command = (lambda: getFileName(self, window_title = "בחר/י קובץ קלט", EntryName = inputFilePath)))
            btn1.pack(side = self.direction)

        if len(self.types) == 0 or "output" in self.types:
            outputFrame = tkinter.Frame(screen)
            outputFrame.pack(expand = 1, fill=tkinter.X)
            label2 = tkinter.Label(outputFrame, text= self.label2)
            label2.pack(side = self.direction)
            outputFilePath = tkinter.Entry(outputFrame)
            outputFilePath.pack(side = self.direction, expand = 1, fill=tkinter.X)
            btn2 = tkinter.Button(outputFrame, text=self.button2, command = (lambda: getFileName(self, window_title = "בחר/י קובץ פלט", EntryName = outputFilePath)))
            btn2.pack(side = self.direction)

        ok = tkinter.Button(screen, text= self.button_submit, command= lambda: submit(self))
        ok.pack()
        screen.mainloop()