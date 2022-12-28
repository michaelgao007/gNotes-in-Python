from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk
import re

class notesSearch(Frame):

	def __init__(self,root):

		Frame.__init__(self,root,pady = 10)
		self.grid(row = 0,column = 0, sticky = "we")
		self.create_widgets()

	def exit_program(self):

		root.quit()
		root.destroy()
		exit()
		
	def search(self):
	
		self.msgText.config(state = 'normal')
		self.msgText.delete('1.0',END)
		self.msgText.tag_config('text',foreground='black',font=('Arial', 12,'bold'))
	
		notesFile = "dayLog.txt"
		notesDict = {}
		keyWord = self.keyword.get()
		lineCursor = 0
		searchResult = ""

		with open(notesFile, "r") as f:

			dictLineNum = 0

			for line in f:

				notesDict[dictLineNum] = line.strip()
				dictLineNum = dictLineNum + 1

		while lineCursor < len(notesDict.keys()):

			if re.search(r'^\d\d?\..*{}'.format(keyWord), notesDict[lineCursor]) != None:

				self.msgText.insert(END, notesDict[lineCursor] + "\n")
				lineCursor = lineCursor + 1

				while re.search(r'(^\d\d?\.)', notesDict[lineCursor]) == None:

					self.msgText.insert(END, notesDict[lineCursor] + "\n")
					lineCursor = lineCursor + 1

					if lineCursor >= len(notesDict.keys()):

						self.msgText.config(state = 'disabled')
						self.keyword.set('')
						return searchResult

			else:

				lineCursor = lineCursor + 1

				if lineCursor >= len(notesDict.keys()):

					self.msgText.config(state = 'disabled')
					self.keyword.set('')
					return searchResult
								

	def create_widgets(self):

		#--------------Status Panel--------------#
		self.statusPanel = LabelFrame(self,text = 'Main Panel', width = 780, height = 1050)
		self.statusPanel.pack(fill = 'both',padx=2)

		self.keyword_Label = Label(self.statusPanel,width = 12,text = 'Keyword:',foreground = 'red')
		self.keyword_Label.grid(row = 0,column = 0,sticky = 'e')

		self.keyword = StringVar()
		self.keyword_Entry = Entry(self.statusPanel,textvariable = self.keyword)
		self.keyword_Entry.grid(row = 0,column = 1,sticky = 'we')
		self.keyword_Entry.focus()

		self.searchButton = Button(self.statusPanel,text = 'Search', command = self.search)
		self.searchButton.grid(row = 0,column = 2,sticky = 'e',padx = 10,pady = 3)

		self.exitButton = Button(self.statusPanel, text = 'Exit',command = self.exit_program)
		self.exitButton.grid(row = 0, column = 4 ,sticky = 'e', padx =10,pady = 3)

		#--------------END of Status Panel--------------#

		#--------------Message Panel--------------#
		self.msgPanel = LabelFrame(self,text = 'Message Panel')
		self.msgPanel.pack(fill='both')

		self.msgText = scrolledtext.ScrolledText(self.msgPanel,wrap = 'word',state = 'disabled')
		self.msgText.grid(row = 0,column = 0,sticky = 'NEWS')
		
if __name__ == "__main__":

	root=Tk()
	root.title("gNotes v1.0")
	root.resizable(0,0)
	notesSearch(root)
	root.mainloop()
	