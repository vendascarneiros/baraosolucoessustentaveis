from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Simulação de um banco de dados de produtos
PRODUTOS = {
    "1": {
        "nome": "Smartphone Modelo X",
        "preco": 1500.00,
        "descricao": "Um smartphone poderoso com câmera de alta resolução.",
        "link_ml": "https://www.mercadolivre.com.br/smartphone-modelo-x/p/MLB12345678", # Substitua pelo link real
        "disponivel_site": True
    },
    "2": {
        "nome": "Notebook Gamer Y",
        "preco": 6800.00,
        "descricao": "O melhor para jogos e produtividade.",
        "link_ml": "https://www.mercadolivre.com.br/notebook-gamer-y/p/MLB87654321", # Substitua pelo link real
        "disponivel_site": False
    }
}

@app.route("/")
def index():
    """Rota para a página inicial, listando os produtos."""
    return render_template("index.html", produtos=PRODUTOS.items())

@app.route("/produto/<id_produto>")
def produto(id_produto):
    """Rota para a página de detalhes de um produto."""
    produto_info = PRODUTOS.get(id_produto)
    if not produto_info:
        return "Produto não encontrado", 404
    
    # Passa as informações do produto para o template
    return render_template("produto.html", id=id_produto, produto=produto_info)

@app.route("/comprar_site/<id_produto>", methods=["POST"])
def comprar_site(id_produto):
    """Simula a compra dentro do site."""
    produto_info = PRODUTOS.get(id_produto)
    if not produto_info or not produto_info.get("disponivel_site"):
        return "Compra no site indisponível ou produto não encontrado.", 400

    # Lógica de processamento de pagamento e estoque... (Ex: Integração com Mercado Pago, etc.)

    # Após a "compra", redireciona para a página de sucesso
    return redirect(url_for("sucesso", nome=produto_info["nome"]))

@app.route("/sucesso")
def sucesso():
    """Página de sucesso após a compra."""
    nome_produto = request.args.get("nome", "o produto")
    return render_template("sucesso.html", nome_produto=nome_produto)

# Ponto de entrada para o Render (Gunicorn)
if __name__ == "__main__":
    app.run(debug=True)
