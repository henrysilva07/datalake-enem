import zipfile 
import requests
from io import BytesIO
import os


# Criando um diretório armazenar os dados do ENEM
os.makedirs("./enem2020", exist_ok=True)

# URL do arquivo 
url = "https://download.inep.gov.br/microdados/microdados_enem_2020.zip"

filebytes = BytesIO(

    requests.get(url).content
)

my_zip = zipfile.ZipFile(filebytes)
my_zip.extractall("./enem2020")

