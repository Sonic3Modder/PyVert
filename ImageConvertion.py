import tkinter as tk
from tkinter import font, filedialog, messagebox, ttk
import cv2
import os
import rawpy
import numpy as np

# Function to handle file selection
def open_file():
    return filedialog.askopenfilename(
        title="Select Image", 
        filetypes=(("Image Files", "*.webp *.nef *.png *.jpg *.jpeg"),)
    )

# Function to handle directory selection
def save_file():
    return filedialog.askdirectory(title="Select Output Directory")

# Function to process the image and save it
def process_image():
    image_path = open_file()
    if not image_path:
        messagebox.showerror("Error", "No image selected!")
        return

    # Validate file format
    file_format = format_var.get().strip().lower()  
    if file_format not in ['tiff', 'png', 'jpeg', 'jpg']:
        messagebox.showerror("Error", "Unsupported file format! Use 'tiff', 'png', or 'jpeg'.")
        return

    output_directory = save_file()
    if not output_directory:
        messagebox.showerror("Error", "No output directory selected!")
        return

    output_path = os.path.join(output_directory, f'ConvertedImage.{file_format}')

    # Process image
    if image_path.lower().endswith('.nef'):
        with rawpy.imread(image_path) as raw:
            img = raw.postprocess()
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    else:
        img = cv2.imread(image_path)

    new_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    
    # Update the progress bar
    progress_bar['maximum'] = img.shape[0]
    progress_bar['value'] = 0
    progress_bar.pack(pady=10)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rgb = img[i][j]
            new_img[i][j] = rgb
        # Update progress bar after each row
        progress_bar['value'] = i + 1
        root.update_idletasks()  # Update the UI

    # Save the image
    if file_format == 'tiff':
        cv2.imwrite(output_path, new_img)
    elif file_format == 'png':
        cv2.imwrite(output_path, new_img)
    elif file_format in ['jpeg', 'jpg']:
        cv2.imwrite(output_path, new_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

    messagebox.showinfo("Success", f"Image saved at: {output_path}")
    progress_bar.pack_forget()  # Hide the progress bar after completion

# Main Application
def create_gui():
    global root
    root = tk.Tk()
    root.title("Image Converter")

    # Set modern color scheme
    root.configure(bg="#F5F5F5")

    # Use a modern Google-style sans-serif font
    custom_font = font.Font(family="Helvetica", size=14, weight="bold")
    label_font = font.Font(family="Helvetica", size=12)
    
    # Create the label
    label = tk.Label(root, text="Choose output file format:", font=label_font, bg="#F5F5F5", fg="#212121")
    label.pack(pady=10)

    global format_var
    format_var = tk.StringVar(value="png")
    
    # Dropdown menu for file format selection
    format_menu = tk.OptionMenu(root, format_var, "tiff", "png", "jpeg")
    format_menu.config(font=custom_font, bg="#FFFFFF", fg="#212121", activebackground="#E0E0E0")
    format_menu.pack(pady=10)

    # Custom button style
    button_style = {'bg': '#4285F4', 'fg': 'white', 'activebackground': '#0F9D58', 'font': custom_font}

    convert_button = tk.Button(root, text="Convert Image", **button_style, command=process_image)
    convert_button.pack(pady=20)

    global progress_bar
    progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate")
    
    root.mainloop()

# Run the application
if __name__ == '__main__':
    create_gui()
