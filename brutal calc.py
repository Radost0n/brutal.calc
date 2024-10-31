import tkinter as tk

def check_stop():
    if any(entry.get().strip().lower() == "стп" for entry in (number1_entry, number2_entry, answer_entry)):
        window.destroy()

def add():
    check_stop()
    try:
        num1 = float(number1_entry.get())
        num2 = float(number2_entry.get())
        result = num1 + num2
        answer_entry.delete(0, tk.END)
        answer_entry.insert(0, str(result))
    except ValueError:
        answer_entry.delete(0, tk.END)
        answer_entry.insert(0, "Ошибка ввода")

def sub():
    check_stop()
    try:
        num1 = float(number1_entry.get())
        num2 = float(number2_entry.get())
        result = num1 - num2
        answer_entry.delete(0, tk.END)
        answer_entry.insert(0, str(result))
    except ValueError:
        answer_entry.delete(0, tk.END)
        answer_entry.insert(0, "Ошибка ввода")

def mul():
    check_stop()
    try:
        num1 = float(number1_entry.get())
        num2 = float(number2_entry.get())
        result = num1 * num2
        answer_entry.delete(0, tk.END)
        answer_entry.insert(0, str(result))
    except ValueError:
        answer_entry.delete(0, tk.END)
        answer_entry.insert(0, "Ошибка ввода")

def div():
    check_stop()
    try:
        num1 = float(number1_entry.get())
        num2 = float(number2_entry.get())
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Деление на ноль"
        answer_entry.delete(0, tk.END)
        answer_entry.insert(0, str(result))
    except ValueError:
        answer_entry.delete(0, tk.END)
        answer_entry.insert(0, "Ошибка ввода")

# Основное окно приложения
window = tk.Tk()
window.title('Brute Force Calculator')
window.geometry("500x500")
window.config(bg="black")
window.resizable(False, False)

# Настройки стиля
button_style = {"width": 5, "height": 2, "bg": "gray", "fg": "white", "font": ("Courier", 18, "bold"), "borderwidth": 5}
label_style = {"bg": "black", "fg": "white", "font": ("Courier", 12, "bold")}
entry_style = {"width": 25, "bg": "black", "fg": "white", "font": ("Courier", 14, "bold"), "borderwidth": 5}

# Кнопки операций
button_add = tk.Button(window, text="+", command=add, **button_style)
button_add.place(x=50, y=350)
button_sub = tk.Button(window, text="-", command=sub, **button_style)
button_sub.place(x=150, y=350)
button_mul = tk.Button(window, text="*", command=mul, **button_style)
button_mul.place(x=250, y=350)
button_div = tk.Button(window, text="/", command=div, **button_style)
button_div.place(x=350, y=350)

# Поля для ввода чисел и вывода ответа
number1_entry = tk.Entry(window, **entry_style)
number1_entry.place(x=50, y=100)
number2_entry = tk.Entry(window, **entry_style)
number2_entry.place(x=50, y=200)
answer_entry = tk.Entry(window, **entry_style)
answer_entry.place(x=50, y=450)

# Метки для ввода чисел и ответа
number1 = tk.Label(window, text="Первое число:", **label_style)
number1.place(x=50, y=70)
number2 = tk.Label(window, text="Второе число:", **label_style)
number2.place(x=50, y=170)
answer = tk.Label(window, text="Ответ:", **label_style)
answer.place(x=50, y=420)

# Запуск основного цикла приложения
window.mainloop()