from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import zipfile as zip
import os

def zipArchive():
    """Compacta os arquivos para dentro do anexos.rar"""
    with zip.ZipFile('anexos.rar', 'w') as zipped:
        for file in os.listdir('anexos'):
            zipped.write(f'anexos/{file}', file)


def downloadArchive(data):
    """Executa o download dos arquivos"""
    archive = requests.get(data['url'])
    with open(f'anexos/{data["name"]}', 'wb') as newArchive:
        newArchive.write((archive.content))


def filter(html, urls=[]):
    """Filtra os endereços de download recebidos"""
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        data = {'name': '', 'url': ''}
        if 'Anexo' in link.getText():
            data['name'] = link.getText().replace(' ', '').replace('(', '').replace(')', '')
            data['url'] = link.get('href')
            urls.append(data)
    return urls


def main():
    os.makedirs('./anexos')
    html = urlopen("https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude")
    links = filter(html)
    for data in links:
        downloadArchive(data)
    zipArchive()
    html.close


if __name__ == "__main__":
    main()
