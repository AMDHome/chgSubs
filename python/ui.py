import os, sys, webbrowser
from chgSubs import *
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import threading
import platform

class Root(Frame):
    def __init__(self, master):

        # init master
        Frame.__init__(self, master, width = 640, height = 520)
        self.master.title("chgSubs by AMDHome")
        self.master.geometry("640x520")             # default size
        self.master.minsize(640, 520)               # min size
        self.master.rowconfigure(0, weight = 1)     # allow for dynamic resizing in the vertical direction
        self.master.columnconfigure(0, weight = 1)  # allow for dynamic resizing in the horizontal direction

        # set window parameters
        self.grid(sticky = "NSEW")
        self.pack(fill = "both" , expand = True)
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)
        self.defautPadX = 20

        # set platform
        self.platform = platform.system()

        # set relevant filenames/paths
        self.download_path = "/"

        if getattr(sys, 'frozen', False):
            self.my_path = os.path.dirname(sys.executable)
        elif __file__:
            self.my_path = os.path.dirname(__file__)

        if os.path.isdir(os.path.expanduser("~/Downloads")):
            self.download_path = os.path.expanduser("~/Downloads")

        # draw window
        self.initBody()
        self.initFooter()   # progress bar/text and start button

        # populate advanced fields
        self.setAdvancedValues(self.getOptionMenuVal())



    # draw body of program
    def initBody(self):
        # draw invisible body frame
        self.body = Frame(self)
        self.body.grid(column = 0, row = 0, sticky="NSEW")
        self.body.columnconfigure(0, weight = 1)

        # draw body entities
        self.initVideoSelection()
        self.initFontSelection()
        self.initStyleSelector()

        self.initAdvanced()

        if self.platform == "Windows":
            self.initMKVToolNixSelection()



    # video selection box (box1) (Line 57 - 112)
    def initVideoSelection(self):
        # draw video title frame
        self.labelFrameVideo = LabelFrame(self.body, text = "Video")
        self.labelFrameVideo.grid(column = 0, row = 0, padx = self.defautPadX, pady = 10, sticky = "NEW")
        self.labelFrameVideo.columnconfigure(0, weight = 1)

        # callback registeration to check for valid file when selecting/entering path
        self.vVal = self.register(self.validVideo)

        # create video path variable and set default
        self.vFilename = StringVar()
        self.vFilename.set(self.download_path)

        # draw path text box/browse button
        self.openVideoEntry()
        self.openVideoButton()

    # draw video path textbox and populate with default values
    def openVideoEntry(self):
        self.OVEntry = ttk.Entry(self.labelFrameVideo, textvariable = self.vFilename, validate = 'all', validatecommand = (self.vVal, '%P'))
        self.validVideo(self.vFilename.get())
        self.OVEntry.grid(column = 0, row = 0, padx = 5, sticky = "EW")

    # draw video browse button
    def openVideoButton(self):
        self.OVButton = ttk.Button(self.labelFrameVideo, text = "Browse", command = self.browseVideoDialog)
        self.OVButton.grid(column = 1, row = 0, padx = 5, pady = 5, sticky = "E")

    # video browse window
    def browseVideoDialog(self):
        # set initial path
        initDir = self.vFilename.get();

        if os.path.isfile(initDir):
            initDir = os.path.dirname(initDir)
        elif not os.path.isdir(initDir):
            self.fFilename.set(self.download_path)

        # open file browse window and save selection
        selected = filedialog.askopenfilename(initialdir = initDir, title = "Select A File", filetypes = (("mkv file", "*.mkv"), ("All Files", "*.*")))
        if selected:
            self.vFilename.set(selected)

        # verify selected item is a file
        self.validVideo(self.vFilename.get())

    # color path based on valid/invalid file path (does not check for properly formattedvideo)
    def validVideo(self, inp):
        if not os.path.isfile(inp):
            self.OVEntry.configure(foreground ='red')
        else:
            self.OVEntry.configure(foreground ='black')
        return True



    # font selection box (box2) (Line 114 - 172)
    def initFontSelection(self):
        # draw font title frame
        self.labelFrameFont = LabelFrame(self.body, text = "Font")
        self.labelFrameFont.grid(column = 0, row = 1, padx = self.defautPadX, pady = 0, sticky = "NEW")
        self.labelFrameFont.columnconfigure(0, weight = 1)

        # callback registeration to check for valid file when selecting/entering path
        self.fVal = self.register(self.validFont)

        # create font path variable and set default
        self.fFilename = StringVar()
        if os.path.isfile(self.my_path + "/OpenSans-Semibold-Horrible.ttf"):
            self.fFilename.set(self.my_path + "/OpenSans-Semibold-Horrible.ttf")
        else:
            self.fFilename.set(self.my_path)

        # draw path text box/browse button
        self.openFontEntry()
        self.openFontButton()

    # draw font path textbox
    def openFontEntry(self):
        self.OFEntry = ttk.Entry(self.labelFrameFont, textvariable = self.fFilename, validate = 'all', validatecommand = (self.fVal, '%P'))
        self.validFont(self.fFilename.get())
        self.OFEntry.grid(column = 0, row = 0, padx = 5, sticky = "EW")

    # draw font browse button
    def openFontButton(self):
        self.OFButton = ttk.Button(self.labelFrameFont, text = "Browse", command = self.browseFontDialog)
        self.OFButton.grid(column = 1, row = 0, padx = 5, pady = 5, sticky = "E")

    # font browse window
    def browseFontDialog(self):
        # set inital path
        initDir = self.fFilename.get()

        if os.path.isfile(initDir):
            initDir = os.path.dirname(initDir)
        elif not os.path.isdir(initDir):
            self.fFilename.set(self.my_path)

        # open file browse window and save selection
        selected = filedialog.askopenfilename(initialdir = initDir, title = "Select A File", filetypes = (("mkv file", "*.mkv"), ("All Files", "*.*")))
        if selected:
            self.fFilename.set(selected)

        # verify selected item is a file
        self.validFont(self.fFilename.get())

    # color font based on valid/invalid file path (does not check for properly formatted font)
    def validFont(self, inp):
        if not os.path.isfile(inp):
            self.OFEntry.configure(foreground ='red')
        else:
            self.OFEntry.configure(foreground ='black')
        return True



    # style presete box (box3) (Line 174 - 219)
    def initStyleSelector(self):
        # draw preset title frame
        self.labelFrameStyle = LabelFrame(self.body, text = "Style Presets")
        self.labelFrameStyle.grid(column = 0, row = 2, padx = self.defautPadX, pady = 10, sticky="NEW")
        self.labelFrameStyle.columnconfigure(0, weight = 1)

        # dropdown options
        self.styleOptions = ["HorribleSubs", "Erai-raws", "Custom"]

        # callback registration to update advanced box values after selection
        self.selVal = self.register(self.updateAdvanced)

        # selection variable
        self.style = StringVar()
        self.style.set(self.styleOptions[0])

        # draw dropdown menu
        self.styleSelector = ttk.Combobox(self.labelFrameStyle, textvariable = self.style, values = self.styleOptions, validate = 'all', validatecommand = (self.selVal, '%P'))
        self.styleSelector.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = "NEW")

    # convert selection to a number value based on selected text
    def getOptionMenuVal(self):
        selectedStyle = self.style.get()

        if selectedStyle == "HorribleSubs":
            return 0
        elif selectedStyle == "Erai-raws":
            return 1
        else:
            return -1

    # set option though code
    def setOptionMenuVal(self, opt):
        self.style.set(self.styleOptions[opt])

    # check to see if entered/selected value is valid, then updates advanced box values through code
    def updateAdvanced(self, inp):
        if inp in self.styleOptions:
            self.styleSelector.configure(foreground ='black')
            self.setAdvancedValues(self.getOptionMenuVal())
        else:
            self.styleSelector.configure(foreground ='red')
        return True


    # advanced style properties box (box4) (Line 220 - 344)
    def initAdvanced(self):
        # draw advanced title frame
        self.labelFrameAdvanced = LabelFrame(self.body, text = "Style Properties (Advanced)")
        self.labelFrameAdvanced.grid(column = 0, row = 4, padx = self.defautPadX, pady = 0, sticky="NEW")
        self.labelFrameAdvanced.columnconfigure(1, weight = 1)

        # set built in defaults
        self.stylePresetOptions = [(848, 480, "Style: Default,Open Sans Semibold,36,&H00FFFFFF,&H000000FF,&H00020713,&H00000000,-1,0,0,0,100,100,0,0,1,1.7,0,2,0,0,28,0"),
                                   (1280, 720, "Style: Default,Open Sans Semibold,45,&H00FFFFFF,&H000000FF,&H00020713,&H00000000,-1,0,0,0,100,100,0,0,1,1.7,0,2,10,10,25,1")]

        # draw advanced section entries
        self.resXRow()
        self.resYRow()
        self.styleDetails()

    # draw label/spinbox for PlayResX values
    def resXRow(self):
        self.xVal = self.register(self.validX)      # callback registeration to check/format based on entered  PlayResX values

        # draw PlayResX label/spinbox
        self.labelX = Label(self.labelFrameAdvanced, text = "PlayResX: ")
        self.labelX.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = "EW")
        self.xEntry = ttk.Spinbox(self.labelFrameAdvanced, from_ = 1, to = 9999, validate = 'all', validatecommand = (self.xVal, '%P'))
        self.xEntry.grid(column = 1, row = 0, padx = 5, sticky = "EW")

    # draw label/spinbox for PlayResY values
    def resYRow(self):
        self.yVal = self.register(self.validY)      # callback registeration to check/format based on entered  PlayResY values

        # draw PlayResY label/spinbox
        self.labelY = Label(self.labelFrameAdvanced, text = "PlayResY: ")
        self.labelY.grid(column = 0, row = 1, padx = 5, pady = 5, sticky = "EW")
        self.yEntry = ttk.Spinbox(self.labelFrameAdvanced, from_ = 1, to = 9999, validate = 'all', validatecommand = (self.yVal, '%P'))
        self.yEntry.grid(column = 1, row = 1, padx = 5, sticky = "EW")

    # draw label/spinbox for stylecode details values
    def styleDetails(self):
        # draw stylecode label
        self.labelStyle = ttk.Label(self.labelFrameAdvanced, text = "Stylecode: ")
        self.labelStyle.grid(column = 0, row = 2, padx = 5, pady = 5, sticky = "EW")

        # draw "fake" stylecode textbox (hacky way of getting the theming to work like i want it to)
        self.styleTextOut = ttk.Entry(self.labelFrameAdvanced)
        self.styleTextOut.grid(column = 1, row = 2, padx = 5, pady = 5, sticky = "NSEW")
        self.styleTextOut.columnconfigure(0, weight = 1)

        # draw the real stylecode textbox over the fake stylecode textbox
        self.styleText = Text(self.styleTextOut, height = 4, wrap = WORD)
        self.styleText.configure(bd = "0")
        self.styleText.grid(column = 0, row = 0, padx = 1, pady = 1, sticky = "NSEW")
        self.styleText.bind("<KeyRelease>", self.updateCustomStyle)

    # Check to see if PlayResX is valid and color label appropriately
    def validX(self, inp):
        selectedStyle = self.getOptionMenuVal()
        status = self.validXY(inp)

        # change Preset to 'Custom' if necessary
        if selectedStyle != -1:
            if int(inp) != self.stylePresetOptions[selectedStyle][0]:
                self.setOptionMenuVal(-1)

        if inp == "":
            self.labelX.configure(foreground = 'red')
            return True
        elif status:
            self.labelX.configure(foreground = 'black')            

        return status;

    # Check to see if PlayResY is valid and color label appropriately 
    def validY(self, inp):
        selectedStyle = self.getOptionMenuVal()
        status = self.validXY(inp)

        # change Preset to 'Custom' if necessary
        if selectedStyle != -1:
            if int(inp) != self.stylePresetOptions[selectedStyle][1]:
                self.setOptionMenuVal(-1)

        if inp == "":
            self.labelY.configure(foreground = 'red')
            return True
        elif status:
            self.labelY.configure(foreground = 'black')           
            
        return status;

    # Make sure PlayResX/Y is an int greater then 0
    def validXY(self, inp):
        try:
            val = int(inp)
            if val < 1:  # if not a positive int print message and ask for input again
                return False
            return True
        except ValueError:
            return False 

    # validate Stylecode and color label approperately
    def updateCustomStyle(self, event):
        selectedStyle = self.getOptionMenuVal()
        content = event.widget.get("1.0", "end-1c")

        if content == "":
            self.labelStyle.configure(foreground = 'red')
        else:
            self.labelStyle.configure(foreground = 'black')       

        # Change Preset to 'Custom' if necessary
        if selectedStyle != -1:
            if content != self.stylePresetOptions[selectedStyle][2]:
                self.setOptionMenuVal(-1)

    # set advanced values based on preset change
    def setAdvancedValues(self, val):
        if val == -1:
            return
        else:
            self.xEntry.set(self.stylePresetOptions[val][0])
            self.yEntry.set(self.stylePresetOptions[val][1])
            self.styleText.delete('1.0', END)
            self.styleText.insert('1.0', self.stylePresetOptions[val][2])



    # MKVToolNix location box (box5) (Line 346 - 413)
    def initMKVToolNixSelection(self):
        # draw toolkit title frame
        self.labelFrameMKVTool = LabelFrame(self.body, text = "MKVToolNix Location")
        self.labelFrameMKVTool.grid(column = 0, row = 5, padx = self.defautPadX, pady = 10, sticky = "NEW")
        self.labelFrameMKVTool.columnconfigure(0, weight = 1)

        # callback registeration to check for valid folder path when selecting/entering path
        self.toolVal = self.register(self.validToolLocation)

        # create toolkit path variable and check default locations to set default path
        self.tFolder = StringVar()

        if os.path.isdir("C:\\Program Files\\MKVToolNix"):
            if self.checkFolderPrograms(os.listdir("C:\\Program Files\\MKVToolNix")):
                self.tFolder.set("C:\\Program Files\\MKVToolNix")
        elif os.path.isdir("C:\\Program Files (x86)\\MKVToolNix"):
            if self.checkFolderPrograms(os.listdir("C:\\Program Files (x86)\\MKVToolNix")):
                self.tFolder.set("C:\\Program Files (x86)\\MKVToolNix")
        else:
            self.tFolder.set(self.download_path)

        # draw frame contents
        self.toolPathEntry()
        self.toolPathButton()
        self.downloadLink()

    # draw toolkit path textbox and populate with default values
    def toolPathEntry(self):
        self.TPEntry = ttk.Entry(self.labelFrameMKVTool, textvariable = self.tFolder, validate = 'all', validatecommand = (self.toolVal, '%P'))
        self.validToolLocation(self.tFolder.get())
        self.TPEntry.grid(column = 0, row = 0, padx = 5, sticky = "EW")

    # draw toolkit folder browse button
    def toolPathButton(self):
        self.OVButton = ttk.Button(self.labelFrameMKVTool, text = "Browse Folder", command = self.browseToolPath)
        self.OVButton.grid(column = 1, row = 0, padx = 5, sticky = "E")

    # draw download link
    def downloadLink(self):
        self.dlLabel = Label(self.labelFrameMKVTool, text = "Click Here to download MKVToolNix", font="TkDefaultFont 7 underline", fg = "blue", cursor = "hand2")
        self.dlLabel.grid(column = 0, row = 1, padx = 5, sticky = "NW")
        self.dlLabel.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.fosshub.com/MKVToolNix.html"))

    # draw browse window
    def browseToolPath(self):
        # set initial path
        initDir = self.tFolder.get()

        if not os.path.isdir(initDir):
            self.tFolder.set(self.download_path)

        # open folder browse window and save selection
        selected = filedialog.askdirectory(initialdir = initDir, title = "Select MKVToolNix Folder", mustexist = True)
        if selected:
            self.tFolder.set(selected)

        # verify toolkit is at specified folder
        self.validToolLocation(self.tFolder.get())

    # color path based on valid/invalid folder path
    def validToolLocation(self, inp):
        if not os.path.isdir(inp):
            self.TPEntry.configure(foreground ='red')
        elif self.checkFolderPrograms(os.listdir(inp)):
            self.TPEntry.configure(foreground ='black')
        else:
            self.TPEntry.configure(foreground ='red')
        return True

    # checks to see if toolkit is actually in specified path
    def checkFolderPrograms(self, files):
        sansExt = map(lambda x: os.path.splitext(x)[0], files)
        return set(['mkvextract', 'mkvmerge', 'mkvpropedit']).issubset(list(sansExt))



    # footer (progress bar/status/button) (Line 415 - 491)
    def initFooter(self):
        # setup invisible footer frame
        self.footer = Frame(self)
        self.footer.grid(column = 0, row = 2, padx = self.defautPadX, pady = 6, sticky="SEW")
        self.footer.columnconfigure(0, weight = 1)

        # draw footer contents
        self.progressBar()
        self.startButton()

    # draw progress bar w/ status
    def progressBar(self):
        # draw progress bar
        self.progressB = ttk.Progressbar(self.footer, orient = HORIZONTAL, mode = "determinate", maximum = 7)
        self.progressB.grid(column = 0, row = 0, sticky = "EW")

        # create progress step variable
        self.progText = StringVar()
        self.progText.set("0/7")
        self.progressValue = 0

        # draw progress step text
        self.progressText = Label(self.footer, textvariable = self.progText, width = 6)
        self.progressText.grid(column = 1, row = 0, pady = 5, sticky = "E")

    # draw start button
    def startButton(self):
        # create button text variable
        self.sButtonText = StringVar()
        self.sButtonText.set("Start")

        # draw button
        self.sButton = ttk.Button(self.footer, textvariable = self.sButtonText, command = self.finalChecks)
        self.sButton.grid(column = 0, row = 1, pady = 7, columnspan = 2, sticky = "SEW")

    # start button command
    def finalChecks(self):
        # reset footer UI
        self.progText.set("0/7")
        self.progressValue = 0

        # check all variables to ensure validity
        validVars = self.checkVariables()
        
        # go
        if validVars == None:
            return
        else:
            self.sButtonText.set("Working...")
            self.startConversion(validVars)

    # start conversion using multithreading
    def startConversion(self, validVars):
        thread = threading.Thread(target = chgSubs, args=(self, *validVars))
        thread.start()

    # update footer function
    def updateProgress(self, message):
        self.progressValue += 1                                 # increment internal progress counter
        self.progText.set(str(self.progressValue) + "/7")       # update progress text
        self.progressB.step()                                   # update progress bar
        if message != None:
            self.sButtonText.set("Working...\t" + message)      # update progress status

    # stop with error message
    def processError(self, message):
        self.progressValue = 0
        self.progText.set(str(self.progressValue) + "-/7")
        if message != None:
            self.sButtonText.set("Error!\t" + message)

    # done command
    def done(self):
        self.progText.set("7/7")                                # update progress text
        self.progressB['value'] = 7                             # update progress bar
        self.sButtonText.set("Done!")                           # update progress status
        
        

    # final check to make sure everything is good before starting conversion
    def checkVariables(self):
        # get all variables
        mkv_location = self.vFilename.get()
        font_location = self.fFilename.get()
        propX = self.xEntry.get()
        propY = self.yEntry.get()
        propStyle = self.styleText.get("1.0",'end-1c')
        toolkit_location = ""                           # defined below

        # validate mkv_location
        if not os.path.isfile(mkv_location):
            self.sButtonText.set("Error: Please select a valid video file.")
            return None

        # validate font_location
        if not os.path.isfile(font_location):
            self.sButtonText.set("Error: Please select a valid font file.")
            return None

        # validate PlayResX value
        if propX == "":
            self.sButtonText.set("Error: The PlayResX field cannot be blank")
            return None

        try:
            temp = int(propX)
        except ValueError:
            self.sButtonText.set("Error: The PlayResX field is invalid")
            return None

        if temp < 1:
            self.sButtonText.set("Error: PlayResX must be greater than 0")
            return None

        # validate PlayResY value
        if propY == "":
            self.sButtonText.set("Error: The PlayResY field cannot be blank")
            return None

        try:
            temp = int(propY)
        except ValueError:
            self.sButtonText.set("Error: The PlayResY field is invalid")
            return None

        if temp < 1:
            self.sButtonText.set("Error: PlayResY must be greater than 0")
            return None

        # validate Stylecode
        if propStyle == "":
            self.sButtonText.set("Error: The Stylecode can not blank")
            return None

        # validate MKVToolNix location
        # on Windows
        if self.platform == "Windows":
            toolkit_location = self.tFolder.get() + "/"

            if not os.path.isdir(toolkit_location):
                self.sButtonText.set("Error: The MKVToolNix location must be a folder/directory")
                return None
        
            if not self.checkFolderPrograms(os.listdir(toolkit_location)):
                self.sButtonText.set("Error: A program is missing from the MKVToolNix location (mkvextract, mkvmerge, mkvpropedit)")
                return None
        
        # on other stuff
        else:
            if not checkMKVTools():
                self.sButtonText.set("Error: MKVToolNix missing. Please install the package mkvtoolnix using your package manager.")
                return None

        return (mkv_location, font_location, propX, propY, propStyle, toolkit_location)