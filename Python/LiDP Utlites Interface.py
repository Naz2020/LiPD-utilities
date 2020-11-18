from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import lipd

LiPDgui = Tk()

LiPDgui.title("LiPD Utilities Interface")


# gets the file to work on
def getFile():
    fileSelected = filedialog.askopenfilename(title='Choose Input file')
    inputFile.set(fileSelected)

    if fileSelected.endswith(".xlsx"):
        lipd.readExcel(usr_path=fileSelected)
    elif fileSelected.endswith(".lpd"):
        lipd.readLipd(usr_path=fileSelected)
    elif fileSelected.endswith(".txt"):
        lipd.readNoaa(usr_path=fileSelected)



# gets the path for file output
def getFolderPath():
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)

def timeScollapse():
	lipd.collapseTs(list=None)
	lipd.collapse()
	CollTs = lipd.readLipd()
	list =lipd.extractTs()
	new_list = lipd.collapseTs(list) 
#Parameters:
#dict – Metadata
#paleData (bool) – Create a paleData time series
#return list: Time series
def timesExtract():
	lipd.timesExtract(dict,paleData=False)
	dict = lipd.readLipd()
	pale = lipd.extract(dict)
	lipd.extract()
	#return list:

#Return list new_list: 	
#	Filtered time series that matches the expression
def timesFilter():
	lipd.timesFilter(list,str)
	lipd.filter()
	filTs = lipd.loadLipd()
	list =lipd.extractTs(filTs)
	new_list = filterTs(list,"archiveType == marine sediment")
	new_list=filterTs(list,"paleoData_variableName == sst")
	#return list new_list:

# list = time series
#str = Expression
# return list_idx
#	indices of entries that match the criteria
def timeSquery():
	lipd.queryTs(list,str)
	lipd.query()
	timeseries_QueryTs = lipd.loadLipd()
	list = lipd.extractTs(timeseries_QueryTs)
	matches = queryTs(list,"archiveType == marine sediment")
	matches = queryTs(list,"geo_meanElev <=2000")
	#return list:
    
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
btnExcel = ttk.Button(converFrame, text="Excel to LiPD", command=lipd.excel)
btnExcel.grid(row=1, column=0)

# Convert from NOAA Button menu
btnNOAA = ttk.Button(converFrame, text="NOAA to LiPD", command=lipd.noaa)
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
btnQuery = ttk.Button(timeFrame, text="Query", command=lipd.querry)
btnQuery.grid(row=1, column=0)

# Time series Extract
btnExtract = ttk.Button(timeFrame, text="Extract",command=lipd.extract )
btnExtract.grid(row=1, column=1)

# Time series Filter
btnFilter = ttk.Button(timeFrame, text="Filter", command=lipd.filter)
btnFilter.grid(row=3, column=0)

# Time series Collapse
btnCollapse = ttk.Button(timeFrame, text="Collapse", command=lipd.collapse)
btnCollapse.grid(row=3, column=1)

timeOutLabel = Label(timeFrame, text="Process Status:  " + status)
timeOutLabel.grid(row=4, column=0)
LiPDgui.resizable(width=False, height=False)
LiPDgui.mainloop()
