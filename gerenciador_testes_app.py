# Função que exibe o menu principal
def mostrar_menu():
    print("\n==== Gerenciador de Cenários de Teste ====")
    print("1. Adicionar cenário")
    print("2. Listar cenários")
    print("3. Deletar cenário")
    print("4. Sair")

# Função para adicionar um novo cenário à lista
def adicionar_cenario(cenarios):
    descricao = input("Digite a descrição do cenário de teste: ").strip()
    if descricao:
        cenarios.append(descricao)
        print("✅ Cenário adicionado com sucesso!")
    else:
        print("⚠️ Descrição vazia não pode ser adicionada.")

# Função que lista todos os cenários armazenados
def listar_cenarios(cenarios):
    if not cenarios:
        print("📭 Nenhum cenário cadastrado.")
    else:
        print("\n📋 Lista de Cenários de Teste:")
        for i, cenario in enumerate(cenarios, start=1):
            print(f"{i}. {cenario}")

# Função para deletar um cenário com base em sua posição
def deletar_cenario(cenarios):
    listar_cenarios(cenarios)
    if not cenarios:
        return
    try:
        indice = int(input("Digite o número do cenário a ser deletado: "))
        if 1 <= indice <= len(cenarios):
            removido = cenarios.pop(indice - 1)
            print(f"🗑️ Cenário '{removido}' removido com sucesso.")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Entrada inválida. Por favor, digite um número.")

# Função principal que executa o loop do programa
def main():
    cenarios = []
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção (1-4): ")
        
        if escolha == '1':
            adicionar_cenario(cenarios)
        elif escolha == '2':
            listar_cenarios(cenarios)
        elif escolha == '3':
            deletar_cenario(cenarios)
        elif escolha == '4':
            print("👋 Encerrando o gerenciador de cenários. Até logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

# Ponto de entrada
if __name__ == "__main__":
    main()
