# 📄 Project 2: Image to PDF Converter

👨‍💻 **Created by:** Hashir Adnan  
🌐 **Website:** [www.techthf.xyz](https://www.techthf.xyz)  
🗓️ **Date:** May 13, 2025

---

## 🧠 Description

This Python script converts multiple image files (JPG, PNG, JPEG) into a single PDF file.  
It's a lightweight utility project to automate the task of combining images into a printable or shareable PDF.

---

## 📦 Features

- 📂 Scans a folder for image files  
- 🔄 Automatically sorts and loads images  
- 🖼️ Converts all images to RGB (PDF-safe)  
- 🧾 Merges them into one PDF document  
- 💾 Saves the output in the same folder  

---

## 🧰 Tools & Modules Used

| Module      | Purpose                      |
|-------------|------------------------------|
| `PIL`       | Image processing (Pillow)    |
| `os`        | File and folder handling     |

---

## 💡 How to Use

1. Place your images (`.jpg`, `.png`, `.jpeg`) in the target folder.  
2. Set the `folder_path` variable in the script to that folder.  
3. Run the script.  
4. The output PDF will be created as `output.pdf` in the same folder.

---

## 🧪 Example

**Input Files:**
```
image1.jpg  
image2.png  
```

**Output File:**
```
output.pdf
```

---

> ✅ Tip: For better results, name your images in the desired order (e.g., `1.jpg`, `2.png`, `3.jpeg`)
