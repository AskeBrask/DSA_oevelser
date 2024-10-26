import tkinter as tk
import random
import time

# Global settings for the visualization
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
ARRAY_SIZE = 30
BAR_WIDTH = WINDOW_WIDTH // ARRAY_SIZE
DELAY = 0.2  # Delay in seconds between steps

# Initialize the Tkinter window
window = tk.Tk()
window.title("Heapsort Visualization")
canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="white")
canvas.pack()

# Generate random data for the bars
array = [random.randint(10, WINDOW_HEIGHT) for _ in range(ARRAY_SIZE)]

def draw_array(arr, color_array):
    """Draw the array with color highlights for affected elements."""
    canvas.delete("all")
    for i, val in enumerate(arr):
        x0 = i * BAR_WIDTH
        y0 = WINDOW_HEIGHT - val
        x1 = (i + 1) * BAR_WIDTH
        y1 = WINDOW_HEIGHT
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
    window.update_idletasks()

def heapify(arr, n, i):
    """Maintain the max heap property for the subtree rooted at index i."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    color_array = ["blue"] * len(arr)

    # Highlight the current node being heapified
    color_array[i] = "yellow"
    if left < n:
        color_array[left] = "red"
    if right < n:
        color_array[right] = "red"
    
    draw_array(arr, color_array)
    time.sleep(DELAY)

    # Check if the left child exists and is larger than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if the right child exists and is larger than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        draw_array(arr, ["green" if x == i or x == largest else "blue" for x in range(len(arr))])
        time.sleep(DELAY)
        heapify(arr, n, largest)

def heapsort(arr):
    """Perform Heapsort with visualization."""
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Swap the root with the last element
        arr[0], arr[i] = arr[i], arr[0]
        draw_array(arr, ["green" if x == i else "blue" for x in range(len(arr))])
        time.sleep(DELAY)

        # Heapify the reduced heap
        heapify(arr, i, 0)

    # Final sorted array in green
    draw_array(arr, ["green"] * len(arr))

# Start button
start_button = tk.Button(window, text="Start Heapsort", command=lambda: heapsort(array))
start_button.pack()

# Run the Tkinter event loop
window.mainloop()
