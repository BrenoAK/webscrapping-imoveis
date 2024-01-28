import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = "(inserir a URL)"

headers = {
    'User-Agent'      : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language' : 'en-US,en;q=0.5',
    'DNT'             : '1', # Do Not Track Request Header
    'Connection'      : 'close'
}
data = requests.get(url, headers=headers, timeout=5).text
soup = BeautifulSoup(data,"html.parser")
def buscar_leiloes_imoveis(soup):
    # Substituir o  identificador específico encontrado no site 
    leiloes = soup.find_all(lambda tag: (tag.name == 'img' and '/imagens/imagem_imovel.png' in tag.get('src', '')) or ('imoveis' in tag.get('class', [])))

    links_leiloes = [leilao.find_parent('a')['href'] for leilao in leiloes if leilao.find_parent('a')]
    return links_leiloes

for link in buscar_leiloes_imoveis(soup):
    print(link)