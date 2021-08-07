from tkinter import *
from tkinter.messagebox import *
window = Tk()
window.geometry("400x365")
window.title("calculator")

def allclear():
    textbox.delete(0,END)
def clear1():
    fetchdata1=textbox.get()
    fetchdata1=fetchdata1[0:len(fetchdata1)-1]
    textbox.delete(0,END)
    textbox.insert(0,fetchdata1)


#Buttoncick function, binding buttons
def buttonclick(event):   # print("button clicked")
    b = event.widget
    btext = b['text']

    if btext == "x":
        textbox.insert(END, '*')
        return;

    if btext == '=':
        try:
            fetch = textbox.get()
            ans = eval(fetch)
            textbox.delete(0,END)
            textbox.insert(0,ans)
        except Exception as e:
            print("error  ",e)
            showerror("error",e)

        return;

    textbox.insert(END, btext)


hadder1 = Label(window, text="MY CALCULATOR", font="Vardana 20 bold italic underline")
hadder1.pack(side=TOP)

# text box
textbox = Entry(window, font="Arial 20 italic", justify=RIGHT, bg="yellow")
textbox.pack(side=TOP, fill=X, padx=7, pady='5')

# button create
buttonframe = Frame(window)
buttonframe.pack(side=TOP)

t = 1
for i in range(0, 3):
    for j in range(0, 3):
        button1 = Button(buttonframe, text=t, width=5, font="Arial 20 bold", bg="light blue", activebackground="black",
                         activeforeground="white")
        button1.grid(row=i, column=j)
        t = t + 1
        button1.bind('<Button-1>', buttonclick)
zero = Button(buttonframe, text="0", width=5, font='Arial 20 bold', bg="light green", relief='ridge')
zero.grid(row=3, column=1)

dot = Button(buttonframe, text=".", width=5, font="Arial 20 bold", bg='light green', relief='ridge')
dot.grid(row=3, column=0)

equel = Button(buttonframe, text="=", width=5, font="Arial 20 bold", bg='light green', relief='ridge')
equel.grid(row=3, column=2)

plus = Button(buttonframe, text="+", width=5, font="Arial 20 bold", bg='brown', fg='light gray', relief='groove')
plus.grid(row=0, column=3)

minus = Button(buttonframe, text="-", width=5, font="Arial 20 bold", bg='brown', fg='light gray', relief='groove')
minus.grid(row=1, column=3)

multiply = Button(buttonframe, text="x", width=5, font='Vardana 20 bold', bg='brown', fg='light gray', relief='groove')
multiply.grid(row=2, column=3)

divide = Button(buttonframe, text="/", width=5, font='Vardana 20 bold', bg='brown', fg='light gray', relief='groove')
divide.grid(row=3, column=3)

clear = Button(buttonframe, text="CLEAR", font="Arial 20 bold", width=11, bg='pink',command=clear1)
clear.grid(row=4, column=2, columnspan=2)

Allclear = Button(buttonframe, text="AC", font="Vardana 20 bold", width=11, relief='ridge', bg='red',command=allclear)
Allclear.grid(row=4, column=0, columnspan=2)


# BINDING all Buttons
zero.bind('<Button-1>', buttonclick)
minus.bind('<Button-1>', buttonclick)
plus.bind('<Button-1>', buttonclick)
dot.bind('<Button-1>', buttonclick)
divide.bind('<Button-1>', buttonclick)
multiply.bind('<Button-1>', buttonclick)
equel.bind('<Button-1>', buttonclick)



window.mainloop()
