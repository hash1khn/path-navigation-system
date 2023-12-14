import subprocess
import networkx as nx
import matplotlib.pyplot as plt
from io import StringIO

keys=['FAST University','Quaidabad','Malir Halt','Airport','Shell Pump','Drigh Road','Tipu Sultan Road','IBEX','Clifton','Checkpost 2','Tank Chowk','Pehlwan GOth','Habib University','Millenium Mall','Dalmia','Malir Cantt','Checkpost 6','Kamran Chowrangi','Munawwar Chowrangi','Darul Sehat','Johar Chowrangi','Johar Mor','National Stadium','Bahadurabad','PECHS','Checkpost 5','Safoora Chowrangi','Moasmiyat','Samama','NIPA','Hassan Square','Jail Chowrangi','Gulshan-e-Maymar','Gulshan Chowrangi','Nazimabaf','Lucky One Mall','Water Pumping','Sohrab Goth','Ancholi']

def run_prim_and_get_output():
    result = subprocess.run(["../cpp/prim"], capture_output=True, text=True)
    return result.stdout

def parse_output(output):
    lines = output.strip().split('\n')[1:]  
    edges = []
    for line in lines:
        tokens = line.split()
        u, v, weight = int(tokens[0]), int(tokens[2]), int(tokens[3])
        edges.append((u, v, weight))
    return edges

def visualize_graph(edges):
    G = nx.Graph()
    G.add_weighted_edges_from(edges)

    # Create a mapping of node indices to keys
    node_labels = {i: keys[i] for i in range(len(keys))}

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    
    nx.draw(G, pos, with_labels=True, labels=node_labels, font_size=10, node_size=100)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Minimum Spanning Tree (Prim's Algorithm)")
    plt.show()

def visualize_full_graph(edges):
    G = nx.Graph()
    G.add_weighted_edges_from(edges)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    
    nx.draw(G, pos, with_labels=True,font_size=3, node_size=100)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)
    plt.title("Full Graph")
    plt.show()

def primsShow():
    output = run_prim_and_get_output()
    edges = parse_output(output)
    visualize_graph(edges)  # Visualize MST

if __name__ == "__main__":
    primsShow()