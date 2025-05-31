# Função que exibe o menu principal para o usuário
def mostrar_menu():
    print("\n==== Gerenciador de Tarefas ====")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Deletar tarefa")
    print("4. Sair")

# Função para adicionar uma nova tarefa à lista
def adicionar_tarefa(tarefas):
    tarefa = input("Digite a descrição da nova tarefa: ").strip()
    if tarefa:
        tarefas.append(tarefa)  # Adiciona tarefa se não for vazia
        print("✅ Tarefa adicionada com sucesso!")
    else:
        print("⚠️ Tarefa vazia não pode ser adicionada.")

# Função que exibe todas as tarefas da lista
def listar_tarefas(tarefas):
    if not tarefas:
        print("📭 Nenhuma tarefa cadastrada.")
    else:
        print("\n📋 Lista de Tarefas:")
        # Usa enumerate para numerar as tarefas a partir de 1
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

# Função que permite remover uma tarefa da lista pelo número
def deletar_tarefa(tarefas):
    listar_tarefas(tarefas)  # Mostra as tarefas antes de pedir entrada
    if not tarefas:
        return  # Se não houver tarefas, sai da função
    try:
        indice = int(input("Digite o número da tarefa a ser deletada: "))
        if 1 <= indice <= len(tarefas):
            removida = tarefas.pop(indice - 1)  # Remove a tarefa com base no índice
            print(f"🗑️ Tarefa '{removida}' removida com sucesso.")
        else:
            print("❌ Número inválido.")  # Fora do intervalo válido
    except ValueError:
        print("❌ Entrada inválida. Por favor, digite um número.")  # Entrada não numérica

# Função principal que executa o loop do menu
def main():
    tarefas = []  # Lista que armazena as tarefas
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção (1-4): ")
        
        # Estrutura condicional para tratar a escolha do usuário
        if escolha == '1':
            adicionar_tarefa(tarefas)
        elif escolha == '2':
            listar_tarefas(tarefas)
        elif escolha == '3':
            deletar_tarefa(tarefas)
        elif escolha == '4':
            print("👋 Saindo do programa. Até a próxima!")
            break  # Encerra o loop e o programa
        else:
            print("❌ Opção inválida. Tente novamente.")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
