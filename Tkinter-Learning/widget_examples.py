from tkinter import *

#padx ve pady parametreleri ile boşluk açabiliriz.
#focus fonksiyonu imleci oradan başlatır

window = Tk()
window. title("Tkinter Python")
window.minsize(width=600,height=600)
window.config(padx=20, pady=20) #windowun içine doğru boşluk

my_label = Label(text="my label")
my_label.config(bg="orange")
my_label.config(fg="dark blue")
my_label.config(padx=10, pady=10)
my_label.pack()

def button_clicked():
    print("button clicked")
    print(my_entry.get())
    print(my_text.get("1.0", END)) #EN BAŞTAN SONA KADAR BAS
    #1.0 -> 1. satırın 0. indexinden itibaren bas demek

my_button = Button (text="button",command=button_clicked)
my_button.config(padx=10, pady=10)
my_button.pack()

#single-line
my_entry = Entry(width=20)
my_entry.pack()
my_entry.focus()

#uzun yazı yazmak için. multiline
my_text = Text(width=30)
my_text.pack()

#scale:
def scale_choice(value):
    print(value)
my_scale = Scale(from_=0, to=50, command=scale_choice)
my_scale.pack()

#spinbox
def spinbox_choice():
    print(my_spinbox.get())
my_spinbox= Spinbox(from_=0, to=50, command=spinbox_choice)
my_spinbox.pack()

#checkbutton
def checkbutton_selection():
    print(check_state.get())

check_state = IntVar() #tkinter kütüphanesinde, checkbox seçiliyken 1, değilken 0 olan bir nesne
my_cb = Checkbutton(text="check", variable=check_state, command=checkbutton_selection)
my_cb.pack()

#radio button
def radio_selected():
    print(radio_checked_state.get())
radio_checked_state = IntVar()
my_rb = Radiobutton(text="OPT-1", value=10, variable=radio_checked_state, command=radio_selected)
my_rb_2 = Radiobutton(text="OPT-2", value=20, variable=radio_checked_state, command=radio_selected)
my_rb.pack()
my_rb_2.pack()

#listbox

def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection()))

my_listbox = Listbox()
name_list = ["Faruk","Gökalp","Yüksel", "Mehmet "]
for i in range(len(name_list)):
    my_listbox.insert(i,name_list[i])
my_listbox.bind('<<ListboxSelect>>',listbox_selected)
my_listbox.pack()

window.mainloop()
