from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
#window.minsize(width=350, height=150)
window.config(padx=20, pady=20)

#Entry
miles_input = Entry(width=20)
miles_input.grid(column=1, row=0)

#Second Label
miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)

#Third Label
equal_label = Label(text="is equal to", font=("Arial", 12, "bold"))
equal_label.grid(column=0, row=1)

#Fourth Label
result_label = Label(text="0", font=("Arial", 12, "bold"))
result_label.grid(column=1, row=1)

#Fifth Label
km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)

#Button
calculate_button = Button(text="Click Me", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()