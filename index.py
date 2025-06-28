from selenium import webdriver
from bs4 import BeautifulSoup as bs

title = []
price = []
link = []

url = 'https://www.amazon.com.br/s?k=qcy&crid=11ZL1O11Y9BX7&sprefix=%2Caps%2C177&ref=nb_sb_ss_recent_1_0_recent'

navegador = webdriver.Edge()

navegador.get(url)

x = bs(navegador.page_source,'html.parser')
product_tag = x.find_all('div',{'class':'a-section a-spacing-small puis-padding-left-small puis-padding-right-small'})

def scraping():
    for product in product_tag:
        title_tag= product.find('h2')
        nome = title_tag.get_text(strip=True)
        title.append(nome)

        price_tag = product.find('span',class_='a-price-whole')
        if price_tag:
            p = price_tag.get_text(strip=True)
            p_correct = p.replace(',','')
        price.append(p_correct)
    for nome,preco in zip(title,price):
        print(f'Produto: {nome}')
        print(f'Preços: {preco}')    

scraping()
