import os
import shutil
import argparse
import sys


def copy_and_sort_files(src_dir, dest_dir):
    
    try:
        # Перебираємо всі елементи у вихідній директорії
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            
            # Якщо елемент є директорією, рекурсивно обробляємо її
            if os.path.isdir(src_path):
                copy_and_sort_files(src_path, dest_dir)
            else:
                try:
                    # Отримуємо розширення файлу (без крапки)
                    _, ext = os.path.splitext(item)
                    ext = ext.lower()[1:] if ext else 'no_extension'
                    
                    # Створюємо шлях до піддиректорії за розширенням
                    ext_dir = os.path.join(dest_dir, ext)
                    os.makedirs(ext_dir, exist_ok=True)
                    
                    # Копіюємо файл
                    dest_path = os.path.join(ext_dir, item)
                    shutil.copy2(src_path, dest_path)
                    print(f"Скопійовано: {src_path} -> {dest_path}")
                
                except (PermissionError, OSError) as e:
                    print(f"Помилка при обробці файлу {src_path}: {e}", file=sys.stderr)
    
    except (PermissionError, OSError) as e:
        print(f"Помилка доступу до директорії {src_dir}: {e}", file=sys.stderr)


def main():
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description='Рекурсивне копіювання та сортування файлів за розширенням.')
    parser.add_argument('source_dir', help='Шлях до вихідної директорії')
    parser.add_argument('dest_dir', nargs='?', default='dist', help='Шлях до директорії призначення (за замовчуванням: dist)')
    
    args = parser.parse_args()
    
    # Перевірка чи існує вихідна директорія
    if not os.path.isdir(args.source_dir):
        print(f"Помилка: Вихідна директорія не існує: {args.source_dir}", file=sys.stderr)
        sys.exit(1)
    
    # Створення директорії призначення, якщо вона не існує
    os.makedirs(args.dest_dir, exist_ok=True)
    
    # Виклик функції для копіювання та сортування файлів
    copy_and_sort_files(args.source_dir, args.dest_dir)
    
    print(f"\nУсі файли успішно скопійовано та відсортовано у директорії: {args.dest_dir}")


if __name__ == '__main__':
    main()