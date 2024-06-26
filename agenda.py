def opcoes():
    print("Agenda de contatos")
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Listar contatos")
    print("4 - Editar contato")
    print("5 - Listar favoritos")
    print("6 - Sair")


contatos = []


def adicionar_contato(contatos):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    fav = input("Favorito (s/n): ")
    novo_contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": fav}
    contatos.append(novo_contato)


def remover_contato(contatos):
    remover_nome = input("Nome para ser removido: ")
    for contato in contatos:
        if contato["nome"] == remover_nome:
            contatos.remove(contato)
            print("Contato removido com sucesso")
            return
    print("Contato não encontrado")


def listar_contatos(contatos):
    for contato in contatos:
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"Email: {contato['email']}")
        print(f"Favorito: {contato['favorito']}")
        print()


def editar_contato(contatos):
    editar_nome = input("Nome para ser editado: ")
    for contato in contatos:
        if contato["nome"] == editar_nome:
            qual = input("O que deseja editar? (1- nome 2 - telefone 3 - email 4 - favorito): ")
            if qual == "1":
                contato["nome"] = input("Novo nome: ")
            elif qual == "2":
                contato["telefone"] = input("Novo telefone: ")
            elif qual == "3":
                contato["email"] = input("Novo email: ")
            elif qual == "4":
                contato["favorito"] = input("Novo favorito: ")
            else:
                print("Opção inválida")
            return
    print("Contato não encontrado")


def listar_favoritos(contatos):
    for contato in contatos:
        if contato["favorito"] == "s":
            print(f"Nome: {contato['nome']}")
            print()


while True:
    opcoes()
    opcao = input("Escolha: ")
    if opcao == "1":
        adicionar_contato(contatos)
    elif opcao == "2":
        remover_contato(contatos)
    elif opcao == "3":
        listar_contatos(contatos)
    elif opcao == "4":
        editar_contato(contatos)
    elif opcao == "5":
        listar_favoritos(contatos)
    elif opcao == "6":
        break
    else:
        print("Opção inválida")
