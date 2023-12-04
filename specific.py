# File: graph_visualization.py

import tkinter as tk
import subprocess
import matplotlib.pyplot as plt
import networkx as nx

def run_cpp(source, destination):
    with open('input.txt', 'w') as file:
        file.write(f"{source} {destination}")

    # Run the C++ program as a separate process
    subprocess.Popen(["./showSpecific"])

def plot_graph():
    try:
        with open('route.txt', 'r') as file:
            route = list(map(int, file.readline().split()))

        route.reverse()  # Reverse the order of nodes

        G = nx.Graph()

        # Adding nodes
        for i, node in enumerate(route):
            G.add_node(node)

        # Adding edges
        for i in range(len(route) - 1):
            G.add_edge(route[i], route[i + 1])

        pos = nx.spring_layout(G)  # Positions for all nodes

        # Draw nodes
        nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=500)
        
        # Draw edges
        nx.draw_networkx_edges(G, pos, edge_color='black')

        # Draw labels
        nx.draw_networkx_labels(G, pos, font_color='black')

        plt.title('Route Graph')
        plt.axis('off')
        plt.show()

    except FileNotFoundError:
        # Route file not found, wait for the C++ program to generate it
        root.after(100, plot_graph)  # Check again after 100ms

def handle_submit(entry_source, entry_dest):
    run_cpp(int(entry_source.get()), int(entry_dest.get()))
    plot_graph()

def create_gui():
    # Tkinter window setup
    root = tk.Tk()
    root.title("Source and Destination")

    frame = tk.Frame(root)
    frame.pack()

    label_source = tk.Label(frame, text="Enter Source Node:")
    label_source.grid(row=0, column=0)
    entry_source = tk.Entry(frame)
    entry_source.grid(row=0, column=1)

    label_dest = tk.Label(frame, text="Enter Destination Node:")
    label_dest.grid(row=1, column=0)
    entry_dest = tk.Entry(frame)
    entry_dest.grid(row=1, column=1)

    submit_button = tk.Button(frame, text="Submit", command=lambda: handle_submit(entry_source, entry_dest))
    submit_button.grid(row=2, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
