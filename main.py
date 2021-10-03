from tkinter import *
import tkinter.messagebox
import backend
root=Tk()
root.title('Library-management-system')
root.geometry('800x700')
root.iconbitmap(r'C:/Users/ACER/Downloads/library.ico')
bg = PhotoImage(file="C:/Users/ACER/Downloads/school.png")
mylabel = Label(root, image=bg)
mylabel.place(x=0, y=0)

# ISBN which is international standard book number
def callback():
  if tkinter.messagebox.askokcancel("quit","Do You really want to quit?"):
    root.destroy()

def clear():
  e1.delete(0,END)
  e2.delete(0,END)
  e3.delete(0,END)
  e4.delete(0,END)

def add_entry():
  backend.insert(title_txt.get()
                 ,author_txt.get()
                 ,year_txt.get()
                 ,isbn_txt.get())
  listing.delete(0,END)
  listing.insert(END,(title_txt.get()
                      ,author_txt.get()
                      ,year_txt.get()
                      ,isbn_txt.get()))
  clear()

def view_all():
  listing.delete(0,END)
  for row in backend.view():
    listing.insert(END,row)
  clear()

def update():
  global selected_tuple
  backend.update(selected_tuple[0]
                 ,title_txt.get()
                 ,author_txt.get()
                 ,year_txt.get()
                 ,isbn_txt.get())
  view_all()

def get_selected_row(event):
  global selected_tuple
  clear()
  index=listing.curselection()[0]
  selected_tuple=listing.get(index)
  e1.insert(END,selected_tuple[1])
  e2.insert(END,selected_tuple[3])
  e3.insert(END,selected_tuple[2])
  e4.insert(END,selected_tuple[4])


def delete():
  global selected_tuple
  backend.delete(selected_tuple[0])
  view_all()

def search():
  listing.delete(0,END)
  search_data=backend.search(title_txt.get()
                             ,author_txt.get()
                             ,year_txt.get()
                             ,isbn_txt.get())
  if len(search_data)!=0:
    for row in search_data:
      listing.insert(END,row)
  else:
    tkinter.messagebox.showinfo('Message','NO RESULT FOUND')
  clear()

selected_tuple=tuple()
title_txt=StringVar()
author_txt=StringVar()
year_txt=StringVar()
isbn_txt=StringVar()



label1=Label(root,text='Book-Title',fg='red',bg='black',font=('STYLE_BRACEBAD, 15'),relief=RAISED)
label1.grid(row=0,column=0,padx=5,pady=5,sticky='nswe')
label2=Label(root,text='Publication-Year',fg='red',bg='black',font=('STYLE_BRACEBAD, 15'),relief=RAISED)
label2.grid(row=1,column=0,padx=5,pady=5,sticky='nswe')
entry1=Entry(root,textvariable=title_txt,font=('STYLE_BRACEBAD, 15'))
entry1.grid(row=0,column=1,padx=5,pady=5,sticky='nswe')
entry2=Entry(root,textvariable=year_txt,font=('STYLE_BRACEBAD, 15'))
entry2.grid(row=1,column=1,padx=5,pady=5,sticky='nswe')

label3=Label(root,text='Author',fg='red',bg='black',font=('STYLE_BRACEBAD, 15'),relief=RAISED)
label3.grid(row=0,column=2,padx=5,pady=5,sticky='nswe')
label4=Label(root,text='ISBN',fg='red',bg='black',font=('STYLE_BRACEBAD, 15'),relief=RAISED)
label4.grid(row=1,column=2,padx=5,pady=5,sticky='nswe')
entry3=Entry(root,textvariable=author_txt,font=('STYLE_BRACEBAD, 15'))

entry3.grid(row=0,column=3,padx=5,pady=5,sticky='nswe')
entry4=Entry(root,textvariable=isbn_txt,font=('STYLE_BRACEBAD, 15'))
entry4.grid(row=1,column=3,padx=5,pady=5,sticky='nswe')

buttonAll=Button(root,text='View All',fg='white',bg='black',font=('STYLE_BRACEBAD, 15'),command=view_all)
buttonAll.grid(row=2,column=3,padx=5,pady=5,sticky='nswe')
buttonSearch=Button(root,text='Search Entry',fg='white',bg='black',font=('STYLE_BRACEBAD, 15'),command=search)
buttonSearch.grid(row=3,column=3,padx=5,pady=5,sticky='nswe')
buttonEntry=Button(root,text='Add Entry',fg='white',bg='black',font=('STYLE_BRACEBAD, 15'),command=add_entry)
buttonEntry.grid(row=4,column=3,padx=5,pady=5,sticky='nswe')
buttonUpdate=Button(root,text='Update Selected',fg='white',bg='black',font=('STYLE_BRACEBAD, 15'),command=update)
buttonUpdate.grid(row=5,column=3,padx=5,pady=5,sticky='nswe')
buttonDelete=Button(root,text='Delete Selected',fg='white',bg='black',font=('STYLE_BRACEBAD, 15'),command=delete)
buttonDelete.grid(row=6,column=3,padx=5,pady=5,sticky='nswe')
buttonClose=Button(root,text='Close',fg='red',bg='black',font=('STYLE_BRACEBAD, 15'),command=root.destroy)
buttonClose.grid(row=7,column=3,padx=5,pady=5,sticky='nswe')


myFrame=Frame(root)


listing=Listbox(root,fg='red',bg='skyblue',font=('STYLE_BRACEBAD, 15'))
listing.grid(row=2,column=0,rowspan=6,columnspan=3,padx=5,pady=5,sticky='nswe')
listing.bind('<<ListboxSelect>>',get_selected_row)

for i in range(4):
  root.grid_columnconfigure(i,weight=1)
for i in range(8):
  root.grid_rowconfigure(i,weight=1)

root.protocol("WM_DELETE_WINDOW",callback)
root.mainloop()