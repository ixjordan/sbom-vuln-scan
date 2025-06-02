from sbom_scanner.sbom_parser import parse_sbom
from sbom_scanner.manifest_parser import parse_requirements_txt
from sbom_scanner.osv_api import query_osv
from cvss import CVSS3


def scan_file(filepath, ecosystem="PyPI"):
    """
    will scan the sbom and the query the OSV database, returning if any CVE are found for the packages
    :param filepath: filepath to sbom
    :param ecosystem:
    :return: list of results
    """
    results = []

    # packages will now contain list of tuples [(name, verion)]
    if filepath.endswith(".txt"):
        packages = parse_requirements_txt(filepath)
        print(packages)
    else:
        packages = parse_sbom(filepath)

    # loop through each package and query OSV
    for name, version in packages:
        # return vulns for that package
        vulns = query_osv(name, version)


        if not vulns:
            print(f"{name} ({version or "unknown"}) --> No known vulnerabilities found")
            continue

        print(f"{name} ({version or "unknown"}) --> {len(vulns)} vulnerabilities found.")

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
            "severity": parse_cvss_scores(severity)
        })
    print("\n──────── Scan Summary ────────")
    print(f"✅ Total packages checked: {len(packages)}")
    print(f"⚠ Vulnerable packages found: {len(results)}")
    print("───────────────────────────────")

    return results



def parse_cvss_scores(severity_list):
    """

    :param severity_list:
    :return:
    """
    if not severity_list:
        return "N/A"
    # list for output score
    output = []


    for s in severity_list:
        # gets the score from the severity list details
        vector = s.get("score", "")

        # if vector is version CVSS:3 then assign severity
        if "CVSS:3" in vector:
            try:
                cvss_obj = CVSS3(vector)
                score = cvss_obj.scores()[0]
                severity = cvss_obj.severities()[0].capitalize()
                # visual icon to display severity
                if score >= 9.0:
                    icon = "🔥"
                elif score >= 7.0:
                    icon = "🔴"
                elif score >= 4.0:
                    icon = "🟠"
                elif score > 0:
                    icon = "🟢"
                else:
                    icon = "⚪"
                # add to output list
                output.append(f"{score:.1f} ({severity} {icon})")
            except Exception as e:
                output.append("N/A")
        else:
            output.append("N/A")
    # return output list
    return ", ".join(output)



if __name__ == "__main__":
    print(scan_file("/Users/jordancroft/Documents/Documents - Jordan.’s MacBook Air/GitHub/sbom-vuln-scan/sample_data/requirements.txt"))