from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import numpy as np

# Define your 2x3 matrix
matrix = np.array([[1, 2, 3],
                   [3, 4, 5]])

# Flatten the matrix into a vector and normalize
vector = matrix.flatten()
norm = np.linalg.norm(vector)
normalized_vector = vector / norm

# Pad the normalized vector to the next power of 2
desired_length = 2**int(np.ceil(np.log2(len(normalized_vector))))
padded_vector = np.zeros(desired_length)
padded_vector[:len(normalized_vector)] = normalized_vector

# Re-normalize the padded vector to ensure its norm is 1
padded_vector /= np.linalg.norm(padded_vector)

# Determine the number of qubits needed
num_qubits = int(np.log2(desired_length))

# Create a quantum circuit with the necessary qubits
qc = QuantumCircuit(num_qubits, num_qubits)  # Added classical bits for measurement

# Initialize the quantum circuit with the padded, normalized vector
qc.initialize(padded_vector, [i for i in range(num_qubits)])

# Add measurements to all qubits
qc.measure(range(num_qubits), range(num_qubits))

# Draw the circuit with measurements
print(qc.draw())

# Simulate the quantum circuit to observe the outcome probabilities
simulator = Aer.get_backend('qasm_simulator')  # Using the QASM simulator for measurements
result = execute(qc, simulator, shots=1024).result()  # Execute the circuit
counts = result.get_counts(qc)  # Get the measurement results

# Plot the measurement outcomes
plot_histogram(counts)
plt.show()
