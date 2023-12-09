# File: graph_visualization.py

import tkinter as tk
import subprocess
import matplotlib.pyplot as plt
import networkx as nx

heading_labeltext ="0: FAST University\n1: Quaidabad\n2: Malir Halt\n3: Airport\n4: Shell Pump\n5: Drigh Road\n6: Tipu Sultan Road\n7: IBEX\n8: Clifton\n9: Checkpost 2\n10: Tank Chowk\n11: Pehlwan Goth\n12: Habib University\n13: Millennium Mall\n14: Dalmia\n15: Malir Cantt\n16: Checkpost 6\n17: Kamran Chowrangi\n18: Munawwar Chowrangi\n19: Darul Sehat\n20: Johar Chowrangi\n21: Johar Mor\n22: National Stadium\n23: Bahadurabad\n24: PECHS\n25: Checkpost 5\n26: Safoora Chowrangi\n27: Moasmiyat\n28: Samama\n29: NIPA\n30: Hassan Square\n31: Jail Chowrangi\n32: Gulshan-e-Maymar\n33: Gulshan Chowrangi\n34: Nazimabad\n35: Lucky One Mall\n36: Water Pumping\n37: Sohrab Goth\n38: Ancholi"

def calctime():
        try:
            with open('time.txt', 'r') as file:
                time = file.readline()
                print(time)
                    
        except FileNotFoundError:
                # Route file not found, wait for the C++ program to generate it
                print('error')

        return time

keys = ['FAST University', 'Quaidabad', 'Malir Halt', 'Airport', 'Shell Pump', 'Drigh Road', 'Tipu Sultan Road',
        'IBEX', 'Clifton', 'Checkpost 2', 'Tank Chowk', 'Pehlwan GOth', 'Habib University', 'Millenium Mall', 'Dalmia',
        'Malir Cantt', 'Checkpost 6', 'Kamran Chowrangi', 'Munawwar Chowrangi', 'Darul Sehat', 'Johar Chowrangi',
        'Johar Mor', 'National Stadium', 'Bahadurabad', 'PECHS', 'Checkpost 5', 'Safoora Chowrangi', 'Mosamiyat',
        'Samama', 'NIPA', 'Hassan Square', 'Jail Chowrangi', 'Gulshan-e-Maymar', 'Gulshan Chowrangi', 'Nazimabad',
        'Lucky One Mall', 'Water Pumping', 'Sohrab Goth', 'Ancholi']

def run_cpp(source, destination):
    with open('input.txt', 'w') as file:
        file.write(f"{source} {destination}")

    # Run the C++ program as a separate process
    subprocess.Popen(["./showSpecific"])

def plot_graph(time):
    try:
        with open('route.txt', 'r') as file:
            route = list(map(int, file.readline().split()))

        # Create a dictionary to map node numbers to corresponding keys
        node_mapping = {i: key for i, key in enumerate(keys)}

        G = nx.Graph()


        # Adding nodes with keys
        for i, node in enumerate(route):
            G.add_node(node_mapping[node])

        # Adding edges
        for i in range(len(route) - 1):
            G.add_edge(node_mapping[route[i]], node_mapping[route[i + 1]])

        pos = nx.spring_layout(G)  # Positions for all nodes

        # Draw nodes
        nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=500)
        
        # Draw edges
        nx.draw_networkx_edges(G, pos, edge_color='black')

        # Draw labels
        nx.draw_networkx_labels(G, pos, font_color='black')

        plt.title('Route Graph')
        plt.axis('off')

        plt.text(0.95, 0.05, f'Time Taken: {time}minutes', transform=plt.gcf().transFigure,
                 fontsize=10, color='black', ha='right', va='bottom')
     
        plt.show()


    except FileNotFoundError:
        # Route file not found, wait for the C++ program to generate it
        root = tk.Tk()
        root.after(100, plot_graph)


        
def handle_submit(entry_source, entry_dest, time):
    run_cpp(int(entry_source.get()), int(entry_dest.get()))
    plot_graph(time)

def create_gui():
    # Tkinter window setup
    root = tk.Tk()
    root.title("Source and Destination")

     

    frame = tk.Frame(root)
    frame.pack()

    keys_source = tk.Label(frame, text=heading_labeltext, font=("Helvetica", 8))
    keys_source.grid()
    label_source = tk.Label(frame, text="Enter Source Node:")
    label_source.grid(row=1, column=0)
    entry_source = tk.Entry(frame)
    entry_source.grid(row=2, column=0)

    label_dest = tk.Label(frame, text="Enter Destination Node:")
    label_dest.grid(row=4, column=0)
    entry_dest = tk.Entry(frame)
    entry_dest.grid(row=5, column=0)

    time = calctime()

    submit_button = tk.Button(frame, text="Submit", command=lambda: handle_submit(entry_source, entry_dest, time))
    submit_button.grid(row=13, columnspan=1)

    root.mainloop()

    

if __name__ == "__main__":
    create_gui()