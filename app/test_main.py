from fastapi.testclient import TestClient
from qiskit import QuantumCircuit
from qiskit.qasm2 import dumps

from .main import app

client = TestClient(app)

def test_run_circuit():
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure_all()

    response = client.post("/runs", json={"circuit": dumps(circuit)})
    assert response.status_code == 200
    assert response.json()["status"] == "COMPLETED"