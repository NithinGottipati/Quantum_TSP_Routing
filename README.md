# Quantum_TSP_Routing
Quantum Traffic Routing using QAOA (TSP)

This project demonstrates how quantum computing can be used to solve a traffic routing problem using the Travelling Salesman Problem (TSP).

---

## 🧠 Project Overview

The goal of this project is to find the shortest route between multiple cities such that each city is visited exactly once and the total travel cost is minimized.

This is achieved using:
- Travelling Salesman Problem (TSP)
- QAOA (Quantum Approximate Optimization Algorithm)
- Qiskit framework

---

## ⚙️ Technologies Used

- Python
- Qiskit
- Qiskit Optimization
- Qiskit Aer
- NetworkX
- Matplotlib

---

## 📌 Features

- Models cities as a graph with distances
- Converts routing problem into an optimization problem
- Uses QAOA to find optimal route
- Visualizes the city network
- Outputs:
  - Optimal route
  - Minimum cost
  - City order (starting from city 0)
