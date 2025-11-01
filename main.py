from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# --- NOVOS PRODUTOS REAIS ---
PRODUTOS = {
    "1": {
        "nome": "Válvula 2 Polegadas Para Carneiro Hidráulico",
        "preco": 255.00,
        "descricao": "Válvula de retenção em bronze de 2 polegadas, ideal para o coração do seu Carneiro Hidráulico.",
        "link_ml": "https://mercadolivre.com/sec/2q3DLFy",
        "disponivel_site": True, # Assume que a compra no site está ativa
        "img_url": "1000011480_valvula2pol.jpg" # Nome fictício para a imagem no Mercado Livre
    },
    "2": {
        "nome": "Carneiro Hidráulico N1 PVC (Modelo Básico)",
        "preco": 454.50,
        "descricao": "Carneiro Hidráulico N1 em PVC, um modelo acessível e eficiente para bombeamento de água.",
        "link_ml": "https://mercadolivre.com/sec/29X1pkd",
        "disponivel_site": False, # Assume que a compra no site está desativada
        "img_url": "1000011480_carneiropvc.jpg" 
    },
    "3": {
        "nome": "Válvula Para Carneiro Hidráulico N 40 Aço Inox",
        "preco": 180.00, # Preço ajustado, pois não estava visível na imagem
        "descricao": "Válvula robusta N 40 em Aço Inox para máxima durabilidade e desempenho no seu Carneiro Hidráulico.",
        "link_ml": "https://mercadolivre.com/sec/2fZ79SA",
        "disponivel_site": True,
        "img_url": "1000011480_valvula40inox.jpg" 
    },
    "4": {
        "nome": "Carneiro Hidráulico Barão Da Cunha 50mm",
        "preco": 750.00, # Preço ajustado, pois não estava visível na imagem
        "descricao": "Modelo de alto desempenho 'Barão da Cunha' de 50mm. Máxima eficiência de bombeamento garantida.",
        "link_ml": "https://mercadolivre.com/sec/22mvpP4",
        "disponivel_site": True,
        "img_url": "1000011480_carneiro50mm.jpg" 
    }
}
# --- FIM DOS NOVOS PRODUTOS REAIS ---


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

    # Lógica de processamento de pagamento e estoque...

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
