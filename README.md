# 🔐 SBOM Vulnerability Scanner

A security tool designed to scan software dependencies for known vulnerabilities using the [OSV.dev](https://osv.dev) vulnerability database.  
It supports both **CycloneDX SBOMs** and **Python `requirements.txt`** files.  
Built with both **CLI** and **API** interfaces, this project is designed for DevSecOps workflows and is structured to grow into a **contextual RAG (Retrieval-Augmented Generation)** system.

---

## 🚀 Project Overview

This tool helps identify known vulnerabilities in third-party dependencies by:
- Parsing software manifests (SBOMs or Python package lists)
- Querying OSV.dev for CVEs
- Providing enriched output including CVSS-based severity context
- Offering both a **command-line interface (CLI)** and a **RESTful API** for flexible usage

The scanner is modular and supports extensibility like:
- Docker containerization
- PostgreSQL for historical scans
- Kubernetes deployment
- LLM-based vulnerability explanations (planned)

---

## ✅ Key Features

- 📦 **Supports multiple formats**: CycloneDX SBOMs and `requirements.txt`
- 🔗 **GitHub integration**: Accepts GitHub URLs and converts to raw content automatically
- 🌐 **Live CVE lookups**: Powered by OSV.dev
- 🔍 **Severity scoring**: Parses CVSS scores and includes intuitive icons
- 🧰 **API ready**: Built with FastAPI (`/scan` endpoint)
- 💻 **CLI ready**: Simple terminal-based scans

---



## 📦 Example CLI Usage

```bash
# Scan local SBOM
python -m sbom_scanner.cli --file sample_data/sample_sbom.json

# Scan Python requirements.txt
python -m sbom_scanner.cli --file sample_data/requirements.txt

# Scan via GitHub URL
python -m sbom_scanner.cli --url https://github.com/user/repo/blob/main/requirements.txt
```

## 📡 API Usage

You can also interact with the scanner through a RESTful API.

### ▶️ Starting the API

Run the following command to start the FastAPI server locally:

```bash
uvicorn api.main:app --reload
```

### 🔍 POST /scan

**Endpoint:** `/scan`  
**Method:** `POST`  
**Description:** Scan a local file path or a GitHub URL for known vulnerabilities.

---

### ✅ Request Body (JSON)

#### Example using a local file path:
```json
{
  "file_path": "sample_data/sample_sbom.json"
}
```
#### Example using a local file path:
```json
{
  "file_path": "sample_data/sample_sbom.json"
}
```
### ✅ Test API Interactively
```
http://localhost:8000/docs
```
## 🧪 Response Example

```json
{
 "results": [
   {
     "package": "django-helpdesk",
     "version": "0.1.1",
     "cve_id": ["CVE-2021-3994"],
     "summary": "Cross-site scripting vulnerability",
     "severity": "8.8 (High 🔴)"
   }
 ]
}
```