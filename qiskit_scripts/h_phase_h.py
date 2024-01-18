from qiskit import QuantumCircuit, Aer, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Define the angle alpha
alpha = 0.5  # You can change this value to any other value

# Initialize a quantum circuit with 1 qubit
qc = QuantumCircuit(1)

# Initialize the qubit to the state |1>
qc.initialize([0, 1], 0)

# Apply the first Hadamard transformation
qc.h(0)

# Apply a phase change with angle alpha
qc.p(alpha, 0)

# Apply the second Hadamard transformation
qc.h(0)

# Measure the final state
qc.measure_all()

# Visualize the circuit
qc.draw('mpl')
plt.show()

# Simulate the circuit
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit).result()

# Get and visualize the measurement results
counts = result.get_counts()
plot_histogram(counts)
plt.show()
