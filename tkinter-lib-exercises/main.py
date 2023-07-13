import tkinter


def click_button():
    user_input = my_entry.get()
    print(user_input)

#pencere oluşturur, başlık atar, minimum boyutu belirler
my_window = tkinter.Tk()
my_window.title("TKinter Learning")
my_window.minsize(450,300)

#label: kullanıcıya metin göstermek için
my_label = tkinter.Label(
    text= "this is a label",
    font= ('Arial',30,"normal")
) #tüm parametreleri bilmediğimiz için ileride değişiklik yapmak istersek:
#config kullanırız..

my_label.config(bg="black", fg="white")

#label'ı pencerenin ortasında konumlandırmak için:
#my_label.pack() #grid ve place gibi metotlar da var
#my_label.place(x=0, y=0)
my_label.grid(row=0,column=0)

#button->  command p.metresi bir metot çalıştırır
my_button = tkinter.Button(text="test", command=click_button)
my_button.config(height=1, width=1)
#my_button.pack() #my_label'in altına koymak için
'''my_button.place(x=my_window.winfo_width()/2-my_button.winfo_width()/2 , y=my_window.winfo_height()/2-my_button.winfo_height()/2)
my_button.update()
'''
my_button.grid(row=1,column=0)

#entry: kullanıcıdan veri almak için
my_entry = tkinter.Entry(width=20)
#my_entry.pack()

#widgetların ekranda görünmesi için pack,place veya grid kullanmak zorundayız

#pack metodu programdaki sırasıyla ögeleri ortalayıp üst üste koyar
#pack'in "side" parametresi: top,bottom,left,right alır
#genel olarak yukarı,aşağı,sola,sağa yerleştirir.

#place metodu ise bize nereye koymak istediğimizi x,y olarak sorar

#grid metodu: önce kafamızda grid sistemi kurmalı, sonra da widget'a iki boyutlu diziye erişir gibi row,column vermeliyiz.




my_window.mainloop()
