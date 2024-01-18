from qiskit import QuantumCircuit, Aer, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

import matplotlib.pyplot as plt

# Initialize a quantum circuit with 1 qubit
circuit = QuantumCircuit(1)

# Apply a ZHZ gate sequence (Z gate followed by H gate followed by Z gate)
circuit.z(0)
circuit.h(0)
circuit.z(0)

# Add a barrier to separate the gate sequences
circuit.barrier()

# Apply an X gate
circuit.x(0)

# Measure the qubit
circuit.measure_all()

# Simulate the circuit
simulator = AerSimulator()
compiled_circuit = transpile(circuit, simulator)
result = simulator.run(compiled_circuit).result()

# Get the measurement results
counts = result.get_counts()

# Plot the measurement results
plot_histogram(counts)
plt.show()
