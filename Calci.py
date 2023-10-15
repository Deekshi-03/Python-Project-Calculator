from tkinter import *

mw = Tk()
mw.title("Calculator")


def clear():
    Display_box.delete(0, END)


def Button_clk(num):
    cur_num = Display_box.get()
    clear()
    f_num = cur_num + num
    Display_box.insert(0, f_num)


first_num = 0

math = ""


def calc(math_type):
    global first_num, math
    math = math_type
    first_num = Display_box.get()
    clear()


def equal():
    global first_num
    second_num = Display_box.get()
    clear()
    if math == "add":
        result = int(first_num) + int(second_num)
    elif math == "sub":
        result = int(first_num) - int(second_num)
    elif math == "mul":
        result = int(first_num) * int(second_num)
    elif math == "div":
        result = int(first_num) / int(second_num)
    Display_box.insert(0, str(result))


# Creating widgets 
Display_box = Entry(mw, width=14, font=("Arial", 28), justify=RIGHT)

Button_0 = Button(mw, text="0", padx=36, pady=10, font=("Arial", 14), command=lambda: Button_clk("0"))
Button_1 = Button(mw, text="1", padx=36, pady=10, font=("Arial", 14), command=lambda: Button_clk("1"))
Button_2 = Button(mw, text="2", padx=36, pady=10, font=("Arial", 14), command=lambda: Button_clk("2"))
Button_3 = Button(mw, text="3", padx=36, pady=10, font=("Arial", 14), command=lambda: Button_clk("3"))
Button_4 = Button(mw, text="4", padx=36, pady=10, font=("Arial", 14), command=lambda: Button_clk("4"))
Button_5 = Button(mw, text="5", padx=36, pady=10, font=("Arial", 14), command=lambda: Button_clk("5"))
Button_6 = Button(mw, text="6", padx=36, pady=10, font=("Arial", 14), command=lambda: Button_clk("6"))
Button_7 = Button(mw, text="7", padx=36, pady=10, font=("Arial", 14), command=lambda: Button_clk("7"))
Button_8 = Button(mw, text="8", padx=36, pady=10, font=("Arial", 14), command=lambda: Button_clk("8"))
Button_9 = Button(mw, text="9", padx=36, pady=10, font=("Arial", 14), command=lambda: Button_clk("9"))

Button_clear = Button(mw, text="Clear", padx=72, pady=10, font=("Arial", 14), command=clear)
Button_div = Button(mw, text="/", padx=39, pady=10, font=("Arial", 14), command=lambda: calc("div"))
Button_mul = Button(mw, text="*", padx=38, pady=10, font=("Arial", 14), command=lambda: calc("mul"))
Button_add = Button(mw, text="+", padx=36, pady=10, font=("Arial", 14), command=lambda: calc("add"))
Button_sub = Button(mw, text="-", padx=39, pady=10, font=("Arial", 14), command=lambda: calc("sub"))
Button_equal = Button(mw, text="=", padx=38, pady=40, font=("Arial", 14), command=equal)

# Showing Widgets

Button_add.grid(row=6, column=1, padx=2, pady=2)
Button_sub.grid(row=6, column=0, padx=2, pady=2)

Button_div.grid(row=5, column=0, padx=2, pady=2)
Button_mul.grid(row=5, column=1, padx=2, pady=2)
Button_equal.grid(row=5, column=2, rowspan=2, padx=2, pady=2)

Button_0.grid(row=4, column=0, padx=2, pady=2)
Button_clear.grid(row=4, column=1, columnspan=2, padx=2, pady=2)

Button_1.grid(row=3, column=0, padx=2, pady=2)
Button_2.grid(row=3, column=1, padx=2, pady=2)
Button_3.grid(row=3, column=2, padx=2, pady=2)

Button_4.grid(row=2, column=0, padx=2, pady=2)
Button_5.grid(row=2, column=1, padx=2, pady=2)
Button_6.grid(row=2, column=2, padx=2, pady=2)

Button_7.grid(row=1, column=0, padx=2, pady=2)
Button_8.grid(row=1, column=1, padx=2, pady=2)
Button_9.grid(row=1, column=2, padx=2, pady=2)

Display_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

mw.mainloop()
