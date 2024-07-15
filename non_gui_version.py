import os
import sys

def create_directory_structure(structure_text):
    lines = structure_text.strip().split('\n')
    base_dir = lines[0].strip('/')

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

if __name__ == "__main__":
    print("Введите структуру каталогов и файлов. Для завершения ввода введите пустую строку:")
    structure_text = ""
    while True:
        try:
            line = input()
            if line == "":
                break
            structure_text += line + "\n"
        except EOFError:
            break

    create_directory_structure(structure_text)
