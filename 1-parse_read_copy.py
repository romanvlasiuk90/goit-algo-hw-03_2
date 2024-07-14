import shutil
import argparse
from pathlib import Path

def parse_arguments():
    print("Використання: python 1-parse_read_copy.py <шлях до вихідної директорії> [<шлях до директорії призначення>]")
    print("Приклад: python 1-parse_read_copy.py /path/to/source /path/to/destination")
    print("Якщо шлях до директорії призначення не вказано, за замовчуванням буде використовуватися 'dist'")
    
    parser = argparse.ArgumentParser(description="Копіювання та сортування файлів за розширенням.")
    parser.add_argument("source", help="Шлях до вихідної директорії")
    parser.add_argument("destination", nargs='?', default="dist", help="Шлях до директорії призначення (за замовчуванням 'dist')")
    return parser.parse_args()

def copy_and_sort_files(src_dir, dst_dir):
    try:
        if not dst_dir.exists():
            dst_dir.mkdir(parents=True, exist_ok=True)
        
        for item in src_dir.iterdir():
            if item.is_dir():
                copy_and_sort_files(item, dst_dir)
            elif item.is_file():
                file_ext = item.suffix[1:] if item.suffix else 'no_extension'
                ext_dir = dst_dir / file_ext
                ext_dir.mkdir(exist_ok=True)
                shutil.copy2(item, ext_dir / item.name)
                print(f"Файл '{item}' скопійовано до '{ext_dir}'")
    except Exception as e:
        print(f"Помилка при обробці: {e}")

def main():
    args = parse_arguments()
    src_dir = Path(args.source)
    dst_dir = Path(args.destination)
    
    if not src_dir.exists():
        print(f"Вихідна директорія '{src_dir}' не існує")
        return
    
    copy_and_sort_files(src_dir, dst_dir)
    print("Копіювання та сортування файлів завершено.")

if __name__ == "__main__":
    main()