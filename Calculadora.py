import tkinter

button_values = [
    ["AC", "+/-", "%", "/"],
    ["7", "8", "9", "*"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["/", "*", "-", "+", "=",]
top_symbols = ["AC", "+/-", "%"] 

row_count = len(button_values) #5
column_count = len(button_values[0]) #4

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_organge = "#FF9500"
color_white = "white"

#criando a janela principal
window = tkinter.Tk()
window.title("Calculadora")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 45), bg=color_black, 
                      fg=color_white, anchor="e", width=column_count)
label.grid(row=0, column=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                                 width=column_count-1, height=1,
                                 command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            button.config(bg=color_light_gray, fg=color_black)
        elif value in right_symbols:
            button.config(bg=color_organge, fg=color_white)
        else:
            button.config(bg=color_dark_gray, fg=color_white)
        button.grid(row=row+1, column=column)
        
frame.pack()

#função para lidar com o clique dos botões (Fazendo os calculos)
A = "0"
operator = None
B = None

def clear_all():
    global A, operator, B
    A = "0"
    operator = None
    B = None

def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)
       

def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator

    if value in right_symbols:
        if value == "=":
            if operator and A:
                B = label["text"]
                result = eval(A + operator + B)
                label["text"] = remove_zero_decimal(result)
                clear_all()
        elif value in ["/", "*", "-", "+"]:
            A = label["text"]
            operator = value
            label["text"] = "0"
    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)

    else: #digitos ou ponto decimal
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value == "√":
            result = float(label["text"]) ** 0.5
            label["text"] = remove_zero_decimal(result)
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value

#centralizar a janela (opcional)
window.update_idletasks()
x = (window.winfo_screenwidth() // 2) - (window.winfo_width() // 2)
y = (window.winfo_screenheight() // 2) - (window.winfo_height() // 2)
window.geometry(f"{window.winfo_width()}x{window.winfo_height()}+{x}+{y}")

window.mainloop()