from fastapi.testclient import TestClient
from qiskit import QuantumCircuit
from qiskit.qasm2 import dumps

from app.main import app
from app.qiskit.backend import Q8SBackend

client = TestClient(app)


circuit = QuantumCircuit(2, name="test")
circuit.h(0)
circuit.cx(0, 1)
circuit.measure_all()


def test_run_circuit():

    response = client.post("/runs", json={"circuit": dumps(circuit)})
    assert response.status_code == 200
    assert response.json()["status"] == "COMPLETED"


def test_run_circuit_invalid():
    response = client.post("/runs", json={"circuit": "invalid qasm"})
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "\"<input>:1,0: 'invalid' is not defined in this scope\""
    assert response.json()["detail"][0]["type"] == "value_error"
    assert response.json()["detail"][0]["loc"] == ["body", "circuit"]


def test_run_circuit_from_backend():
    simulator = Q8SBackend(client=client)

    job = simulator.run(circuit)

    assert job != None

    result = job.result()

    assert result.get_counts() != None
