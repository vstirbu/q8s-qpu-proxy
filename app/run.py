import os
from qiskit import transpile
from qiskit.qasm2 import loads
from qiskit.result import Result
from iqm.qiskit_iqm.iqm_provider import IQMProvider, IQMFakeAdonis


def run_circuit(qasm: str) -> Result:
    circuit = loads(qasm)

    if os.getenv("IQM_TOKENS_FILE") is None:
        backend = IQMFakeAdonis()
    else:
        provider = IQMProvider(os.getenv("IQM_CORTEX_URL"))
        backend = provider.get_backend()

    new_circuit = transpile(circuit, backend)
    return backend.run(new_circuit, shots=1000).result()
