from tkinter import *
from tkinter import messagebox
import base64

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def openMessageBox(error_title,error_message):
    messagebox.showwarning(title=error_title, message=error_message)

def encyrpt_the_message_send_to_the_file():
    raw_message = enter_your_secret_input.get("1.0", END)
    title = enter_your_title_input.get()
    password = enter_master_key_input.get()



    if len(raw_message) == 0 or len(title) == 0 or len(password) == 0:
        error_title="Error!!"
        error_message="Please enter all the areas!"
        openMessageBox(error_title,error_message)
    else:
        #ENCYRIPTION
        encyrpted_message = encode(password, raw_message)



        try:
            with open("mysecret_file.txt", mode="a") as data_file:
                data_file.write(f"\n{title}\n{encyrpted_message}")
        except FileNotFoundError:
            with open("mysecret_file.txt", mode="w") as data_file:
                data_file.write(f"\n{title}\n{encyrpted_message}")

        finally:
            enter_your_secret_input.delete("1.0", END)
            enter_your_title_input.delete(0,END)
            enter_master_key_input.delete(0,END)



def get_from_the_file():
    key = enter_master_key_input.get()
    encyrpted_message = enter_your_secret_input.get("1.0", END)


    if len(encyrpted_message) == 0 or len(key) == 0:
        error_title="Error!!"
        error_message="Please enter all the areas!"
        openMessageBox(error_title,error_message)
    else:
        try:
            decyrpted_message = decode(key,encyrpted_message)
            enter_your_secret_input.delete("1.0",END)
            enter_your_secret_input.insert("1.0", decyrpted_message)
        except:
            error_title="Error!!"
            error_message="Please enter encyrpted message!"
            openMessageBox(error_title,error_message)

window = Tk()
window.width = 700  # Pencere genişliğini 400 piksel olarak ayarlar
window.height = 700  # Pencere yüksekliğini 300 piksel olarak ayarlar
window.config(padx=30, pady=15)

#UI
#resim
top_secret_image = PhotoImage(file= "image_top_secret.png")
image_label = Label(image=top_secret_image)
image_label.pack()
#enter your title labelı
enter_your_title_label = Label(text="Enter Your Title")
enter_your_title_label.pack()
#enter your title entrysi
enter_your_title_input = Entry(width=20)
enter_your_title_input.focus()
enter_your_title_input.pack()
#enter your secret labelı
enter_your_secret_label = Label(text="Enter Your Secret")
enter_your_secret_label.pack()
#enter your secret entrysi
enter_your_secret_input = Text(width=30,height=30)
enter_your_secret_input.pack()
#enter your key labelı
enter_master_key_label = Label(text="Enter Master Key")
enter_master_key_label.pack()
#enter your key entrysi
enter_master_key_input = Entry(width=20)
enter_master_key_input.pack()
#save-encrypt butonu
save_button = Button(text="Save and Encyrpt",command = encyrpt_the_message_send_to_the_file) #,command = encyrpt_message
save_button.pack()
#decrypt butonu
decyrpt_button = Button(text="Decyrpt",command =get_from_the_file )
decyrpt_button.pack()







window.mainloop()

