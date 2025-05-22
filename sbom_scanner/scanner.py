from sbom_scanner.sbom_parser import parse_sbom
from sbom_scanner.osv_api import query_osv

def scan_sbom(filepath, ecosystem="PyPI"):
    """

    :param filepath:
    :param ecosystem:
    :return:
    """
    results = []

    # packages will now contain list of tuples [(name, verion)]
    packages = parse_sbom(filepath)

    # loop through each package and query OSV
    for name, version in packages:
        # return vulns for that package
        vulns = query_osv(name, version)
        if not vulns:
            continue

        # filter for only the most recent vulnerability
        top_vuln = vulns[0]


        aliases = top_vuln.get("aliases", [top_vuln.get("id", "N/A")])
        summary = top_vuln.get("summary", "No description")
        severity = top_vuln.get("severity", [])

        # add this to results as a dict
        results.append({
            "package": name,
            "version": version,
            "cve_id": aliases,
            "summary": summary,
            "severity": severity
        })
    return results


if __name__ == "__main__":
    print(scan_sbom("/Users/jordancroft/Documents/Documents - Jordan.’s MacBook Air/GitHub/sbom-vuln-scan/sample_data/sample_sbom.json"))