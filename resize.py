import os
import argparse
import random
from PIL import Image

# Function to resize an image
def resize_image(file_path, output_path):
    with Image.open(file_path) as im:
        basename = os.path.basename(file_path)
        im.thumbnail((512, 512))
        im.save(f"{output_path}/{basename}")
        print(f"Resized image {basename}")

# Function to randomly select files from a folder
def select_random_files(folder_path, num_images):
    # Get all the files in the folder
    files = os.listdir(folder_path)
    # Select random files
    selected_files = random.sample(files, num_images)
    return selected_files


def read_folder(folder_path, output_path, num_images):
    # create output folder if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for filename in select_random_files(folder_path, num_images):
        # Check if the file is an image
        if filename.endswith(("jpg", "jpeg", "png", "gif")):
            file_path = os.path.join(folder_path, filename)
            # Resize the image
            resize_image(file_path, output_path)

def parse_args():
    parser = argparse.ArgumentParser(description="resize images")
    parser.add_argument(
        "--input",
        type=str,
        default="img/ffhq",
        help="input folder",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="img/ffhq/cropped",
        help="output folder",
    )
    parser.add_argument(
        "--num_images",
        type=int,
        default=256,
        help="number of images to generate",
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    read_folder(args.input, args.output, args.num_images)
