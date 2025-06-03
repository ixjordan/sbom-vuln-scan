import requests
import tempfile

def download_file_to_temp(url):

    response = requests.get(url)
    response.raise_for_status()

    # create temp file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:

        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                decoded = chunk.decode('utf-8')
                temp_file.write(decoded)
                print(decoded)



def convert_to_raw_github_url(url):

    # pattern match to githubs blob url
    github_pattern = r'https://github\.com/([^/]+)/([^/]+)/blob/(.+)'

if __name__=="__main__":
    download_file_to_temp("https://github.com/erinjmonaghan/northcoders_final_project_25/blob/main/requirements.txt")
