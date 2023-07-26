#!/usr/bin/env python
# coding: utf-8

# In[32]:


import tkinter as tk

window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

def fahrenheit_to_celsius():

    fahrenheit = ent_temperature.get()
    celsius = (float(fahrenheit) - 32) * 5/9
    celsius = round(celsius, 2)
    lbl_result["text"] = f"{celsius} \N{DEGREE CELSIUS}"

frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=40)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

btn_convert = tk.Button(
    master=window, 
    text="\N{RIGHTWARDS BLACK ARROW}", 
    command=fahrenheit_to_celsius
)

lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

btn_convert.grid(row=0, column=1, pady=10)
frm_entry.grid(row=0,column=0, padx=10)
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w") 
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()


# In[ ]:




