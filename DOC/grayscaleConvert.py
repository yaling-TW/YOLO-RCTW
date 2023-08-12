from PIL import Image
import os

def convert_to_grayscale(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    file_list = os.listdir(input_folder)

    for filename in file_list:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Open the image using Pillow
        image = Image.open(input_path)

        # Convert the image to grayscale
        grayscale_image = image.convert("L")

        # Save the grayscale image
        grayscale_image.save(output_path)

if __name__ == "__main__":
    input_folder = "images/TWFDB"
    output_folder = "images/TWFDB_grayscale"

    convert_to_grayscale(input_folder, output_folder)
