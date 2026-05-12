# =========================
# SISTEMA DE RPG
# =========================

personagens = []
npcs = []
campanhas = []

classes_disponiveis = [
    "Mago",
    "Guerreiro",
    "Ladino",
    "Arqueiro",
    "Clérigo"
]

# =========================
# FUNÇÕES AUXILIARES
# =========================

def pausar():
    input("\nPressione ENTER para continuar...")


# =========================
# PERSONAGENS
# =========================

def criar_personagem():

    print("\n=== CRIAÇÃO DE PERSONAGEM ===")

    nome = input("Digite o nome do personagem: ")

    print("\nClasses disponíveis:")

    for i, classe in enumerate(classes_disponiveis, start=1):
        print(f"{i} - {classe}")

    escolha = int(input("\nEscolha a classe: "))

    classe_escolhida = classes_disponiveis[escolha - 1]

    personagem = {
        "nome": nome,
        "classe": classe_escolhida,
        "inventario": []
    }

    personagens.append(personagem)

    print(f"\nPersonagem {nome} criado com sucesso!")
    pausar()


def ver_personagens():

    print("\n=== PERSONAGENS ===")

    if not personagens:
        print("Nenhum personagem criado.")
        pausar()
        return

    for i, p in enumerate(personagens, start=1):

        print(f"\n{i} - {p['nome']}")
        print(f"Classe: {p['classe']}")

        if p["inventario"]:
            print("Inventário:")
            for item in p["inventario"]:
                print(f"- {item}")
        else:
            print("Inventário vazio.")

    pausar()


def alterar_personagem():

    print("\n=== ALTERAR PERSONAGEM ===")

    if not personagens:
        print("Nenhum personagem criado.")
        pausar()
        return

    for i, p in enumerate(personagens, start=1):
        print(f"{i} - {p['nome']}")

    escolha = int(input("\nEscolha o personagem: "))

    personagem = personagens[escolha - 1]

    novo_nome = input("Novo nome: ")

    print("\nClasses disponíveis:")

    for i, classe in enumerate(classes_disponiveis, start=1):
        print(f"{i} - {classe}")

    nova_classe = int(input("\nEscolha a nova classe: "))

    personagem["nome"] = novo_nome
    personagem["classe"] = classes_disponiveis[nova_classe - 1]

    print("\nPersonagem atualizado com sucesso!")
    pausar()


def adicionar_item():

    print("\n=== ADICIONAR ITEM ===")

    if not personagens:
        print("Nenhum personagem criado.")
        pausar()
        return

    for i, p in enumerate(personagens, start=1):
        print(f"{i} - {p['nome']}")

    escolha = int(input("\nEscolha o personagem: "))

    item = input("Nome do item: ")

    personagens[escolha - 1]["inventario"].append(item)

    print("Item adicionado com sucesso!")
    pausar()


# =========================
# NPCs
# =========================

def criar_npc():

    print("\n=== CRIAR NPC ===")

    nome = input("Digite o nome do NPC: ")
    funcao = input("Digite a função do NPC: ")

    npc = {
        "nome": nome,
        "funcao": funcao
    }

    npcs.append(npc)

    print("NPC criado com sucesso!")
    pausar()


def ver_npcs():

    print("\n=== NPCs ===")

    if not npcs:
        print("Nenhum NPC criado.")
        pausar()
        return

    for i, npc in enumerate(npcs, start=1):
        print(f"\n{i} - {npc['nome']}")
        print(f"Função: {npc['funcao']}")

    pausar()


def alterar_npc():

    print("\n=== ALTERAR NPC ===")

    if not npcs:
        print("Nenhum NPC criado.")
        pausar()
        return

    for i, npc in enumerate(npcs, start=1):
        print(f"{i} - {npc['nome']}")

    escolha = int(input("\nEscolha o NPC: "))

    npc = npcs[escolha - 1]

    npc["nome"] = input("Novo nome: ")
    npc["funcao"] = input("Nova função: ")

    print("NPC atualizado com sucesso!")
    pausar()


# =========================
# CAMPANHAS
# =========================

def criar_campanha():

    print("\n=== CRIAR CAMPANHA ===")

    nome = input("Digite o nome da campanha: ")
    historia = input("Digite a história da campanha: ")

    campanha = {
        "nome": nome,
        "historia": historia,
        "sessoes": []
    }

    campanhas.append(campanha)

    print("Campanha criada com sucesso!")
    pausar()


