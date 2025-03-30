import requests
import os

class Downloader:
    def __init__(self, links):
        self.links = links

    def download_pdfs(self):
        downloaded_files = []
        
        if not os.path.exists('downloads'):
            os.makedirs('downloads')
        
        for url in self.links:
            if not url.startswith('http'):
                url = f"https://www.gov.br{url}"

            response = requests.get(url)
            
            filename = url.split("/")[-1]
            
            file_path = os.path.join('downloads', filename)
            with open(file_path, 'wb') as file:
                file.write(response.content)
            
            downloaded_files.append(file_path)
        
        return downloaded_files