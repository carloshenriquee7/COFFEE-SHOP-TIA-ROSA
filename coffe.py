# SISTEMA COFFEE SHOP TIA ROSA - 

# ============================================================================
# PARTE 1: ESSA PARTE EU FIZ O MENU
# ============================================================================

produtos = [
    {"numeroProduto": "1", "nome": "Café Expresso", "preco": 4.50, "categoria": "Café"},
    {"numeroProduto": "3", "nome": "Café com Chocolate", "preco": 6.00, "categoria": "Café"},
    {"numeroProduto": "4", "nome": "Pão de Açúcar", "preco": 3.50, "categoria": "Pães"},
    {"numeroProduto": "5", "nome": "Pão com Queijo", "preco": 4.00, "categoria": "Pães"},
    {"numeroProduto": "6", "nome": "Água Mineral", "preco": 3.00, "categoria": "Água"},
    {"numeroProduto": "7", "nome": "Suco de Melancia", "preco": 6.00, "categoria": "Sucos"},
    {"numeroProduto": "8", "nome": "Suco de Uva", "preco": 6.50, "categoria": "Sucos"},
    {"numeroProduto": "10", "nome": "Biscoito", "preco": 4.00, "categoria": "Doces"}
]
clientes = []
pedidos = []
proximo_pedido = 1

# ============================================================================
# PARTE 2: AQUI EU FIZ AS FUNÇÕES
# ============================================================================

def buscar_produto(numeroProduto):
    for produto in produtos:
        if produto["numeroProduto"] == numeroProduto:
            return produto
    return None

def buscar_cliente(cpf):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente
    return None

def mostrar_cardapio():
    print("\n" + "="*50)
    print("Menu - COFFEE SHOP TIA ROSA")
    print("="*50)
    
    categorias = {}
    
    for produto in produtos:
        categoria = produto["categoria"]
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(produto)
    
    for categoria, lista_produtos in categorias.items():
        print(f"\n {categoria.upper()}")
        print("-" * 30)
        for produto in lista_produtos:
            print(f"[{produto['numeroProduto']}] {produto['nome']} - R$ {produto['preco']:.2f}")
    print()

def cadastrar_cliente():
    print("\n--- CADASTRO DO CLIENTE ---")
    cpf = input("Digite o CPF (apenas números): ")
    nome = input("Digite o nome completo: ")
    telefone = input("Digite o telefone: ")
    
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print("Cliente já cadastrado!")
            return
    
    novo_cliente = {
        "cpf": cpf,
        "nome": nome,
        "telefone": telefone,
        "pontos": 0
    }
    
    clientes.append(novo_cliente)
    print(f"Cliente {nome} cadastro concluído!")

def consultar_cliente():
    cpf = input("Digite o CPF do cliente: ")
    cliente = buscar_cliente(cpf)
    
    if cliente is None:
        print("Cliente não encontrado!")
        return
    
    print(f"\n--- DADOS DO CLIENTE ---")
    print(f"Nome: {cliente['nome']}")
    print(f"CPF: {cliente['cpf']}")
    print(f"Telefone: {cliente['telefone']}")
    print(f"Pontos: {cliente['pontos']}")

def fazer_pedido():
    global proximo_pedido
    
    print("\n--- FAZER PEDIDO ---")
    
    cpf_cliente = input("Digite o CPF: ")
    
    cliente = buscar_cliente(cpf_cliente)
    if cliente is None:
        print("Cliente não encontrado! Cadastre primeiro.")
        return
    
    print(f"Cliente: {cliente['nome']}")
    
    mostrar_cardapio()
    
    itens_pedido = []
    total_pedido = 0
    
    while True:
        numeroProduto = input("\nDigite o código do produto (ou 'fim' para terminar): ")
        
        if numeroProduto.lower() == "fim":
            break
        
        produto = buscar_produto(numeroProduto)
        if produto is None:
            print("Produto não encontrado!")
            continue
        
        try:
            quantidade = int(input("Digite a quantidade: "))
            if quantidade <= 0:
                print("Quantidade deve ser maior que zero!")
                continue
        except ValueError:
            print("Digite um número válido!")
            continue
        
        subtotal = produto["preco"] * quantidade
        total_pedido += subtotal
        
        item = {
            "numeroProduto": produto["numeroProduto"],
            "nome": produto["nome"],
            "preco": produto["preco"],
            "quantidade": quantidade,
            "subtotal": subtotal
        }
        itens_pedido.append(item)
        
        print(f"Adicionado: {quantidade}x {produto['nome']} - R$ {subtotal:.2f}")
    
    if len(itens_pedido) == 0:
        print("Nenhum item foi adicionado!")
        return
    
    pedido = {
        "numero": proximo_pedido,
        "cpf_cliente": cpf_cliente,
        "nome_cliente": cliente["nome"],
        "itens": itens_pedido,
        "total": total_pedido
    }
    
    pedidos.append(pedido)
    proximo_pedido += 1
    
    cliente["pontos"] += int(total_pedido)
    
    print(f"\n{'='*40}")
    print("RESUMO DO PEDIDO")
    print(f"{'='*40}")
    print(f"Pedido Nº: {pedido['numero']}")
    print(f"Cliente: {cliente['nome']}")
    print("\nItens:")
    for item in itens_pedido:
        print(f"  {item['quantidade']}x {item['nome']} - R$ {item['subtotal']:.2f}")
    print(f"\nTOTAL: R$ {total_pedido:.2f}")
    print(f"Pontos ganhos: {int(total_pedido)}")
    print(f"Total de pontos do cliente: {cliente['pontos']}")

def mostrar_vendas():
    if len(pedidos) == 0:
        print("Nenhum pedido foi feito ainda!")
        return
    
    total_vendas = 0
    for pedido in pedidos:
        total_vendas += pedido["total"]
    
    ticket_medio = total_vendas / len(pedidos)
    
    print(f"\n--- RELATÓRIO DAS VENDAS ---")
    print(f"Número de pedidos: {len(pedidos)}")
    print(f"Valor total vendido: R$ {total_vendas:.2f}")
    print(f"Ticket médio: R$ {ticket_medio:.2f}")

# ============================================================================
# PARTE 3: OPÇOES DE FUNCIONALIDADES
# ============================================================================

def menu_principal():
    while True:
        print("\n" + "="*40)
        print("   SISTEMA COFFEE SHOP TIA ROSA")
        print("="*40)
        print("1 - Mostrar Cardápio")
        print("2 - Cadastrar Cliente")
        print("3 - Consultar Cliente")
        print("4 - Fazer Pedido")
        print("5 - Relatório de Vendas")
        print("0 - Sair")
        print("-"*40)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            mostrar_cardapio()
        elif opcao == "2":
            cadastrar_cliente()
        elif opcao == "3":
            fazer_pedido()
        elif opcao == "4":
            consultar_cliente()
        elif opcao == "5":
            mostrar_vendas()
        elif opcao == "0":
            print("Volte sempre!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# ============================================================================
# PARTE 4: INICIAR O PROGRAMA
# ============================================================================

if __name__ == "__main__":
    print("Bem-vindo ao Sistema Coffee Shop Tia Rosa!")
    print("Sistema iniciando...")

    menu_principal()
