Web Scraping Test

Funcionalidades
✅ Web Scraping: Coleta os links de arquivos PDF na página alvo.
✅ Download: Baixa os arquivos PDF e os salva na pasta downloads.
✅ Compacta os arquivos PDF baixados em um .zip e remove os arquivos temporários.

Estrutura do Projeto

│-- downloads/               # Pasta onde os arquivos zip são armazenados (caso não exista, ele criará sozinho)
│-- src/                     # Código-fonte do projeto
│   ├── main.py              # Arquivo principal para executar o script
│   ├── scraper.py           # Coleta os links dos PDFs
│   ├── downloader.py        # Baixa os PDFs
│   ├── compressor.py        # Compacta os PDFs baixados
│-- requirements.txt         # Dependências do projeto
│-- .gitignore               # Define arquivos ignorados pelo Git
│-- README.md                # Documentação do projeto
│-- LICENSE                  # Licença do projeto


Como Rodar o Projeto?

Clone o repositório:

git clone https://github.com/NchStuart/web_scraping_test/
cd web_scraping_test

Crie um ambiente virtual:

python -m venv venv

Ative o ambiente virtual:

No Windows:

.\venv\Scripts\activate

No Linux/Mac:

source venv/bin/activate

Instale as dependências:

pip install -r requirements.txt

Execute o script:

python src/main.py

Dependências

requests - Para fazer as requisições HTTP e baixar os arquivos PDF.

zipfile - Para compactação dos arquivos PDF.

os - Para manipulação de diretórios.

Selenium - Para realizar a automação no navegador
