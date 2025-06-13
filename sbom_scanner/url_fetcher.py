import requests
import tempfile

def download_file_to_temp(url):
    """

    :param url: URL of the file to download
    :return:
    """
    # use helper function to convet to raw url
    url = convert_github_blob_to_raw(url)
    print(f"[i] Using raw URL: {url}")

    # request.get to access url
    response = requests.get(url)
    response.raise_for_status()

    # create temp file (set delete=False so doesnt delete)
    with tempfile.NamedTemporaryFile("w", delete=False) as temp_file:
        # write response(url) to temp file
        temp_file.write(response.text)

    # this will return the temp file path to be parsed in cli tool
    return temp_file.name

def convert_github_blob_to_raw(url:str):


    newUrl=""

    # check if url is already the raw url
    if url.startswith("https://github.com/") and "/blob/" in url:
        # replace with raw url component
        newUrl= url.replace("https://github.com/", "https://raw.githubusercontent.com/")
        # remove "/blob" from url
        newUrl = newUrl.replace("/blob", "")

        # return new formated url for downloading
        return newUrl
    else:
        return url








if __name__ == "__main__":
    temp_path = download_file_to_temp("https://github.com/erinjmonaghan/northcoders_final_project_25/blob/main/requirements.txt")
    print(f"[+] Downloaded to: {temp_path}")





