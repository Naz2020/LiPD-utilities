from tkinter import *
from tkinter import ttk
from tkinter import filedialog

LiPDgui = Tk()

LiPDgui.title("LiPD Utilities Interface")


# gets the file to work on
def getFile():
    fileSelected = filedialog.askopenfilename(title='Choose Input file')
    inputFile.set(fileSelected)


# gets the path for file output
def getFolderPath():
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)


# Stores input file
inputFile = StringVar()

# Stores output path
folderPath = StringVar()

# status set to default
status = "None pending"

# frame to hold  input/output
inOutFrame = Frame(LiPDgui, borderwidth=2, relief="ridge")
inOutFrame.grid(row=0, column=0)

# label for input entry box
fileLabel = Label(inOutFrame, text="Input File      ")
fileLabel.grid(row=0, column=0)

# label for Output entry box
outLabel = Label(inOutFrame, text="Output Directory")
outLabel.grid(row=2, column=0)

# file input entry box
fileIn = Entry(inOutFrame, textvariable=inputFile)
fileIn.grid(row=0, column=1)

# Output path entry box
outPath = Entry(inOutFrame, textvariable=folderPath)
outPath.grid(row=2, column=1)

# Input file Button
btnInputFile = ttk.Button(inOutFrame, text="  Choose File  ", command=getFile)
btnInputFile.grid(row=0, column=2)

# Output Path Button
btnBrowse = ttk.Button(inOutFrame, text="Browse Folder", command=getFolderPath)
btnBrowse.grid(row=2, column=2)

# frame to hold conversion divider
converdivFrame = Frame(LiPDgui, borderwidth=2, relief="ridge")
converdivFrame.grid(row=1, column=0)

# Divider label for conversion buttons
converLabel = Label(converdivFrame, text="Conversions")
converLabel.grid(row=0, column=0)

# frame to hold conversion buttons
converFrame = Frame(LiPDgui, borderwidth=2, relief="ridge")
converFrame.grid(row=2, column=0)

# Convert from excel Button
btnExcel = ttk.Button(converFrame, text="Excel to LiPD", )
btnExcel.grid(row=1, column=0)

# Convert from NOAA Button
btnNOAA = ttk.Button(converFrame, text="NOAA to LiPD", )
btnNOAA.grid(row=1, column=2)

converOutLabel = Label(converFrame, text="Process Status:  " + status)
converOutLabel.grid(row=3, column=0)

# frame to hold Time Series divider
timedivFrame = Frame(LiPDgui, borderwidth=2, relief="ridge")
timedivFrame.grid(row=3, column=0)

# Divider label for conversion buttons
timeLabel = Label(timedivFrame, text="Time Series Operations")
timeLabel.grid(row=0, column=1)

# frame to hold time series buttons
timeFrame = Frame(LiPDgui, borderwidth=2, relief="ridge")
timeFrame.grid(row=4, column=0)

# Time series Querry
btnQuery = ttk.Button(timeFrame, text="Query", )
btnQuery.grid(row=1, column=0)

# Time series Extract
btnExtract = ttk.Button(timeFrame, text="Extract", )
btnExtract.grid(row=1, column=1)

# Time series Filter
btnFilter = ttk.Button(timeFrame, text="Filter", )
btnFilter.grid(row=3, column=0)

# Time series Collapse
btnCollapse = ttk.Button(timeFrame, text="Collapse")
btnCollapse.grid(row=3, column=1)

timeOutLabel = Label(timeFrame, text="Process Status:  " + status)
timeOutLabel.grid(row=4, column=0)

LiPDgui.mainloop()
