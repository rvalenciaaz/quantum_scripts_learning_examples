import numpy as np
from qutip import *

# Setting up the initial state, two single photons coming in from different ports
ket_2photon = tensor(basis(2,1), basis(2,0), basis(2,0), basis(2,0)) + tensor(basis(2,0), basis(2,1), basis(2,0), basis(2,0))

# The 50:50 beam splitter transformation in the Fock basis is given by:
theta = np.pi/4
phi = 0
U = tensor(qip.operations.rz(phi), qip.operations.rz(phi)) * tensor(qip.operations.ry(theta), qip.operations.ry(-theta)) * tensor(qip.operations.rz(phi), qip.operations.rz(-phi))

# The transformation for two beam splitters can be represented as:
BS = tensor(U, qeye(2), qeye(2)) + tensor(qeye(2), U, qeye(2)) + tensor(qeye(2), qeye(2), U)

# Evolve the system
final_state = BS * ket_2photon

# Project onto the two-photon state where one photon comes out from each output
ket_coincidence = tensor(basis(2,1), basis(2,0), basis(2,1), basis(2,0))
projector_coincidence = ket_coincidence * ket_coincidence.dag()

# Calculate the probability of a coincidence count (one photon out of each output)
P_coincidence = (final_state.dag() * projector_coincidence * final_state).data[0,0]

print("The probability of a coincidence count is ", np.abs(P_coincidence))
