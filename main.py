from estoque import listar_estoque, verificar_estoque, adicionar_estoque

def menu():
    while True:
        print("\n=== Farmácia - Gerenciamento de Estoque ===")
        print("1. Listar estoque")
        print("2. Verificar estoque por produto")
        print("3. Adicionar ao estoque")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_estoque()
        elif opcao == "2":
            produto_id = int(input("ID do produto: "))
            verificar_estoque(produto_id)
        elif opcao == "3":
            nome = input("Nome do produto: ")
            qtd = int(input("Quantidade: "))
            preco = float(input("Preço unitário: "))
            fornecedor = int(input("ID do fornecedor: "))
            adicionar_estoque(nome, qtd, preco, fornecedor)
        elif opcao == "4":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
