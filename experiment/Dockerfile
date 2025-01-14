FROM --platform=amd64 python:3.11

WORKDIR /app

RUN pip install git+https://git@github.com/vstirbu/q8s-qpu-proxy.git@1-poc

COPY main.py .

# ENV QPU_PROXY_URL=http://qpu-proxy.qubernetes

# CMD ["python", "main.py"]
