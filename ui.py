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
    def __init__(self, **kwargs):
        import tkinter
        from tkinter.filedialog import askopenfilename, asksaveasfilename

        for key in kwargs:                        # set arguments into private variables
            self.__dict__["_"+key] = kwargs[key]

        if "dir" not in kwargs:
            self._dir = "ltr"                    # default direction is left to right

        if "window_title" not in kwargs:
            if self._dir == "ltr":
                self._window_title = "Please choose file(s) path"
            else:
                self._window_title = "אנא בחרו את מיקום הקובץ"
        if 'types' not in kwargs:
            self._types = ["input", "output"]          # default behvaior: input + output path

        if 'label1' not in kwargs:                     # default labels per direction
            if self._dir == "ltr":
                self._label1 = "Choose input file path"
            else:
                self._label1 = "בחר/י מיקום קובץ קלט"
        
        if 'label2' not in kwargs:
            if self._dir == "ltr":
                self._label2 = "Choose output file path"
            else:
                self._label2 = "בחר/י מיקום קובץ פלט"

        if 'button1' not in kwargs:                  # default button text per direction
            if self._dir == "ltr":
                self._button1 = "Browse"
            else:
                self._button1 = "בחר/י"

        if 'button2' not in kwargs:
            if self._dir == "ltr":
                self._button2 = "Browse"
            else:
                self._button2 = "בחר/י"                

        if 'button_submit' not in kwargs:
            if self._dir == "ltr":
                self._button_submit = "Submit"
            else:
                self._button_submit = "אישור"

        if self._dir == "rtl":
            for key in ["_label1","_button1","_label2","_button2","_button_submit"]:
                self.__dict__[key] = self.__dict__[key][::-1]


        if 'input' in self._types:
            self.inputfile = None
        if 'output' in self._types:
            self.outputfile = None


        def submit(self):
            if 'input' in self._types:
                self.inputfile =  inputFilePath.get()
            if 'output' in self._types:
                self.outputfile = outputFilePath.get()
            screen.destroy()
    

        def getFileName(self, window_title, EntryName):
            if self._dir == "rtl":
                window_title = window_title[::-1]
            varName = askopenfilename(title=window_title)
            EntryName.insert(0, varName)

        screen = tkinter.Tk(className= self._window_title)
        screen.minsize(300, 80)
        if self._dir == "rtl":                                      # set the gui direction (ltr/rtl)
            self._direction = tkinter.RIGHT
        else:
            self._direction = tkinter.LEFT

        if "input" in self._types:
            inputFrame = tkinter.Frame(screen)
            inputFrame.pack(expand = 1, fill=tkinter.X)
            if self._dir == "rtl":
                label1 = tkinter.Label(inputFrame, text= ":"+self._label1)
            else:
                label1 = tkinter.Label(inputFrame, text= self._label1+":")
            label1.pack(side = self._direction)
            inputFilePath = tkinter.Entry(inputFrame)
            inputFilePath.pack(side = self._direction, expand = 1, fill=tkinter.X)
            btn1 = tkinter.Button(inputFrame, text=self._button1, command = (lambda: getFileName(self, self._label1, EntryName = inputFilePath)))
            btn1.pack(side = self._direction)

        if "output" in self._types:
            outputFrame = tkinter.Frame(screen)
            outputFrame.pack(expand = 1, fill=tkinter.X)
            if self._dir == "rtl":
                label2 = tkinter.Label(outputFrame, text= ":"+self._label2)
            else:
                label2 = tkinter.Label(outputFrame, text= self._label2+":")
            label2.pack(side = self._direction)
            outputFilePath = tkinter.Entry(outputFrame)
            outputFilePath.pack(side = self._direction, expand = 1, fill=tkinter.X)
            btn2 = tkinter.Button(outputFrame, text=self._button2, command = (lambda: getFileName(self, self._label2, EntryName = outputFilePath)))
            btn2.pack(side = self._direction)

        ok = tkinter.Button(screen, text= self._button_submit, command= lambda: submit(self))
        ok.pack()
        screen.mainloop()