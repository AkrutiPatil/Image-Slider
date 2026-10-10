from itertools import cycle
from PIL import Image,ImageTk
import time
import tkinter as tk


root=tk.Tk()
root.title("Image Slideshow Viewer")

#list of ImagePath
image_paths=[r"C:\Users\ASUS\OneDrive\Pictures\image_0.jpg",
             r"C:\Users\ASUS\OneDrive\Pictures\Screenshots\Screenshot 2025-11-05 182442.png",
             r"C:\Users\ASUS\OneDrive\Pictures\Screenshots\Screenshot 2025-11-05 182722.png",
             r"C:\Users\ASUS\OneDrive\Pictures\Screenshots\Screenshot 2025-11-05 182759.png"
            ]

#resize the images to 1080x1080
image_size=(1080,1080)
images=[Image.open(path).resize(image_size) for path in image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_images)
        label.upadte()
        time.sleep(3)

slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root, text ='Play SLideshow',command=start_slideshow)
play_button.pack()

root.mainloop()