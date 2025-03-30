from scraper import Scraper
from downloader import Downloader
from compressor import Compressor

def main():
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

    scraper = Scraper(url)
    pdf_links = scraper.get_pdf_links()

    downloader = Downloader(pdf_links)
    downloaded_files = downloader.download_pdfs()

    compressor = Compressor(downloaded_files)
    compressor.compress_files()

if __name__ == "__main__":
    main()