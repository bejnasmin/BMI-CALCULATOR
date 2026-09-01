import tkinter

window = tkinter.Tk()
window.title("BMI CALCULATOR")
window.config(width=400, height=400)



def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get() 
   
    if weight == "" or height == "":
        result_label.config(text="Please enter both weight and height!") 
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
            
        except ValueError:
            result_label.config(text="Please enter valid numbers for weight and height!")
        
#ui
weight_input_label = tkinter.Label(text="Enter your weight (kg):")
weight_input_label.pack()

weight_input = tkinter.Entry(width=10)
weight_input.pack() 

height_input_label = tkinter.Label(text="Enter your height (m):")
height_input_label.pack()

height_input = tkinter.Entry(width=10)
height_input.pack()

button = tkinter.Button(text="Calculate",command=calculate_bmi)
button.pack()   

result_label = tkinter.Label()
result_label.pack()

def write_result(bmi):
    result_string=f"Your BMI is: {bmi} You are "
    if bmi <= 16:
        result_string += "Severely thin!"
    elif bmi > 16 and bmi <=17:
        result_string += "Moderately thin!"
    elif bmi > 17 and bmi <=18.5:
        result_string += "Mildly thin"
    elif bmi > 18.5 and bmi <=25:
        result_string += "Normal"
    elif bmi > 25 and bmi <=30:
        result_string += "Overweight"
    elif bmi > 30 and bmi <=35:
        result_string += "Obese Class I"
    elif bmi > 35 and bmi <=40:
        result_string += "Obese Class II"
    else:
        result_string += "Obese Class III"
        
    return result_string
    



window.mainloop()