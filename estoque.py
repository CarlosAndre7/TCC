def listar_estoque():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("""
        SELECT p.nome, e.quantidade, e.preco 
        FROM estoque e
        JOIN produto p ON p.produto_id = e.produto
    """)
    rows = cur.fetchall()
    for row in rows:
        print(f"Produto: {row[0]}, Quantidade: {row[1]}, Preço: R$ {row[2]:.2f}")
    cur.close()
    conn.close()

def verificar_estoque(produto_id):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT VERIFICAR_ESTOQUE(%s);", (produto_id,))
    quantidade = cur.fetchone()[0]
    print(f"Estoque do produto {produto_id}: {quantidade} unidades")
    cur.close()
    conn.close()

def adicionar_estoque(nome_produto, quantidade, preco, fornecedor_id):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("""
        SELECT ADICIONAR_ESTOQUE(%s, %s, %s, %s);
    """, (nome_produto, quantidade, preco, fornecedor_id))
    conn.commit()
    print("Estoque atualizado com sucesso.")
    cur.close()
    conn.close()
