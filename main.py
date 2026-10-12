tarefas = []
opcao = ""

while opcao != "4":  # Agora a opção de sair é 4!
    print("\n--- GERENCIADOR DE TAREFAS (Com Dicionários) ---")
    print("1. Adicionar tarefa")
    print("2. Ver lista de tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Sair")

    opcao = input("Escolha uma opção (1, 2, 3 ou 4): ")

    if opcao == "1":
        nome_tarefa = input("Digite a nova tarefa: ")

        # Criamos o dicionário da tarefa
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
                # Usamos um ícone simples para destacar o status!
                status_formatted = "[✓] Concluída" if t["status"] == "concluída" else "[ ] Pendente"
                print(f"{i + 1}. {t['titulo']} - {status_formatted}")

    elif opcao == "3":
        print("\n--- MARCAR TAREFA COMO CONCLUÍDA ---")
        if len(tarefas) == 0:
            print("Nenhuma tarefa para concluir.")
        else:
            # Mostramos as tarefas primeiro para o usuário escolher o número
            for i, t in enumerate(tarefas):
                print(f"{i + 1}. {t['titulo']} [{t['status']}]")

            numero = int(input("\nDigite o número da tarefa concluída: ")) - 1

            # Verificamos se o número digitado é válido
            if 0 <= numero < len(tarefas):
                # AQUI ESTÁ O CONCEITO CHAVE: alterando a chave 'status' do dicionário selecionado
                tarefas[numero]["status"] = "concluída"
                print(
                    f"Sucesso! Tarefa '{tarefas[numero]['titulo']}' marcada como concluída.")
            else:
                print("Número de tarefa inválido!")

    elif opcao == "4":
        print("\nSaindo do programa. Até logo!")

    else:
        print("\nOpção inválida! Escolha de 1 a 4.")


   










