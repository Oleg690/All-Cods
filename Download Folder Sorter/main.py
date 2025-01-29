import os
import shutil
from pathlib import Path

def transfer_photos(src_folder, dest_folder, valid_extensions=('.png', '.jpg', '.jpeg')):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for filename in os.listdir(src_folder):
        if filename.lower().endswith(valid_extensions):
            src_path = os.path.join(src_folder, filename)
            dest_path = os.path.join(dest_folder, filename)

            shutil.move(src_path, dest_path)
    print("Photos successfully transferred!")

if __name__ == "__main__":
    # Set your source (Downloads) and destination folders
    downloads_folder = str(Path.home() / "Downloads")
    selected_folder = r"C:\Users\crist\OneDrive\Imagini\Screenshot-from-Python-Lesson"

    # Transfer photos from Downloads folder to the selected folder
    transfer_photos(downloads_folder, selected_folder)
