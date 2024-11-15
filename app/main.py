from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from qiskit.qasm2.exceptions import QASM2ParseError

from .run import run_circuit

app = FastAPI()


class Run(BaseModel):
    circuit: str


@app.post("/runs")
def execute(run: Run):
    try:
        result = run_circuit(run.circuit)
        return {"status": "COMPLETED", "result": result}
    except QASM2ParseError as e:
        raise HTTPException(
            status_code=422, detail=[{"type": "value_error", "loc": ["body", "circuit"], "msg": str(e)}]
        )
