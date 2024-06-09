import tkinter as tk
from PIL import Image, ImageTk
import pyautogui
import threading
import time

def start_clicker():
    def clicker_thread():
        try:
            while clicker_running:
                x, y = pyautogui.position()
                pyautogui.click(x=x, y=y)
        except KeyboardInterrupt:
            print("Clicker stopped.")

    global clicker_running
    clicker_running = True
    threading.Thread(target=clicker_thread).start()

def stop_clicker():
    global clicker_running
    clicker_running = False

def on_key_press(event):
    stop_clicker()

root = tk.Tk()
root.title("Auto Clicker")
root.geometry("300x250")
root.resizable(False, False)

window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

image = Image.open("click.png")
resized_image = image.resize((70, 70), resample=Image.BOX)
photo_image = ImageTk.PhotoImage(resized_image)

image_label = tk.Label(root, image=photo_image)
image_label.pack(pady=10)

def delayed_start():
    time.sleep(3)
    start_clicker()

start_button = tk.Button(root, text="Start", command=delayed_start)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=stop_clicker)
stop_button.pack(pady=5)

root.bind("<Key>", on_key_press)  # Klavyeden herhangi bir tuşa basıldığında stop_clicker fonksiyonunu çağırır

root.mainloop()