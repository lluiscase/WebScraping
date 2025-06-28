# WebScraping
## Tecnologias e objetivos:
- Crie um pequeno projeto de web scraping (pode usar Python) que colete dados de algum site público (notícias, clima, e-commerce etc.).
- Depois, envie o código que utilizou e também um arquivo .txt com o resultado dos dados coletados ou um breve resumo do que foi extraído. (Dei preferencia a criar um site)
- Python: Selenium, BS4, Flask
- CSS

## Passo-a-Passo:
- Função para o usuário pesquisar o item desejado no site da Amazon (Uso de Selenium);
- Função para fazer o WebScraping da pagina de pesquisa selecionado. Retorno de Titulo, Preço e link do produto (Uso de BS4 e Selenium);
- Criação de um site para visualização dos resultados da WebScraping. (Uso de Flask).

### Possiveis melhoras:
- Tratamento de erro quando a pesquisa é iniciada muito rapido, pode travar todo codigo;
- Filtro para os melhores itens coletados;
- Adicionar os centavos no preço;
- Adicionar imagem dos itens.
- Permitir o usuário escolher qual website quer fazer esse tipo de pesquisa.

### Run:
1. git clone https://github.com/lluiscase/WebScraping
2. python -m venv nomedoseuprojeto
3. pip install -r requirements.txt