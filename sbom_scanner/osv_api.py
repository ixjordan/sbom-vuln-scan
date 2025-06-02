import requests
import json

def query_osv(name, version, ecosystem= "PyPI"):
    """
    Queries OSV.dev for CVEs associated with a specific package version.

    :param name: Name of the package (e.g 'requests')
    :param version:  Version String (e.g. '2.28.1')
    :param ecosystem: Package ecosystem (e.g. 'PyPI', 'NPM', etc.)
    :return: List of CVEs (can be empty) or None if request fails
    """
    # url for post request
    url = "https://api.osv.dev/v1/query"


    # payload to go to the post request
    if version is not None:
        payload = {
            "package":{
                "name": name,
                "ecosystem": ecosystem
            },
            "version": version
        }
    else:
        # if version isnt specified in package
        payload = {
            "package": {
                "name": name,
                "ecosystem": ecosystem
            },
        }


    try:
        # make a post request to OSV api
        response = requests.post(url,json=payload)
        response.raise_for_status()
        data = response.json()

        return data.get("vulns", [])

    except Exception as e:
        print("Sorry trouble getting data")
        return []

if __name__ == "__main__":
   print(query_osv("langroid", None))