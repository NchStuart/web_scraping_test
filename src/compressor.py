import os
import zipfile

class Compressor:
    def __init__(self, files_to_compress):
        self.files_to_compress = files_to_compress

    def compress_files(self):
        download_path = os.path.join(os.getcwd(), 'downloads')

        zip_filename = os.path.join(download_path, 'pdf_anexos.zip')

        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for file in self.files_to_compress:
                zipf.write(file, os.path.basename(file))

        print(f"Arquivos compactados em: {zip_filename}")

        for file in self.files_to_compress:
            os.remove(file)

        print(f"Arquivos temporários excluídos.")