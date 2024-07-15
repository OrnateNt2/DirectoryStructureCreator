import os
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
from tkinter import font

def create_directory_structure(base_path, structure_text):
    lines = structure_text.strip().split('\n')
    base_dir = os.path.join(base_path, lines[0].strip('/'))

    if not os.path.exists(base_dir):
        os.makedirs(base_dir, exist_ok=True)
    
    current_depth = -1
    path_stack = [base_dir]

    for line in lines[1:]:
        stripped_line = line.strip()
        if not stripped_line or stripped_line == '│':
            continue

        depth = (len(line) - len(line.lstrip(' │├└'))) // 4
        
        name = stripped_line.split(' ')[-1]

        if depth > current_depth:
            path_stack.append(os.path.join(path_stack[-1], name.strip('/')))
        elif depth == current_depth:
            path_stack[-1] = os.path.join(os.path.dirname(path_stack[-1]), name.strip('/'))
        else:
            for _ in range(current_depth - depth):
                path_stack.pop()
            path_stack[-1] = os.path.join(os.path.dirname(path_stack[-1]), name.strip('/'))

        current_depth = depth

        current_path = path_stack[-1]

        if name.endswith('/'):
            if not os.path.exists(current_path):
                os.makedirs(current_path)
        else:
            with open(current_path, 'w') as f:
                pass

def create_structure():
    directory = filedialog.askdirectory()
    if not directory:
        return

    structure_text = text_area.get("1.0", tk.END)
    try:
        create_directory_structure(directory, structure_text)
        messagebox.showinfo("Success", "Directory and file structure created successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Создаем основное окно
root = tk.Tk()
root.title("Directory and File Structure Creator")
root.geometry('700x600')
root.configure(bg='#f5f5f5')
root.resizable(False, False)  # Запрещаем изменять размер окна

# Устанавливаем шрифты
header_font = font.Font(family="Helvetica", size=18, weight="bold")
button_font = font.Font(family="Helvetica", size=12, weight="bold")
text_font = font.Font(family="Courier", size=10)

# Заголовок
header_label = tk.Label(root, text="Directory and File Structure Creator", font=header_font, bg='#f5f5f5')
header_label.pack(pady=20)

# Создаем виджет для ввода структуры
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=25, font=text_font)
text_area.pack(padx=20, pady=10)

# Создаем кнопку для создания структуры
create_button = tk.Button(root, text="Create Structure", command=create_structure, font=button_font, bg='#4CAF50', fg='white', padx=10, pady=5, relief=tk.FLAT)
create_button.pack(pady=20)

# Запускаем главный цикл обработки событий
root.mainloop()
