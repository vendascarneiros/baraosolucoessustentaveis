# app.py (ou routes.py)

from flask import Flask, render_template

app = Flask(__name__)

# --- Dados de Exemplo (Simulando um Banco de Dados) ---
produtos_db = {
    1: {
        'nome': 'Otimizador Inteligente v2.0',
        'preco': 159.90,
        'descricao': 'A mais nova versão do nosso otimizador, com IA para prever a melhor hora de compra e venda.',
        'disponivel_site': True,
        'link_ml': 'https://produto.mercadolivre.com.br/ML12345'
    },
    2: {
        'nome': 'Licença Premium Anual',
        'preco': 299.00,
        'descricao': 'Acesso irrestrito a todas as funcionalidades e relatórios avançados por um ano.',
        'disponivel_site': False,
        'link_ml': 'https://produto.mercadolivre.com.br/ML67890'
    }
}

# --- Rota Principal (Opcional, só para listar os produtos) ---
@app.route('/')
def index():
    # Renderiza uma página com a lista de produtos (opcional)
    return render_template('index.html', produtos=produtos_db)


# --- ROTA 1: Detalhes do Produto (O Nosso Foco) ---
@app.route('/produto/<int:id_produto>')
def detalhes(id_produto):
    """
    Busca os dados de um produto pelo ID e renderiza a página de detalhes.
    """
    # 1. Buscar o produto no "Banco de Dados" (nosso dicionário)
    produto = produtos_db.get(id_produto)

    # 2. Tratar o erro (Produto não encontrado)
    if produto is None:
        # Poderia ser um template 404
        return "Produto não encontrado", 404

    # 3. Renderizar o template 'detalhes.html' (o seu código Jinja)
    # Passamos o objeto 'produto' e o 'id' para o template.
    return render_template(
        'detalhes.html',
        produto=produto,
        id=id_produto
    )


# --- ROTA 2: Ação de Compra no Site (Próximo Passo) ---
@app.route('/comprar/<int:id_produto>', methods=['POST'])
def comprar_site(id_produto):
    """
    Inicia o processo de checkout no site.
    (Essa rota será o nosso Próximo Passo 2)
    """
    return f"Iniciando checkout do Produto ID: {id_produto}. Redirecionando para o carrinho..."


if __name__ == '__main__':
    # Você precisará do Jinja template salvo como 'detalhes.html' na pasta 'templates'
    app.run(debug=True)
