import argparse
import os
from sbom_scanner import scanner
from rich.console import Console
from rich.table import Table



def format_results(filepath):
    results = scanner.scan_sbom(filepath)
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
    pass

if __name__ == "__main__":
    format_results("/Users/jordancroft/Documents/Documents - Jordan.’s MacBook Air/GitHub/sbom-vuln-scan/sample_data/sample_sbom.json")