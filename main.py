tarefas = []
opcao = ""

while opcao != "5":
    print("\n--- GERENCIADOR DE TAREFAS ---")
    print("1. Adicionar tarefa")
    print("2. Ver lista de tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")

    opcao = input("Escolha uma opção (1 a 5): ")

    if opcao == "1":
        nome_tarefa = input("Digite a nova tarefa: ")
        tarefa_dict = {
            "titulo": nome_tarefa,
            "status": "pendente"
        }
        tarefas.append(tarefa_dict)
        print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")

    elif opcao == "2":
        print("\n--- LISTA DE TAREFAS ---")
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada ainda.")
        else:
            for i, t in enumerate(tarefas):
                status_formatted = "[✓] Concluída" if t["status"] == "concluída" else "[ ] Pendente"
                print(f"{i + 1}. {t['titulo']} - {status_formatted}")

    elif opcao == "3":
        print("\n--- MARCAR TAREFA COMO CONCLUÍDA ---")
        if len(tarefas) == 0:
            print("Nenhuma tarefa para concluir.")
        else:
            for i, t in enumerate(tarefas):
                print(f"{i + 1}. {t['titulo']} [{t['status']}]")

            numero = int(input("\nDigite o número da tarefa concluída: ")) - 1

            if 0 <= numero < len(tarefas):
                tarefas[numero]["status"] = "concluída"
                print(
                    f"Sucesso! Tarefa '{tarefas[numero]['titulo']}' marcada como concluída.")
            else:
                print("Número de tarefa inválido!")

    elif opcao == "4":
        print("\n--- REMOVER TAREFA ---")
        if len(tarefas) == 0:
            print("Nenhuma tarefa para remover.")
        else:
            # Mostramos as tarefas para o usuário saber qual número escolher
            for i, t in enumerate(tarefas):
                print(f"{i + 1}. {t['titulo']}")

            numero = int(
                input("\nDigite o número da tarefa que deseja apagar: ")) - 1

            # Validação do índice digitado
            if 0 <= numero < len(tarefas):
                # O método pop() remove a tarefa do índice selecionado e retorna o item removido
                tarefa_removida = tarefas.pop(numero)
                print(
                    f"A tarefa '{tarefa_removida['titulo']}' foi removida com sucesso!")
            else:
                print("Número de tarefa inválido!")

    elif opcao == "5":
        print("\nSaindo do programa. Até logo!")

    else:
        print("\nOpção inválida! Escolha de 1 a 5.")

   










