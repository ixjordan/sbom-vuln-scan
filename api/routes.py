from fastapi import APIRouter
from api.schemas import ScanResult, ScanRequest
from sbom_scanner import url_fetcher
from sbom_scanner.scanner import scan_file
from enums.scan_enums import InputType

router = APIRouter()

# end point for user to scan
@router.post(path="/scan", response_model=ScanResult)
def scan_endpoint(scan_request: ScanRequest):
    results=[]

    if scan_request.file_path:
        # if user passes filepath(will be an sbom)
        if scan_request.file_path.endswith("requirements.txt"):
            results = scan_file(scan_request.file_path, InputType.REQUIREMENTS)
        elif scan_request.file_path.endswith(".json"):
            results = scan_file(scan_request.file_path, InputType.SBOM)

    #for user passed url
    elif scan_request.url:
        # stores temp file path
        if scan_request.url.endswith("requirements.txt"):
            temp_path = url_fetcher.download_file_to_temp(scan_request.url)
            results = scan_file(temp_path, InputType.REQUIREMENTS)
        elif scan_request.url.endswith(".json"):
            temp_path = url_fetcher.download_file_to_temp(scan_request.url)
            results = scan_file(temp_path, InputType.SBOM)

    return ScanResult(results=results)

