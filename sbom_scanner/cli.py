import argparse
import os
from sbom_scanner import scanner
from rich.console import Console
from rich.table import Table

from sbom_scanner.url_fetcher import download_file_to_temp


def format_results(filepath):
    results = scanner.scan_file(filepath)
    console = Console()

    if not results:
        console.print("[green]✅ No known vulnerabilities found in the SBOM.[/green]")
        return

    table = Table(title="🔍 CVE Scan Results from SBOM")

    table.add_column("Package", style="cyan", no_wrap=True)
    table.add_column("Version", style="magenta")
    table.add_column("CVE(s)", style="red")
    table.add_column("Summary", style="white")
    table.add_column("Severity", style="yellow")

    for vuln in results:
        aliases = " / ".join(vuln["cve_id"]) if vuln["cve_id"] else "N/A"
        summary = vuln["summary"][:100] + "..." if len(vuln["summary"]) > 100 else vuln["summary"]

        if vuln["severity"]:
            sev = vuln["severity"]
        else:
            sev = "N/A"

        table.add_row(
            vuln["package"],
            vuln["version"],
            aliases,
            summary,
            sev
        )

    console.print(table)

def main():
    parser = argparse.ArgumentParser(
        description = "Scan a CycloneDX SBOM file for known vulnerabilites using OSV.dev"
    )
    # user must enter one option
    group = parser.add_mutually_exclusive_group(required=True)

    # file format
    group.add_argument(
        "--file",
        "-f",
        help = "Path to the CylconeDX SBOM JSON file"
    )
    # url format
    group.add_argument(
        "--url",
        help= "URL to github package file"
    )




    args = parser.parse_args()



    # error if filepath doesnt exist
    if args.file:
        # if file path not accurate print error
        if not os.path.exists(args.file):
            print(f"File not found: {args.file}")
            return
        format_results(args.file)
    # if url is provided, will call download function
    elif args.url:
        temp_path = download_file_to_temp(args.url)
        format_results(temp_path)


    format_results(args.file)

if __name__ == "__main__":
    main()