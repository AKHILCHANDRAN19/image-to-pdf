import os
from PIL import Image

# Set the Download folder path
download_folder = "/storage/emulated/0/Download"
output_pdf_path = os.path.join(download_folder, "output_images.pdf")

# List to store image file paths
image_paths = []

# Supported image extensions
image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.webp')

# Get all images from the Download folder
for filename in os.listdir(download_folder):
    if filename.lower().endswith(image_extensions):
        image_paths.append(os.path.join(download_folder, filename))

# Ensure there are images to process
if not image_paths:
    print("No images found in the Download folder.")
else:
    # Open the first image and convert it to RGB
    image_list = [Image.open(image).convert("RGB") for image in image_paths]

    # Save all images as a PDF
    try:
        # Save as PDF
        image_list[0].save(output_pdf_path, save_all=True, append_images=image_list[1:])
        print(f"PDF created successfully: {output_pdf_path}")
    except Exception as e:
        print(f"Error creating PDF: {e}")
