clientes = []

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    
    cliente = {
        "Nome": nome,
        "Email": email,
        "Telefone": telefone
    }
    
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def listar_clientes():
    if not clientes:
        print("Não há clientes cadastrados.")
    else:
        print("Lista de clientes:")
        for cliente in clientes:
            print(f"Nome: {cliente['Nome']}, Email: {cliente['Email']}, Telefone: {cliente['Telefone']}")

def menu():
    print("\n--- Menu ---")
    print("1. Cadastrar cliente")
    print("2. Listar clientes")
    print("3. Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            listar_clientes()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
