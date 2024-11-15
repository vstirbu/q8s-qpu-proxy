from abc import ABC
from httpx import Client
from qiskit import QuantumCircuit
from qiskit.providers import BackendV2, Options
from qiskit.qasm2 import dumps

from app.qiskit.job import Q8sJob


class Q8SBackend(BackendV2, ABC):
    _client = None

    def __init__(self, client: Client = None, **kwargs):
        super().__init__(**kwargs)

        if client:
            self._client = client
        else:
            self._client = Client()

    @classmethod
    def _default_options(self) -> Options:
        return Options(shots=1024)

    @property
    def max_circuits(self):
        return 1

    @property
    def target(self):
        return "q8s"

    def run(self, run_input: QuantumCircuit, **kwargs):
        result = self._client.post("http://localhost:8000/runs", json={"circuit": dumps(run_input)})

        return Q8sJob(result=result.json(), backend=self, job_id=1)
