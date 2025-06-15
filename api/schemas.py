from pydantic import BaseModel, root_validator, model_validator
from typing import Optional

class ScanRequest(BaseModel):
    file_path: Optional[str] = None
    url: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def check_at_least_one(cls, values):
        # assing class instance vars to these vars
        file_path = values.get("file_path")
        url = values.get("url")

        # if neither privided raise exception
        if not file_path and not url:
            raise ValueError("You must provide either file or url.")
        # if both provided raise exception
        if file_path and url:
            raise ValueError("Only one of the paths should be provided")

        return values

class Vulnerability(BaseModel):
    package: str
    version: Optional[str]
    cve_id: list[str]
    summary: str
    severity: str

class ScanResult(BaseModel):
    results: list[Vulnerability]