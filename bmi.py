#! /user/bin/env/python3
import tkinter

def btn_click():
    height = float(height_box.get())
    weight=float(weight_box.get())
    BMI=weight/(height*height)

    bmi_box.delete(0, tkinter.END)

    bmi_box.insert(0, BMI)

tki = tkinter.Tk()
tki.geometry('400x300')
tki.title('BMI計算')

height_lavel = tkinter.Label(text='身長[m]')
height_lavel.place(x=60, y=50)
weight_lavel = tkinter.Label(text='体重')
weight_lavel.place(x=60, y=80)
area_lavel = tkinter.Label(text='BMI')
area_lavel.place(x=60, y=230)

height_box = tkinter.Entry(width=20)
height_box.place(x=140, y=50)
weight_box = tkinter.Entry(width=20)
weight_box.place(x=140, y=80)
bmi_box = tkinter.Entry(width=20)
bmi_box.place(x=140, y=230)

btn = tkinter.Button(tki, text='BMIを計算する。', command=btn_click)
btn.place(x=140, y=150)

tki.mainloop()