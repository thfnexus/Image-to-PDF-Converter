"""
📄 Project 2: Image to PDF Converter
👨‍💻 Created by: Hashir Adnan
🌐 Website: www.techthf.xyz
🗓️ Date: [Insert today's date]

🧠 Description:
This Python script converts multiple image files (JPG, PNG, JPEG) into a single PDF file.
It's a lightweight utility project to automate the task of combining images into a printable or shareable PDF.

📦 Features:
- Scans a folder for image files
- Automatically sorts and loads images
- Converts all images to RGB (PDF-safe)
- Merges them into one PDF document
- Saves the output in the same folder

🧰 Tools & Modules Used:
- PIL (Pillow): for image processing
- os: for file handling

💡 How to Use:
1. Place your images (.jpg/.png) in the target folder.
2. Set the `folder_path` variable in the script to that folder.
3. Run the script.
4. The output PDF will be created as `output.pdf` in the same folder.

✅ Example:
Input Files: image1.jpg, image2.png  
Output File: output.pdf

"""

from PIL import Image
import os

# ✅ Set your image folder path
folder_path = r"c:\Users\ads\Desktop\py\pro 2"  # Change if needed
output_pdf = os.path.join(folder_path, "output.pdf")

# ✅ Collect all image files
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
image_files.sort()  # Optional: sort alphabetically

# ✅ Open and convert each image
images = []
for file in image_files:
    image_path = os.path.join(folder_path, file)
    img = Image.open(image_path).convert('RGB')  # Convert to RGB for PDF
    images.append(img)

# ✅ Save all images as one PDF
if images:
    first_img = images[0]
    rest_imgs = images[1:]
    first_img.save(output_pdf, save_all=True, append_images=rest_imgs)
    print(f"✅ PDF created successfully at: {output_pdf}")
else:
    print("❌ No image files found.")
