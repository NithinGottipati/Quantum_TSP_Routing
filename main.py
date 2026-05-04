
# Quantum Traffic Routing using TSP (QAOA)


# Step 1: Import Libraries
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


from qiskit.algorithms import QAOA
from qiskit_optimization.applications import Tsp
from qiskit_optimization.algorithms import MinimumEigenOptimizer

# Step 2: Create Graph (Cities + Distances)
def create_graph():
    graph = nx.Graph()

    # Example: 4 cities
    edges = [
        (0, 1, 10),
        (0, 2, 15),
        (0, 3, 20),
        (1, 2, 35),
        (1, 3, 25),
        (2, 3, 30),
    ]

    graph.add_weighted_edges_from(edges)
    return graph

# Step 3: Draw Graph
def draw_graph(graph):
    pos = nx.spring_layout(graph)
    labels = nx.get_edge_attributes(graph, 'weight')

    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=2000)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    plt.title("City Graph (Traffic Map)")
    plt.show()

# Step 4: Solve TSP using QAOA
def solve_tsp(graph):
    tsp = Tsp(graph)
    qp = tsp.to_quadratic_program()

    # QAOA setup
    from qiskit_aer import Aer
    from qiskit.utils import QuantumInstance

    backend = Aer.get_backend('aer_simulator')
    quantum_instance = QuantumInstance(backend)

    qaoa = QAOA(quantum_instance=quantum_instance, reps=1)

    optimizer = MinimumEigenOptimizer(qaoa)
    result = optimizer.solve(qp)

    return tsp, result

# Step 5: Display Results
def display_result(tsp, result):
    print("\nOptimal Route (Binary Representation):", result.x)
    print("Minimum Cost:", result.fval)

    # Step 1: Convert result to city order
    route = tsp.interpret(result.x)

    # Step 2: Function to rotate route to start from city 0
    def start_from_zero(route):
        while route[0] != 0:
            route = route[1:] + [route[0]]
        return route

    # Step 3: Apply rotation
    route = start_from_zero(route)

    # Step 4: Print final route
    print("City Order (start from 0):", route)
    
# Step 6: Main Function
def main():
    graph = create_graph()

    print("Graph Created Successfully")

    draw_graph(graph)

    tsp, result = solve_tsp(graph)

    display_result(tsp, result)

# Run Program
if __name__ == "__main__":
    main()