import os
import shutil
import argparse
import sys

def copy_files_recursively(src_dir, dest_dir):
    try:
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)

            if os.path.isdir(src_path):
                copy_files_recursively(src_path, dest_dir)
            else:
                _, ext = os.path.splitext(item)
                if ext == "":
                    ext = "no_ext"

                ext = ext.lstrip(".")
                ext_dir = os.path.join(dest_dir, ext)

                os.makedirs(ext_dir, exist_ok=True)
                dest_path = os.path.join(ext_dir, item)

                try:
                    shutil.copy2(src_path, dest_path)
                    print(f"Скопійовано: {src_path} -> {dest_path}")
                except Exception as e:
                    print(f"Помилка при копіюванні {src_path}: {e}")

    except Exception as e:
        print(f"Помилка доступу до {src_dir}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання і сортування файлів за розширенням")
    parser.add_argument("src", nargs="?", default=".")
    parser.add_argument("dest", nargs="?", default="dist")
    args = parser.parse_args()

    if not os.path.exists(args.src):
        print("Вихідна директорія не існує")
        sys.exit(1)

    os.makedirs(args.dest, exist_ok=True)
    copy_files_recursively(args.src, args.dest)


if __name__ == "__main__":
    main()
