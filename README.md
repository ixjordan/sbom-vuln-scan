# 📦 SBOM Vulnerability Scanner

A Python-based CLI tool that scans a **CycloneDX JSON SBOM** file and checks listed packages against the [OSV.dev](https://osv.dev) vulnerability database. Designed to help DevSecOps engineers and developers quickly identify known vulnerabilities in third-party dependencies.

---

## 🚀 Project Background

This tool was created as part of my ongoing DevSecOps learning journey. After building a license compliance checker, I wanted to expand into security vulnerabilities — especially within software supply chains.

I started with SBOM parsing to avoid direct dependency file coupling, and then integrated live CVE lookup using the [OSV.dev API](https://osv.dev/docs/#section/Features/Querying). Finally, I incorporated `cvss` parsing to extract and format severity scores in a human-readable format.

---

## 🎯 Features

- ✅ Accepts CycloneDX-formatted SBOMs (JSON)
- 🔍 Extracts `name`, `version` from `library` components
- 🌐 Queries OSV.dev for known vulnerabilities (CVE, GHSA, etc.)
- 🧠 Parses CVSS vector strings using the `cvss` Python library
- 📊 CLI table output with colored formatting via `rich`
- 🔧 Flags the **most severe vulnerability** per package

---

## 📄 Example Usage

```bash
# Basic scan
python -m sbom_scanner.cli --file sample_data/sample_sbom.json
```

Sample Output:
```
🔍 CVE Scan Results from SBOM
┏━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ Package ┃ Version ┃ CVE(s)             ┃ Summary                       ┃ Severity     ┃
┡━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│ requests│ 2.28.1  │ CVE-2023-32681     │ Proxy header leak issue       │ 8.8 (High 🔴) │
│ flask   │ 2.2.3   │ CVE-2023-30861     │ Session cookie exposure risk  │ 4.3 (Medium 🟠)│
└─────────┴─────────┴────────────────────┴───────────────────────────────┴──────────────┘
```

---

## 🔬 CVSS Integration

Vulnerabilities often contain raw CVSS vectors like:
```
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N
```
This tool uses the [`cvss`](https://pypi.org/project/cvss/) library to:
- Parse the vector string
- Calculate the base score
- Return a formatted string like:
  → `8.8 (High 🔴)`

This allows for more intuitive risk visibility and future filtering/sorting.

---

## 🧰 Tech Stack

- Python 3.10+
- `requests` for API calls
- `json` for SBOM parsing
- `rich` for CLI output
- `argparse` for CLI interface
- `cvss` for CVSS vector decoding

---

## 🛠️ File Structure
```
sbom-vuln-scan/
├── sbom_scanner/
│   ├── cli.py
│   ├── osv_api.py
│   ├── scanner.py
│   └── sbom_parser.py
├── sample_data/
│   └── sample_sbom.json
├── requirements.txt
├── README.md
```

---

## 📌 Future Improvements
- [ ] Add export to JSON or CSV
- [ ] Add support for SPDX SBOMs
- [ ] Support full CVE history (not just top match)
- [ ] Ecosystem auto-detection from SBOM `purl`

---


