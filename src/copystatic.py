import os
import shutil


def copy_files_recursive(source_dir_path, dest_dir_path):
    # Remove destination if it exists
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    # Iterate through all items in source
    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            # Copy file
            shutil.copy(from_path, dest_path)
        else:
            # Recursively copy directory
            copy_files_recursive(from_path, dest_path)
