import json
import os
import pandas as pd

def convert_labelme_to_yolo(labelme_directory, output_directory, class_map):
    data_rows = []

    for filename in os.listdir(labelme_directory):
        if filename.endswith('.json'):
            labelme_path = os.path.join(labelme_directory, filename)
            with open(labelme_path, 'r') as f:
                data = json.load(f)

            image_path = data['imagePath']
            image_width = data['imageWidth']
            image_height = data['imageHeight']

            for shape in data['shapes']:
                label = shape['label']
                points = shape['points']
                x_min = min(point[0] for point in points)
                y_min = min(point[1] for point in points)
                x_max = max(point[0] for point in points)
                y_max = max(point[1] for point in points)

                class_id = class_map.get(label)
                if class_id is not None:
                    x_center = (x_min + x_max) / (2 * image_width)
                    y_center = (y_min + y_max) / (2 * image_height)
                    width = (x_max - x_min) / image_width
                    height = (y_max - y_min) / image_height
                    data_rows.append([filename, class_id, x_center, y_center, width, height])

    column_names = ['filename', 'class_id', 'x_center', 'y_center', 'width', 'height']
    df = pd.DataFrame(data_rows, columns=column_names)

    grouped = df.groupby('filename')
    for filename, group in grouped:
        base_filename = os.path.splitext(filename)[0]
        output_file = os.path.join(output_directory, base_filename + '.txt')
        group[['class_id', 'x_center', 'y_center', 'width', 'height']].to_csv(output_file, sep=' ', header=False, index=False)

        print(f'Converted {filename} to YOLO format: {output_file}')


# Provide the directory path containing the Labelme JSON files
labelme_directory = 'labelme'

# Provide the output directory for YOLO format files
output_directory = 'labelme'

# Define the mapping of class labels to class IDs (customize as per your labels)
class_map = {
    'fish': 0,
    'angelfish': 1,
    'butterflyfish': 2,
    'grouper': 3,
    'grunt': 4,
    'humpheadparrotfish': 5,
    'humpheadwrasse': 6,
    'moorishidol': 7,
    'morayeel': 8,
    'parrotfish': 9,
    'snapper': 10,
    # Add more classes as needed
}

convert_labelme_to_yolo(labelme_directory, output_directory, class_map)
