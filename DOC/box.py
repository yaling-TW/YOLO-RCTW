import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Load the image
image_path = "A000007_L-avi-74577.jpg"
image = plt.imread(image_path)

# Create a figure and axes
fig, ax = plt.subplots()

# Display the image
ax.imshow(image)

# Read the YOLO format annotations
annotations = []
with open("A000007_L-avi-74577.txt", "r") as file:
    for line in file:
        annotations.append(line.strip().split())

# Define the class labels
class_labels = ["fish"]

# Draw bounding boxes on the image
for annotation in annotations:
    class_id = int(annotation[0])
    center_x, center_y, width, height = map(float, annotation[1:5])

    # Calculate the top-left coordinates of the bounding box
    left = (center_x - width / 2) * image.shape[1]
    top = (center_y - height / 2) * image.shape[0]

    # Calculate the width and height of the bounding box
    bbox_width = width * image.shape[1]
    bbox_height = height * image.shape[0]

    # Create a rectangle patch
    rect = patches.Rectangle((left, top), bbox_width, bbox_height, linewidth=1, edgecolor='r', facecolor='none')

    # Add the rectangle patch to the axes
    ax.add_patch(rect)

    # Add the class label text near the bounding box
    label = f"{class_labels[class_id]}"
    ax.text(left, top, label, color='r')

# Show the image with bounding boxes
plt.show()
