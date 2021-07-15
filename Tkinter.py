from tkinter import *
from PyDictionary import PyDictionary

root=Tk()
pd=PyDictionary()

root.geometry("400x400")
root.title("my project")
root.config(bg="orange")

def printoutput():
  meaningans.config(text=pd.meaning(entry1.get())['Noun'][0])
  synonymans.config(text=pd.synonym(entry1.get())[0])
  antonymans.config(text=pd.antonym(entry1.get()))

label1=Label(root, text="Word Dicitionary")
label1.pack()

frame1=Frame(root)
label2=Label(frame1,text="Enter word" )
entry1=Entry(frame1)
button1=Button(frame1, text="Click me" ,command=printoutput)

frame1.pack()
label2.pack()
entry1.pack()
button1.pack()

frame2=Frame(root)
meaning=Label(frame2,text="Meaning" )
meaningans=Label(frame2,text="")
frame2.pack()
meaning.pack()
meaningans.pack()

frame3=Frame(root)
synonym=Label(frame3,text="Synonym" )
synonymans=Label(frame3,text="")
frame3.pack()
synonym.pack()
synonymans.pack()

frame4=Frame(root)
antonym=Label(frame4,text="Antonym" )
antonymans=Label(frame4,text="")
frame4.pack()
antonym.pack()
antonymans.pack()

root.mainloop()
