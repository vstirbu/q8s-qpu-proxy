import os
from qiskit import QuantumCircuit
from app.qiskit.backend import Q8SBackend

print("loaded backend")

PROXY_URL = os.getenv("QPU_PROXY_URL")

if not PROXY_URL:
    raise ValueError("QPU_PROXY_URL is not set")

print("got proxy url", PROXY_URL)

simulator = Q8SBackend(proxy_url=PROXY_URL)

print("created simulator")

circuit = QuantumCircuit(2, name="test")
circuit.h(0)
circuit.cx(0, 1)
circuit.measure_all()

job = simulator.run(circuit)

print("ran circuit")
