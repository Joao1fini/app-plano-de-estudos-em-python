import questionary
import os
import time
login1 = False
areas = ["1 - cybersegurança","2 - desenvolvedor","3 - redes"]
os.system("cls")
def conteudos(area):
    conteudo = questionary.select(
        "Qual o tipo de conteudo gostaria de ver? ",
        choices=[
            "1 - Artigos",
            "2 - Roadmaps",
            "3 - Videos"
        ]
    ).ask()
    if conteudo.startswith("1"):
        with open(f"conteudo/artigo/{area}", "r") as conteudo:
            os.system("cls")
            print(conteudo.read())
    elif conteudo.startswith("2"):
        with open(f"conteudo/roadmap/{area}", "r") as conteudo:
            os.system("cls")
            print(conteudo.read())
    elif conteudo.startswith("3"):
        with open(f"conteudo/videos/{area}", "r") as conteudo:
            os.system("cls")
            print(conteudo.read())
def conteudosdev():
    escolha = questionary.select(
                "gostaria de adicionar artigo, videos ou roadmap?",
                    choices=[
                        "1 - artigo",
                        "2 - roadmap",
                        "3 - video"]).ask()
    if escolha.startswith("1"):
        caminho= "conteudo/artigo"
    elif escolha.startswith("2"):
        caminho= "conteudo/roadmap"
    elif escolha.startswith("3"):
        caminho= "conteudo/videos"
    return caminho
def cadastro():
    while True:
        os.system("cls")
        nome=input("Digite seu nome de usuario: ")
        senha = input("Digite sua senha: ")
        senhan = input("Digite sua senha novamente : ")
        if senha == senhan:
            with open("usuario.txt","a") as dados:
                dados.write(f"{nome},{senha}\n")
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
def assunto(assunt):
    os.system("cls")
    for i in range(1,4):
        print("carregando"+"."*i)
        time.sleep(0.8)
        os.system("cls")
    area = questionary.select(
        "Escolha sua area de interesse ",
        choices=[
            f"{areas[0]}",
            f"{areas[1]}",
            f"{areas[2]}"
        ]
    ).ask()
    if area.startswith("1"):
        area = "cyber.txt"
    elif area.startswith("2"):
        area = "developer.txt"
    elif area.startswith("3"):
        area = "redes.txt"
    if assunt == True:
        conteudos(area)
    return area
usuario = questionary.select(
    "Você é um usuario ou colaborador?",
    choices=[
        "[1]USUARIO",
        "[2]COLABORADOR"
    ]
).ask()
if usuario.startswith("[1]"):
    lr = questionary.select(
        "Bme vindo a estudos.sh",
        choices=[
            "[1]login",
            "[2]Cadastrar"
        ]
    ).ask()
    if lr.startswith("[1]"):
        if login(0):
            login1 = True
    elif lr.startswith("[2]"):
        cadastro()
    else:
        print("valor invalido tente novamente ")
        os.system("cls")
if login1 == True:
    assunto(True)
if usuario.startswith("[2]"):
    escolha = questionary.select(
        "Bem-vindo a central de colaboradores\npara se tornar um colaborador um adm central deve te adicionar, deseja prosseguir para o login?",
            choices=[
            "sim",
            "não"]
        ).ask()
    if escolha.startswith("s"):
        if login(1):
            escolha = questionary.select(
                "Oque deseja? ",
                choices=[
                    "1 - ver conteudo",
                    "2 - adicionar conteudo",
                    "3 - editar conteudo"
                ]).ask()
            if escolha.startswith("1"):
                assunto(True)
            elif escolha.startswith("2"):
                caminho = conteudosdev()
                new_nome = questionary.text("Digite o nome do novo arquivo").ask().strip() + ".txt"
                novofile = os.path.join(caminho,new_nome)
                
                with open(novofile,"w") as f:
                    os.startfile(novofile)
                
            elif escolha.startswith("3"):
                caminho = conteudosdev()
                os.system("cls")
                area = assunto(False)
                caminho = os.path.join(caminho,area)
                os.startfile(caminho)
    else:
        exit()
    