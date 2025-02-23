import tkinter as tk
from tkinter import messagebox
import pyautogui
import cv2
import numpy as np
import threading
import time

# Global variables
recording = False
coords = []  # To store the selected region
out = None  # Video writer object

def select_area(event):
    """Stores the coordinates of the selected area."""
    global coords
    if len(coords) < 2:
        coords.append((event.x_root, event.y_root))
    if len(coords) == 2:
        messagebox.showinfo("Selection", f"Selected Area: {coords}")

def start_recording():
    """Starts the screen recording."""
    global recording, out
    if len(coords) < 2:
        messagebox.showwarning("Warning", "Please select a region first.")
        return
    recording = True
    x1, y1 = coords[0]
    x2, y2 = coords[1]
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    
    # Define codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('screen_record.avi', fourcc, 10.0, (width, height))
    
    def record():
        """Captures frames and saves to the video file."""
        while recording:
            img = pyautogui.screenshot(region=(x1, y1, width, height))
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            out.write(frame)
            time.sleep(0.1)  # To control the frame rate
    
    threading.Thread(target=record, daemon=True).start()
    messagebox.showinfo("Recording", "Recording started. Click Stop to stop.")

def stop_recording():
    """Stops the recording and saves the video."""
    global recording, out
    recording = False
    if out:
        out.release()
    messagebox.showinfo("Recording", "Recording saved as 'screen_record.avi'")

def create_gui():
    """Creates the GUI using Tkinter."""
    root = tk.Tk()
    root.title("Screen Recorder")
    root.geometry("300x200")
    
    label = tk.Label(root, text="Click twice to select recording area")
    label.pack()
    
    canvas = tk.Canvas(root, width=200, height=100, bg="gray")
    canvas.pack()
    canvas.bind("<Button-1>", select_area)
    
    start_button = tk.Button(root, text="Start Recording", command=start_recording)
    start_button.pack()
    
    stop_button = tk.Button(root, text="Stop Recording", command=stop_recording)
    stop_button.pack()
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()