def ver_campanhas():

    print("\n=== CAMPANHAS ===")

    if not campanhas:
        print("Nenhuma campanha criada.")
        pausar()
        return

    for i, campanha in enumerate(campanhas, start=1):

        print(f"\n{i} - {campanha['nome']}")
        print(f"História: {campanha['historia']}")

        print("Sessões:")

        if campanha["sessoes"]:
            for s in campanha["sessoes"]:
                print(f"- {s}")
        else:
            print("Nenhuma sessão cadastrada.")

    pausar()


def adicionar_sessao():

    print("\n=== ADICIONAR SESSÃO ===")

    if not campanhas:
        print("Nenhuma campanha criada.")
        pausar()
        return

    for i, campanha in enumerate(campanhas, start=1):
        print(f"{i} - {campanha['nome']}")

    escolha = int(input("\nEscolha a campanha: "))

    sessao = input("Descrição da sessão: ")

    campanhas[escolha - 1]["sessoes"].append(sessao)

    print("Sessão adicionada com sucesso!")
    pausar()


def alterar_sessao():

    print("\n=== ALTERAR SESSÃO ===")

    if not campanhas:
        print("Nenhuma campanha criada.")
        pausar()
        return

    for i, campanha in enumerate(campanhas, start=1):
        print(f"{i} - {campanha['nome']}")

    escolha_campanha = int(input("\nEscolha a campanha: "))

    campanha = campanhas[escolha_campanha - 1]

    if not campanha["sessoes"]:
        print("Nenhuma sessão cadastrada.")
        pausar()
        return

    print("\nSessões:")

    for i, sessao in enumerate(campanha["sessoes"], start=1):
        print(f"{i} - {sessao}")

    escolha_sessao = int(input("\nEscolha a sessão: "))

    nova_sessao = input("Nova descrição da sessão: ")

    campanha["sessoes"][escolha_sessao - 1] = nova_sessao

    print("Sessão alterada com sucesso!")
    pausar()


# =========================
# MENU JOGADOR
# =========================

def menu_jogador():

    while True:

        print("\n=== MENU DO JOGADOR ===")

        print("1 - Criar personagem")
        print("2 - Ver personagens")
        print("3 - Alterar personagem")
        print("4 - Adicionar item")
        print("0 - Voltar")

        escolha = input("\nEscolha: ")

        if escolha == "1":
            criar_personagem()

        elif escolha == "2":
            ver_personagens()

        elif escolha == "3":
            alterar_personagem()

        elif escolha == "4":
            adicionar_item()

        elif escolha == "0":
            break

        else:
            print("Opção inválida.")
            pausar()


# =========================
# MENU MESTRE
# =========================

def menu_mestre():

    while True:

        print("\n=== MENU DO MESTRE ===")

        print("1 - Criar NPC")
        print("2 - Ver NPCs")
        print("3 - Alterar NPC")
        print("4 - Criar campanha")
        print("5 - Ver campanhas")
        print("6 - Adicionar sessão")
        print("7 - Alterar sessão")
        print("0 - Voltar")

        escolha = input("\nEscolha: ")

        if escolha == "1":
            criar_npc()

        elif escolha == "2":
            ver_npcs()

        elif escolha == "3":
            alterar_npc()

        elif escolha == "4":
            criar_campanha()

        elif escolha == "5":
            ver_campanhas()

        elif escolha == "6":
            adicionar_sessao()

        elif escolha == "7":
            alterar_sessao()

        elif escolha == "0":
            break

        else:
            print("Opção inválida.")
            pausar()


# =========================
# MENU PRINCIPAL
# =========================

def menu_principal():

    while True:

        print("\n=== RPG SYSTEM ===")

        print("1 - Jogador")
        print("2 - Mestre")
        print("0 - Sair")

        escolha = input("\nEscolha: ")

        if escolha == "1":
            menu_jogador()

        elif escolha == "2":
            menu_mestre()

        elif escolha == "0":
            print("\nSaindo do sistema...")
            break

        else:
            print("Opção inválida.")
            pausar()


# =========================
# INICIAR SISTEMA
# =========================

menu_principal()