"""
Created on Fri Jul 30 13:40:11 2021

@author: Renato
"""

# Importando bibliotecas
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pandas as pd

# Declarando variável cards
cards = []

# Obtendo o HTML

response = urlopen('https://www.euamomomi.com.br/blusa-infantil-feminina')
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

# total de página
pages = 3

# iterando todas as páginas do site
for i in range(pages):
    # Obtendo html
    response = urlopen('https://www.euamomomi.com.br/blusa-infantil-feminina?p=' + str(i + 1))
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    # Obtendo as TAGs de interesse
    anuncios = soup.find('div', {"id": "lista-produtos-area"}).findAll('li')

    # Coletando as informações dos cards
    for anuncio in anuncios:      
   
        ## OBTENDO HIPERLINK        
        if anuncio.find('a') != None:
            link = 'https:' + anuncio.find('a').get('href')
            
            # obtendoHtml do hiperlink (link)
            response = urlopen(link)
            html = response.read().decode('utf-8')
            soup = BeautifulSoup(html, 'html.parser')
            
            # Abrindo dicionário
            card = {}
            
            # Obtendo as TAGs de interesse
            #dados = soup.find('div', {'class': 'lista-dados-produto'})
            if  soup.find('div', {'class': 'container container-product'}) != None:
                dados = soup.find('div', {'class': 'container container-product'})

                # nome do produto
                if dados.find('h1', {'itemprop': 'name'}) != None:
                    card['nome do produto'] = dados.find('h1', {'itemprop': 'name'}).get_text()
                  
                # Descrição do produto
                if  dados.find('div', {'class': 'content'}) != None:
                    card['descrição do produto'] = dados.find('div', {'class': 'content'}).get_text()
                
                #  composição            
                if dados.find('div', {'class': 'composicao'}).find('div', {'class': 'content'}) != None:
                    card['composição'] = dados.find('div', {'class': 'composicao'}).find('div', {'class': 'content'}).get_text()

                # tamanhos (lista com tamanhos disponíveis)
                if dados.find('div', {'id': 'variacao-area-id-2'}) != None:
                    tamanhos = dados.find('div', {'id': 'variacao-area-id-2'}).findAll('li')

                    t = []

                    for tamanho in tamanhos:
                        if tamanho.get("data-estoque") != '0':
                            num = tamanho.get_text().replace(' ', '')
                            t.append(num)
                        
                    card['tamanhos'] = t
                 
                # fotos (lista com as urls das imagens)
                if dados.findAll('li', {'class': 'clearfix'}) != None:
                    todas_imagem = dados.findAll('li', {'class': 'clearfix'})
                    
                    x = []
                    
                    for i in todas_imagem:
                        im = i.get('data-img-full')
                        x.append(im)
                    card['fotos'] = x

                # Adicionando resultado à lista cards
                cards.append(card)


# Criando um DataFrame com os resultados
dataset = pd.DataFrame(cards)
dataset.to_excel('./dataset.xlsx', index = False, encoding = 'utf-8-sig')
#dataset