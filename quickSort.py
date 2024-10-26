import tkinter as tk
import random
import time
import pygame  # for sound on macOS and cross-platform

# Initialize pygame for sound
pygame.mixer.init()

# Initialize the window
window = tk.Tk()
window.title("Quick Sort Visualization")
window.geometry("600x450")
canvas = tk.Canvas(window, width=600, height=350, bg="white")
canvas.pack()

# Load sound file
sound_file = "/Users/askebrask/Downloads/bib.mp3"  # Full path to your sound file
beep_sound = pygame.mixer.Sound(sound_file)

# Generate random data for the bars
array = [random.randint(10, 300) for _ in range(400)]  # Reduced length for better visualization

# Function to play a sound
def play_sound():
    beep_sound.play()

# Function to display messages on the canvas
def show_message(text):
    canvas.delete("message")
    canvas.create_text(300, 320, text=text, tag="message", font=("Helvetica", 12), fill="black")
    window.update_idletasks()

# Function to draw the array as vertical bars
def draw_array(array, color_array):
    canvas.delete("all")  # Clear the canvas except the message
    canvas_height = 300
    canvas_width = 600
    bar_width = canvas_width / len(array)
    for i, val in enumerate(array):
        x0 = i * bar_width
        y0 = canvas_height - val
        x1 = (i + 1) * bar_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
    window.update_idletasks()

# Quick Sort algorithm with visualization
def quick_sort_visualize(array, low, high):
    if low < high:
        show_message("Choosing pivot")
        pivot_index = partition(array, low, high)
        
        # Visualize pivot placement and play sound
        draw_array(array, ["yellow" if x == pivot_index else "blue" for x in range(len(array))])
        play_sound()
        time.sleep(0.3)
        
        quick_sort_visualize(array, low, pivot_index - 1)   # Sort left partition
        quick_sort_visualize(array, pivot_index + 1, high)  # Sort right partition

# Partition function for Quick Sort
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]  # Swap
            show_message(f"Swapping elements at {i} and {j}")
            draw_array(array, ["green" if x == i or x == j else "blue" for x in range(len(array))])
            play_sound()
            time.sleep(0.1)
    array[i + 1], array[high] = array[high], array[i + 1]  # Place pivot in the right position
    show_message("Pivot placed")
    return i + 1

# Button to start Quick Sort
def start_sort():
    quick_sort_visualize(array, 0, len(array) - 1)
    show_message("Array sorted!")
    draw_array(array, ["green" for _ in range(len(array))])  # Final sorted array

start_button = tk.Button(window, text="Start Quick Sort", command=start_sort)
start_button.pack()

# Run the GUI
window.mainloop()
