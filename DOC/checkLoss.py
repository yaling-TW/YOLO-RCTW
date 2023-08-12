import os

image_folder_path = "images/OzFish_train"
txt_folder_path = "labels/OzFish_train"

# Get the list of image files
image_files = os.listdir(image_folder_path)

# Get the list of text files
txt_files = os.listdir(txt_folder_path)

# Remove file extensions from image file names
image_files_without_ext = [os.path.splitext(file)[0] for file in image_files]

# Remove file extensions from text file names
txt_files_without_ext = [os.path.splitext(file)[0] for file in txt_files]

# Find missing image files
missing_image_files = [file + ".png" for file in txt_files_without_ext if file + ".png" not in image_files]

# Find missing text files
missing_txt_files = [file + ".txt" for file in image_files_without_ext if file + ".txt" not in txt_files]

# Print the missing files
print("Missing image files:", missing_image_files)
print("Missing text files:", missing_txt_files)
