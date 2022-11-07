from tabula.io import convert_into
import zipfile as zip
import os

def zipArchive():
    """Compacta os arquivos para dentro do anexos.rar"""
    with zip.ZipFile('Teste_Gabriel_Rocha.zip', 'w', zip.ZIP_DEFLATED) as zipped:
        zipped.write('Anexo-1.csv')

def main():
    convert_into('AnexoI-Listacompletadeprocedimentos.pdf', 'Anexo-1.csv',  output_format='csv', pages='all', )
    zipArchive()
    
if __name__ == "__main__":
    main()
