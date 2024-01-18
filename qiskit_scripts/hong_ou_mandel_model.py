from qiskit import QuantumCircuit, Aer, transpile
from qiskit.providers.aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create the quantum circuit
circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)

circuit.measure_all()

# Draw the circuit
circuit.draw('mpl')
plt.show()

# Simulate the circuit
simulator = AerSimulator()
compiled_circuit = transpile(circuit, simulator)
result = simulator.run(compiled_circuit).result()

# Get the measurement results
counts = result.get_counts()

# Plot the results
plot_histogram(counts)
plt.show()


