from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
from selenium.webdriver.edge.options import Options
title = []
price = []
urls_produtos = []

def open():
    url_principal = 'https://www.amazon.com.br/?tag=admarketbr-20&ref=pd_sl_ee1f051d03fe7ebc7cf11aab597ceb571053edd1ba0cd53f0fc76ed3&mfadid=adm'
    options = Options()
    options.add_argument("--headless")
    navegador = webdriver.Edge(options=options)
    navegador.get(url_principal)
    return navegador

def search(navegador,item):
    box = navegador.find_element("id","twotabsearchtextbox")
    search = navegador.find_element("id","nav-search-submit-button")
    box.click()
    box.send_keys(item)
    search.click()
    time.sleep(10)

def scraping(navegador):
    url_secundaria = navegador.current_url
    navegador.get(url_secundaria)
    x = bs(navegador.page_source,'html.parser')
    product_tag = x.find_all('div',{'class':'a-section a-spacing-small puis-padding-left-small puis-padding-right-small'})
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