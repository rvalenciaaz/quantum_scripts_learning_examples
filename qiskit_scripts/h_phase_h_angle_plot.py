from qiskit import QuantumCircuit, Aer, transpile
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
from numpy import pi

# Function to create and simulate the circuit for a given alpha and number of shots
def simulate_circuit(alpha, shots=1024):
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

    # Simulate the circuit
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    result = simulator.run(compiled_circuit, shots=shots).result()

    # Get the measurement results
    counts = result.get_counts()
    return counts

max_index=16
# List to store the calculated probabilities
probabilities_0 = []
probabilities_1 = []
alphas = [i*pi/4 for i in range(max_index)]  # Creating a list of alpha values from 0 to 2*pi with step pi/4

# Number of shots (change this to any value you want)
num_shots = 2**16

print(num_shots)

for alpha in alphas:
    counts = simulate_circuit(alpha, shots=num_shots)
    probabilities_0.append(counts.get('0', 0)/num_shots)
    probabilities_1.append(counts.get('1', 0)/num_shots)

# Plot probabilities vs alpha
plt.figure()
plt.plot(alphas, probabilities_0, label='Probability of measuring |0⟩')
plt.plot(alphas, probabilities_1, label='Probability of measuring |1⟩')
plt.xlabel('Alpha (in multiples of π/4)')
plt.ylabel('Probability')
plt.title('Probabilities vs Alpha')
plt.xticks([i*pi/4 for i in range(max_index)], [f'{i}π/4' for i in range(max_index)])  # Setting x-ticks as multiples of π/4
plt.legend()
plt.grid(True)
plt.show()
