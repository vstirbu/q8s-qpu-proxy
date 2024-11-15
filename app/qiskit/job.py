from qiskit.providers import JobStatus, JobV1
from qiskit.providers.backend import Backend
from qiskit.result import Counts, Result


class Q8sJob(JobV1):
    _result: Result = None

    def __init__(self, result: dict, backend: Backend | None, job_id: str, **kwargs) -> None:
        super().__init__(backend, job_id, **kwargs)

        self._result = Result.from_dict(result["result"])

    def result(self) -> Result:
        return self._result

    def status(self) -> JobStatus:
        return JobStatus.DONE

    def submit(self):
        raise NotImplementedError("Q8sJob.submit() is not implemented")
