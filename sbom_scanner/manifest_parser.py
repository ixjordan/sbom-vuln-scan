


def parse_requirements_txt(filepath):
    """
    Parses a python requirements.txt file.

    :param filepath: Path to requirements.txt file
    :return: List
    """


    packages = []

    try:
        with open(filepath) as f:
            # through line by line
            for line in f:
                # strip each line
                line = line.strip()
                # ignore empty lines or comments
                if line =="" or line.startswith("#"):
                    continue

                if "==" in line:
                    package, version = line.split("==")
                    packages.append((package.strip(), version.strip()))

                elif "~=" in line:
                    package, version = line.split("~=")
                    packages.append((package.strip(), version.strip()))

                elif ">=" in line:
                    package, version = line.split(">=")
                    packages.append((package.strip(), version.strip()))

                else:
                    package = line.strip()
                    packages.append((package, "Unknown"))

    # exception errors
    except FileNotFoundError:
        print("Sorry file not found")
    except Exception as e:
        print("Sorry error occurred")

    return packages

if __name__=="__main__":
    filepath = "/Users/jordancroft/Documents/Documents - Jordan.’s MacBook Air/GitHub/sbom-vuln-scan/sample_data/requirements.txt"
    print(parse_requirements_txt(filepath))