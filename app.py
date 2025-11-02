import questionary
import os
import time
login1 = False
os.system("cls")
for d in ["conteudo", "conteudo/artigos", "conteudo/roadmaps", "conteudo/videos"]:
    os.makedirs(d, exist_ok=True)
for path in ("usuario.txt", "colaborador.txt"):
    if not os.path.exists(path):
        open(path, "a").close()
def conteudos():
    escolha = questionary.select(
        "qual o tipo de conteudo? ",
        choices=[
            "artigos",
            "roadmaps",
            "videos",
            "sair"
        ]
    ).ask()
    if escolha.startswith("a"):return "conteudo/artigos"
    elif escolha.startswith("r"):return "conteudo/roadmaps"
    elif escolha.startswith("v"):return "conteudo/videos"
    elif escolha.startswith("s"): return False
def cadastro():
    while True:
        os.system("cls")
        nome=input("Digite seu nome de usuario: ")
        senha = input("Digite sua senha: ")
        senhan = input("Digite sua senha novamente : ")
        if senha == senhan:
            with open("usuario.txt", "r") as dados:
                for linha in dados:
                    usuario_s, senha_s = linha.strip().split(",")
                    if nome == usuario_s:
                        escolha = questionary.select(
                            "Cadastro ja existente ",
                            choices=[
                                "cadastrar novamente",
                                "ir para Login",
                                "Sair"
                            ]
                        ).ask()
                        if escolha.startswith("c"):
                            continue
                        elif escolha.startswith("i"):
                            if login(0):
                                return True
                        else:
                            break
                            exit()
            with open("usuario.txt","a") as dados:
                dados.write(f"{nome},{senha}\n")
                os.system("cls")
                print("cadastro efetuado")
                time.sleep(1.5)
                os.system("cls")

                return True
                break
        else:
            print("senhas não semelhantes, tente novamente: ")
            continue
def login(tipo):
    nome = input("Digite seu nome de usuario: ")
    senha = input("Digite sua senha: ")
    if tipo==0:
        with open("usuario.txt","r") as dados: 
            for linha in dados:
                usuario, senha_salva = linha.strip().split(",")
                if nome==usuario and senha == senha_salva:
                    os.system("cls")
                    print(f"Bem vindo de volta {nome}")
                    return True
    elif tipo==1:
        with open("colaborador.txt","r") as dados: 
            for linha in dados:
                usuario, senha_salva = linha.strip().split(",")
                if nome==usuario and senha == senha_salva:
                    os.system("cls")
                    print(f"Bem vindo {nome}")
                    return True
    print("Erro nome/senha incorretos")    
    return False
def assunto(caminho):
    os.system("cls")
    for i in range(1,4):
        print("carregando"+"."*i)
        time.sleep(0.4)
        os.system("cls")
    try:
        caminho2 = sorted(f for f in os.listdir(caminho))
        escolha = questionary.select(
            "Escolha sua area de interesse ",
            choices=
                caminho2
        ).ask()
        full_path = os.path.join(caminho, escolha)
        os.startfile(os.path.abspath(full_path))
    except ValueError:
        os.makedirs(caminho, exist_ok=True)
        print("pasta não existe")
while True:
    usuario = questionary.select(
        "Você é um usuario ou colaborador?",
        choices=[
            "[1]USUARIO",
            "[2]COLABORADOR",
            "[3]SAIR"
        ]
    ).ask()
    if usuario.startswith("[1]"):
        while True:
            lr = questionary.select(
                "Bem vindo a estudos.sh",
                choices=[
                    "[1]login",
                    "[2]Cadastrar",
                    "[3]SAIR"
                ]
            ).ask()
            if lr.startswith("[1]"):
                if login(0):
                    login1 = True
            elif lr.startswith("[2]"):
                if cadastro():
                        login1 = True
            elif lr.startswith("[3]"):
                break
                exit()
            else:
                print("valor invalido tente novamente ")
                os.system("cls")
            if login1 == True:
                caminho = conteudos()
                if not caminho:
                    os.system("cls")
                    continue
                assunto(caminho)
            else:
                continue
    if usuario.startswith("[2]"):
        while True:
            escolha = questionary.select(
                "Bem-vindo a central de colaboradores\npara se tornar um colaborador um adm central deve te adicionar, deseja prosseguir para o login?",
                    choices=[
                    "sim",
                    "não"]
                ).ask()
            if escolha.startswith("s"):
                if login(1):
                    while True:
                        escolha = questionary.select(
                            "Oque deseja? ",
                            choices=[
                                "1 - ver conteudo",
                                "2 - adicionar conteudo",
                                "3 - editar conteudo",
                                "4 - voltar"
                            ]).ask()
                        if escolha.startswith("1"):
                            caminho = conteudos()
                            if not caminho:
                                continue
                            assunto(caminho)
                        elif escolha.startswith("2"):
                            caminho = conteudos()
                            new_nome = questionary.text("Digite o nome do novo arquivo").ask().strip() + ".txt"
                            novofile = os.path.join(caminho,new_nome)

                            with open(novofile,"w") as f:
                                os.startfile(novofile)
                        elif escolha.startswith("3"):
                            caminho = conteudos()
                            if not caminho:
                                continue
                            assunto(caminho)
                            continue
                        else:
                            break
            else:
                os.system("cls")
                break
    elif usuario.startswith("[3]"):
        break
    