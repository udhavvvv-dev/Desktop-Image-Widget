import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import json
import os

# File to save widget settings
CONFIG_FILE = "widget_config.json"

def save_config(widget_x, widget_y, img_path, minimized, width, height):
    config = {
        "position": {"x": widget_x, "y": widget_y},
        "image": img_path,
        "minimized": minimized,
        "size": {"width": width, "height": height}
    }
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Config file is empty or contains invalid JSON. Using default configuration.")
            return None
    return None


def choose_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        load_image(file_path)
        save_config(root.winfo_x(), root.winfo_y(), file_path, minimized=False, width=root.winfo_width(), height=root.winfo_height())

def load_image(path):
    global img, img_label, img_path
    img_path = path
    image = Image.open(path)
    image = image.resize((root.winfo_width(), root.winfo_height()), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    img_label.configure(image=img)
    img_label.image = img

def minimize_widget():
    root.withdraw()
    save_config(root.winfo_x(), root.winfo_y(), img_path, minimized=True, width=root.winfo_width(), height=root.winfo_height())

def maximize_widget():
    root.deiconify()

def close_widget():
    root.destroy()

def on_right_click(event):
    context_menu.post(event.x_root, event.y_root)

def resize_start(event):
    global start_width, start_height, start_x, start_y
    start_width = root.winfo_width()
    start_height = root.winfo_height()
    start_x = event.x_root
    start_y = event.y_root

def resize_drag(event):
    new_width = start_width + (event.x_root - start_x)
    new_height = start_height + (event.y_root - start_y)
    root.geometry(f"{new_width}x{new_height}")
    if img_path:
        load_image(img_path)
    save_config(root.winfo_x(), root.winfo_y(), img_path, minimized=False, width=new_width, height=new_height)

# Main application
root = tk.Tk()
root.title("Desktop Widget")
root.geometry("300x200")
root.overrideredirect(True)  # Removes window border

# Load previous configuration
config = load_config()
img_path = config["image"] if config and "image" in config else None
position = config["position"] if config and "position" in config else {"x": 100, "y": 100}
minimized = config["minimized"] if config and "minimized" in config else False
size = config["size"] if config and "size" in config else {"width": 300, "height": 200}

# Set initial position and size
root.geometry(f"{size['width']}x{size['height']}+{position['x']}+{position['y']}")
root.wm_attributes("-topmost", False)  # Will not stay on top of other windows

# Minimize on start if last state was minimized
if minimized:
    root.withdraw()

# Set up dragging functionality
def start_drag(event):
    root.x = event.x
    root.y = event.y

def stop_drag(event):
    save_config(root.winfo_x(), root.winfo_y(), img_path, minimized=False, width=root.winfo_width(), height=root.winfo_height())

def on_drag(event):
    x = root.winfo_pointerx() - root.x
    y = root.winfo_pointery() - root.y
    root.geometry(f"+{x}+{y}")

root.bind("<Button-1>", start_drag)
root.bind("<ButtonRelease-1>", stop_drag)
root.bind("<B1-Motion>", on_drag)

# Add image label
img_label = tk.Label(root)
img_label.pack(fill="both", expand=True)

# Load the last used image, if exists
if img_path:
    load_image(img_path)

# Add right-click context menu
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Change Image", command=choose_image)
context_menu.add_command(label="Exit Widget", command=close_widget)
root.bind("<Button-3>", on_right_click)

# Set up resize handle (bottom-right corner)
resize_handle = tk.Label(root, cursor="bottom_right_corner")
resize_handle.pack(side="bottom", anchor="se")
resize_handle.bind("<Button-1>", resize_start)
resize_handle.bind("<B1-Motion>", resize_drag)

root.mainloop()
