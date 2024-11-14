from fastapi import FastAPI
from pydantic import BaseModel

from .run import run_circuit

app = FastAPI()

class Run(BaseModel):
    circuit: str

@app.post("/runs")
def execute(run: Run):
    result = run_circuit(run.circuit)
    return { "status": "COMPLETED", "result": result }
