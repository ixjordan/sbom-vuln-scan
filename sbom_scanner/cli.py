import argparse
import os
from sbom_scanner import scanner
from rich.console import Console
from rich.table import Table



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

    parser.add_argument(
        "--file",
        "-f",
        required=True,
        help = "Path to the CylconeDX SBOM JSON file"
    )

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"File not found: {args.file}")
        return

    format_results(args.file)

if __name__ == "__main__":
    main()