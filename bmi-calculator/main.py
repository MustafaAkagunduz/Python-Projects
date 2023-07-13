from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.config(padx=30, pady=30)
window.configure(bg="yellow")



def calculate_bmi():
    person_height = height_input.get()
    person_weight = weight_input.get()
    if person_weight == "" or person_height == "":
        result_label.config(text="Enter both weight and height!")
    else:
        try:
            bmi = float(person_weight) / ((float(person_height) / 100) ** 2)
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number!")


weight_input_label = Label(text="Enter Your Weight (kg)")
weight_input_label.pack()
weight_input = Entry(width=10)
weight_input.pack()
height_input_label = Label(text="Enter Your Height (cm)")
height_input_label.pack()
height_input = Entry(width=10)
height_input.pack()
calculate_button = Button(text="Calculate", command=calculate_bmi)
calculate_button.pack()
result_label = Label()
result_label.pack()


def write_result(bmi):
    result_string = f"Your BMI is {round(bmi, 2)}. You are "
    if bmi <= 16:
        result_string += "severely thin!"
        window.configure(bg="blue")
    elif 16 < bmi <= 17:
        result_string += "moderately thin!"
        window.configure(bg="blue")
    elif 17 < bmi <= 18.5:
        result_string += "mild thin!"
        window.configure(bg="blue")
    elif 18.5 < bmi <= 25:
        result_string += "normal weight"
        window.configure(bg="green")
    elif 25 < bmi <= 30:
        result_string += "overweight"
        window.configure(bg="red")
    elif 30 < bmi <= 35:
        result_string += "obese class 1"
        window.configure(bg="red")
    elif 35 < bmi <= 40:
        result_string += "obese class 2"
        window.configure(bg="red")
    else:
        result_string += "obese class 3"
        window.configure(bg="red")
    return result_string


window.mainloop()
