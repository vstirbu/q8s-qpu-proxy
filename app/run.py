from qiskit import transpile
from qiskit.qasm2 import loads
from qiskit.result import Result
from iqm.qiskit_iqm.iqm_provider import IQMProvider, IQMFakeAdonis


def run_circuit(qasm: str, server_url: str = "https://demo.qc.iqm.fi/cocos") -> Result:
    circuit = loads(qasm)

    backend = IQMFakeAdonis()
    new_circuit = transpile(circuit, backend)
    return backend.run(new_circuit, shots=1000).result()
