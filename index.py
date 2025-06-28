from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs

title = []
price = []
urls_produtos = []

url_principal = 'https://www.amazon.com.br/?tag=admarketbr-20&ref=pd_sl_ee1f051d03fe7ebc7cf11aab597ceb571053edd1ba0cd53f0fc76ed3&mfadid=adm'

navegador = webdriver.Edge()

navegador.get(url_principal)

def search(item):
    navegador.maximize_window()
    box = navegador.find_element("id","twotabsearchtextbox")
    search = navegador.find_element("id","nav-search-submit-button")
    box.click()
    box.send_keys(item)
    search.click()
    time.sleep(10)

text = input(str("O que deseja pesquisar na amazon? "))
search(text)
url_secundaria = navegador.current_url
navegador.get(url_secundaria)
print(url_secundaria)

x = bs(navegador.page_source,'html.parser')
product_tag = x.find_all('div',{'class':'a-section a-spacing-small puis-padding-left-small puis-padding-right-small'})

def scraping():
    for product in product_tag:
        title_tag= product.find('h2')
        nome = title_tag.get_text(strip=True)
        title.append(nome)
        link_tag = product.find('a',class_='a-link-normal s-line-clamp-4 s-link-style a-text-normal')
        link_result = 'www.amazon.com.br'+link_tag['href']
        urls_produtos.append(link_result)
        price_tag = product.find('span',class_='a-price-whole')
        if price_tag:
            p = price_tag.get_text(strip=True)
            p_correct = p.replace(',','')
            price.append(p_correct)
    for nome,preco,link in zip(title,price,urls_produtos):
        print(f'Produto: {nome}')
        print(f'Preços: {preco}')
        print(f'URL: {link}')    

scraping()
