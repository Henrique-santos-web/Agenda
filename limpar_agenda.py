# agenda = [
#     {"Nome":"","Número":""}
# ]


# while True:

#     print("------- AGENDA -------")
#     print("- Adicionar")
#     print("- Ver Contatos")
#     print("- Sair")
#     execucao = input("")
#     print("----------------------")

#     agenda = execucao

#     if agenda == "Adicionar":
#         nome_contato = input("Nome: ")
#         numero_contato = input("Número: ")

#     elif agenda == "Ver Contatos":
#         print({agenda})       
# # Desafio não concluído e a frustração? É extremamente frustrante não ser capaz de criar uma simples agenda 



# correção do professor

import time
import os
agenda = []

TEMPO = 3

while True:
    os.system("cls") #limpar o terminal do código

    print("----- AGENDA -----")
    print("1. Adicionar")
    print("2. Ver Contatos")
    print("3. Limpar contatos")
    print("4. Sair")

    opcao = input("Escolha uma opçao: ")

    if opcao == "1":
        os.system("cls")
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o E-mail: ")

        contato_clone = False

        for contato_existente in agenda:
            if contato_existente['telefone'].strip().lower() == telefone.strip().lower():
                contato_clone = True
                break

        if contato_clone:
            print(f"Este número({telefone}) já existe!")
            time.sleep(TEMPO)
        else:
            contato = {
                "nome": nome,
                "telefone": telefone,
                "email": email
            }
            agenda.append(contato)

            print(f"{contato['nome']} foi adicionado com sucesso!!")
            time.sleep(TEMPO)

    elif opcao == "2":
        os.system("cls")

        if len(agenda) == 0:
            print("A lista de contatos está vazia!")
            time.sleep(TEMPO)
            continue
        
        print("----- LISTA DE CONTATOS -----")

        if len(agenda) == 1:
            print(f"Você tem {len(agenda)} contato!!")
        elif len(agenda) > 1:
            print(f"Você tem {len(agenda)} contatos!!")
        
        for contato in agenda:
            print(f"| Nome: {contato['nome']} --- Telefone: {contato['telefone']} --- E-mail: {contato['email']} |")
        
        print("----- FIM DA LISTA DE CONTATOS -----")
        time.sleep(TEMPO)

    elif opcao == "3":
        agenda.clear()
        print("Você excluiu todos os contatos!!")
        time.sleep(TEMPO)

    elif opcao == "4":
        os.system("cls")
        print("Finalizando aplicação")
        time.sleep(TEMPO)
        break
    else:
        print("Opção inválida, tente novamente")
        time.sleep(TEMPO)