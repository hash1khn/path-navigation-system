import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
from prims import primsShow
from showw import showAll
from specific import run_cpp, plot_graph, handle_submit, create_gui
import os



def show_graph():
    image_path = '../img/map.png'
    img = Image.open(image_path)
    img = img.resize((900, 600), Image.BICUBIC)  
    img = ImageTk.PhotoImage(img)
    
    image_window = tk.Toplevel()
    image_label = tk.Label(image_window, image=img)
    image_label.pack()

    image_label.image = img


def open_algorithm_window():
    algorithm_window = tk.Toplevel(root)
    algorithm_window.title("Select Algorithm")

    # Set window size
    algorithm_window_width = 300
    algorithm_window_height = 150

    # Calculate the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the x and y coordinates for the algorithm window
    x_coordinate = (screen_width / 2) - (algorithm_window_width / 2)
    y_coordinate = (screen_height / 2) - (algorithm_window_height / 2)

    # Set the algorithm window size and position
    algorithm_window.geometry(f"{algorithm_window_width}x{algorithm_window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

    # Create and configure heading label
    heading_label = tk.Label(algorithm_window, text="Select Algorithm", font=("Helvetica", 14,"bold"))
    heading_label.pack(pady=10)

    # Create and configure "Dijkstra Algorithm" button
    dijkstra_button = tk.Button(algorithm_window, text="Dijkstra Algorithm", command=dijkstra_algorithm,bg="#4CAF50", fg="black", padx=10, pady=5)
    dijkstra_button.pack(pady=10)

    # Create and configure "Prim's Algorithm" button
    prims_button = tk.Button(algorithm_window, text="Prim's Algorithm", command=prims_algorithm,bg="#4CAF50", fg="black", padx=10, pady=5)
    prims_button.pack(pady=10)

def dijkstra_algorithm():
    # Create a new window for Dijkstra Algorithm options
    dijkstra_options_window = tk.Toplevel(root)
    dijkstra_options_window.title("Dijkstra Algorithm Options")

    # Create and configure heading label
    heading_label = tk.Label(dijkstra_options_window, text="Dijkstra Algorithm Options", font=("Helvetica", 14, "bold"))
    heading_label.pack(pady=10)

    # Create and configure "Show All" button
    show_all_button = tk.Button(dijkstra_options_window, text="Show All", command=show_all_dijkstra, bg="#4CAF50", fg="black", padx=10, pady=5)
    show_all_button.pack(pady=10)

    # Create and configure "Show Specific" button
    show_specific_button = tk.Button(dijkstra_options_window, text="Show Specific", command=show_specific_dijkstra, bg="#4CAF50", fg="black", padx=10, pady=5)
    show_specific_button.pack(pady=10)

def show_all_dijkstra():
    # Handle the logic for showing all Dijkstra results
    showAll()

def show_specific_dijkstra():
    # Handle the logic for showing specific Dijkstra result
    create_gui()


def prims_algorithm():
    try:
        # Execute the compiled C++ program
        primsShow()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("KARACHI MAP")

# Set window size
window_width = 800
window_height = 500

# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates for the Tk root window
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)

# Set the window size and position
root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

# Load and resize background image (replace "download.jpeg" with your image file)
image = Image.open('../img/introimage.png')
image = image.resize((window_width, window_height), Image.BICUBIC)
background_image = ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create and configure a label
welcome_label = tk.Label(root, text="Map Navigation System", font=("Helvetica", 23, "bold"),bg="blue", fg="white", padx=10, pady=5,relief=tk.GROOVE)
welcome_label.pack(pady=20)

# Create and configure "Show Graph" button
show_graph_button = tk.Button(root, text="Show Map",font=("Helvetica", 16), command=show_graph,bg="#4CAF50", fg="black", padx=10, pady=5)
show_graph_button.pack(pady=10)

# Create and configure "Let's Go" button
lets_go_button = tk.Button(root, text="Let's Go",font=("Helvetica", 16,"bold","italic"), command=open_algorithm_window,bg="#4CAF50", padx=10, pady=5)
lets_go_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

