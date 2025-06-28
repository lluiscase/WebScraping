from flask import Flask, render_template,request
from scrap import title,price,urls_produtos,search,open,scraping
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index(): 
    if request.method == 'POST':
        content = request.form['content']
        navegador = open()
        search(navegador,content)
        scraping(navegador)
        table = [{'name':n,'price':p,'url':u} for n,p,u in zip(title,price,urls_produtos)]
        return render_template('result.html', tasks=table)
    title.clear()
    price.clear()
    urls_produtos.clear()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

    
