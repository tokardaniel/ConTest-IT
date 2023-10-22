from typing import List
import requests
import json

class DownloadData:

    @classmethod
    def download(cls, url) -> List[dict]:
        response = requests.get(url)

        return json.loads(response.text)
