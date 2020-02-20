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
    def __init__(self, window_title, *types):
        import tkinter
        from tkinter.filedialog import askopenfilename, asksaveasfilename

        self.window_title = window_title
        self.types = types
        if 'input' in self.types or len(types) == 0:
            self.inputfile = None
        if 'output' in self.types or len(types) == 0:
            self.outputfile = None


        def submit(self):
            if 'input' in self.types or len(types) == 0:
                self.inputfile =  inputFilePath.get()
            if 'output' in self.types or len(types) == 0:
                self.outputfile = outputFilePath.get()
            screen.destroy()
    

        def getFileName(self, window_title, EntryName):
            varName = askopenfilename(title=window_title)
            EntryName.insert(0, varName)


        screen = tkinter.Tk(className= self.window_title)
        screen.minsize(300, 80)
        if len(self.types) == 0 or "input" in self.types:
            inputFrame = tkinter.Frame(screen)
            inputFrame.pack(expand = 1, fill=tkinter.X)
            label1 = tkinter.Label(inputFrame, text= "קובץ קלט:"[::-1])
            label1.pack(side = tkinter.RIGHT)
            inputFilePath = tkinter.Entry(inputFrame)
            inputFilePath.pack(side = tkinter.RIGHT, expand = 1, fill=tkinter.X)
            btn1 = tkinter.Button(inputFrame, text="בחירה"[::-1], command = (lambda: getFileName(self, window_title = "בחר/י קובץ קלט", EntryName = inputFilePath)))
            btn1.pack(side = tkinter.RIGHT)

        if len(self.types) == 0 or "output" in self.types:
            outputFrame = tkinter.Frame(screen)
            outputFrame.pack(expand = 1, fill=tkinter.X)
            label2 = tkinter.Label(outputFrame, text= "קובץ פלט:"[::-1])
            label2.pack(side = tkinter.RIGHT)
            outputFilePath = tkinter.Entry(outputFrame)
            outputFilePath.pack(side = tkinter.RIGHT, expand = 1, fill=tkinter.X)
            btn2 = tkinter.Button(outputFrame, text="בחירה"[::-1], command = (lambda: getFileName(self, window_title = "בחר/י קובץ פלט", EntryName = outputFilePath)))
            btn2.pack(side = tkinter.RIGHT)

        ok = tkinter.Button(screen, text= "אישור"[::-1], command= lambda: submit(self))
        ok.pack()
        screen.mainloop()