import subprocess
import networkx as nx
import matplotlib.pyplot as plt
from io import StringIO
import os
import tkinter as tk
from tkinter import messagebox

keys = ['FAST University', 'Quaidabad', 'Malir Halt', 'Airport', 'Shell Pump', 'Drigh Road', 'Tipu Sultan Road',
        'IBEX', 'Clifton', 'Checkpost 2', 'Tank Chowk', 'Pehlwan GOth', 'Habib University', 'Millenium Mall', 'Dalmia',
        'Malir Cantt', 'Checkpost 6', 'Kamran Chowrangi', 'Munawwar Chowrangi', 'Darul Sehat', 'Johar Chowrangi',
        'Johar Mor', 'National Stadium', 'Bahadurabad', 'PECHS', 'Checkpost 5', 'Safoora Chowrangi', 'Mosamiyat',
        'Samama', 'NIPA', 'Hassan Square', 'Jail Chowrangi', 'Gulshan-e-Maymar', 'Gulshan Chowrangi', 'Nazimabad',
        'Lucky One Mall', 'Water Pumping', 'Sohrab Goth', 'Ancholi']


def run_dijkstra_and_get_output(source):
    cpp_folder = 'cpp'
    dijkstra_executable = 'showAll'

    # Determine the correct executable file extension based on the operating system
    if os.name == 'nt':  # Windows
        executable_path = f'..\\{cpp_folder}\\{dijkstra_executable}.exe'
    else:  # Unix-like
        executable_path = f'../{cpp_folder}/{dijkstra_executable}'

    # Use subprocess.run with the correct executable path
    result = subprocess.run([executable_path], input=str(source), capture_output=True, text=True)
    return result.stdout


def parse_output(output):
    lines = output.strip().split('\n')[1:]  # Skip the first line
    distances = []
    for line in lines:
        tokens = line.split()
        vertex, distance = int(tokens[0]), int(tokens[1])
        distances.append((vertex, distance))
    return distances


def visualize_graph(distances):
    G = nx.Graph()
    for i, (vertex, distance) in enumerate(distances):
        G.add_node(i, label=f"{keys[i]}\n{distance}")
    for i in range(len(distances) - 1):
        G.add_edge(i, i + 1)

    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'label')

    nx.draw(G, pos, with_labels=True, labels=labels, font_size=10, node_size=100)
    plt.title("Shortest Distances from Source (Dijkstra's Algorithm)")
    plt.show()


def showAll():
    # Create a new window for entering the source vertex
    source_window = tk.Toplevel()
    source_window.title("Enter Source Vertex")
    heading_labeltext ="0: FAST University\n1: Quaidabad\n2: Malir Halt\n3: Airport\n4: Shell Pump\n5: Drigh Road\n6: Tipu Sultan Road\n7: IBEX\n8: Clifton\n9: Checkpost 2\n10: Tank Chowk\n11: Pehlwan Goth\n12: Habib University\n13: Millennium Mall\n14: Dalmia\n15: Malir Cantt\n16: Checkpost 6\n17: Kamran Chowrangi\n18: Munawwar Chowrangi\n19: Darul Sehat\n20: Johar Chowrangi\n21: Johar Mor\n22: National Stadium\n23: Bahadurabad\n24: PECHS\n25: Checkpost 5\n26: Safoora Chowrangi\n27: Moasmiyat\n28: Samama\n29: NIPA\n30: Hassan Square\n31: Jail Chowrangi\n32: Gulshan-e-Maymar\n33: Gulshan Chowrangi\n34: Nazimabad\n35: Lucky One Mall\n36: Water Pumping\n37: Sohrab Goth\n38: Ancholi" 

    # Create and configure heading label
    heading_label = tk.Label(source_window, text="Enter Source Vertex", font=("Helvetica", 14, "bold"))
    heading_label.pack(pady=10)

    heading_label = tk.Label(source_window, text=heading_labeltext, font=("Helvetica", 10))
    heading_label.pack(pady=10)

    # Create and configure entry widget
    source_entry = tk.Entry(source_window, font=("Helvetica", 12))
    source_entry.pack(pady=10)

    # Create and configure submit button
    submit_button = tk.Button(source_window, text="Submit", command=lambda: submit_source(source_entry.get()),
                              bg="#4CAF50", fg="black", padx=10, pady=5)
    submit_button.pack(pady=10)


def submit_source(source):
    try:
        source = int(source)
        output = run_dijkstra_and_get_output(source)
        distances = parse_output(output)
        visualize_graph(distances)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for the source vertex.")


if __name__ == "__main__":
    showAll()
