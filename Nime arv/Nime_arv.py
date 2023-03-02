import tkinter as tk

# функция для расчета числа имени
def calculate_num(name, lang):
    # таблица соответствия буквам и числам на русском языке
    rus_table = {
        'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ё': 7, 'ж': 8, 'з': 9,
        'и': 1, 'й': 2, 'к': 3, 'л': 4, 'м': 5, 'н': 6, 'о': 7, 'п': 8, 'р': 9,
        'с': 1, 'т': 2, 'у': 3, 'ф': 4, 'х': 5, 'ц': 6, 'ч': 7, 'ш': 8, 'щ': 9,
        'ъ': 0, 'ы': 1, 'ь': 2, 'э': 3, 'ю': 4, 'я': 5
    }
    
    # таблица соответствия буквам и числам на английском языке
    eng_table = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
        'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'o': 6, 'p': 7, 'q': 8, 'r': 9,
        's': 1, 't': 2, 'u': 3, 'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8
    }
    
    # выбор таблицы в зависимости от языка
    if lang == 'ru':
        table = rus_table
    elif lang == 'en':
        table = eng_table
    else:
        return "Unsupported language"
    
    # расчет числа имени
    num = sum([table.get(letter.lower(), 0) for letter in name])
    while num > 9:
        num = sum(int(digit) for digit in str(num))
        
    return num

# функция для обработки события нажатия на кнопку
def on_submit():
    name = name_entry.get()
    lang = lang_var.get()
    num = calculate_num(name, lang)
    result_label.config(text="Число имени: {}".format(num))

# создание графического интерфейса
root = tk.Tk()
root.title("Расчет числа имени")

# добавление виджетов на форму
name_label = tk.Label(root, text="Введите имя:")
name_entry = tk.Entry(root)
lang_label = tk.Label(root, text="Выберите язык:")
lang_var = tk.StringVar(root, "ru")
lang_menu = tk.OptionMenu(root, lang_var, "ru", "en")
submit_button = tk.Button(root, text="Рассчитать", command=on_submit)
result_label = tk.Label(root, text="")

#расположение виджетов на форме
name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
name_entry.grid(row=0, column=1, padx=5, pady=5)
lang_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
lang_menu.grid(row=1, column=1, padx=5, pady=5)
submit_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

#запуск цикла обработки событий
root.mainloop()