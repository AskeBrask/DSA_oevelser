import tkinter as tk
import pygame
import os
import time

# Initialize pygame for sound
pygame.mixer.init()
time.sleep(0.1)  # Small delay to ensure mixer is ready

# Sound file path
sound_file = "bib.mp3"
if not os.path.exists(sound_file):
    print("Sound file not found:", sound_file)

# Load sound once
beep_sound = pygame.mixer.Sound(sound_file)

# Tkinter window setup
window = tk.Tk()
window.title("Fibonacci Spiral Visualization with Sound")
canvas_width = 800
canvas_height = 800
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Visualization parameters
delay = 0.2  # Delay between drawing squares (in seconds)

# Memoization dictionary for Fibonacci
memo = {}

# Function to calculate Fibonacci numbers with memoization
def fibonacci(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

# Function to play sound
def play_sound():
    try:
        beep_sound.play()
    except pygame.error as e:
        print(f"Error playing sound: {e}")

# Function to draw the Fibonacci spiral
def draw_fibonacci_spiral(n):
    x, y = canvas_width // 2, canvas_height // 2  # Start at the center
    angle = 0  # Initial angle for rotation

    for i in range(n):
        # Calculate the side length of the square
        side = fibonacci(i) * 10  # Scale up Fibonacci numbers for better visibility

        # Define the corners of the square based on the current angle
        if angle == 0:       # Right
            x1, y1 = x, y
            x2, y2 = x + side, y + side
            x += side
        elif angle == 90:    # Down
            x1, y1 = x - side, y
            x2, y2 = x, y + side
            y += side
        elif angle == 180:   # Left
            x1, y1 = x - side, y - side
            x2, y2 = x, y
            x -= side
        elif angle == 270:   # Up
            x1, y1 = x, y - side
            x2, y2 = x + side, y
            y -= side

        # Draw the square
        canvas.create_re