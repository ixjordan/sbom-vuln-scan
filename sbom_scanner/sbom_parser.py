import json


def parse_sbom(filepath):
    """
    Parses a CYcloneDX JSON SBOM file and returns a list of (name, version) tuples
    :param filepath: file path to sbom file
    :return: returns a list of tuples (name, version)
    """
    libraries = []
    try:
        with open(filepath) as f:
            # load json contents from file
            data = json.load(f)

            # get components
            components = data.get("components", [])

            for component in components:
                if component["type"] == "library":
                    name = component.get("name")
                    version = component.get("version")
                    if name and version:
                        libraries.append((name, version))


    except FileNotFoundError:
        print("Sorry file was not found")
    return libraries

if __name__ == "__main__":
    parse_sbom("/Users/jordancroft/Documents/Documents - Jordan.’s MacBook Air/GitHub/sbom-vuln-scan/sample_data/sample_sbom.json")