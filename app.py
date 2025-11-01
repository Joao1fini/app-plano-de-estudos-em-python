import questionary
import os
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
def login():
    nome = input("Digite seu nome de usuario: ")
    senha = input("Digite sua senha: ")
    with open("usuario.txt","r+") as dados:
        for linha in dados:
            usuario, senha_salva = linha.strip().split(",")
            if nome==usuario and senha == senha_salva:
                print(f"Bem vindo de volta {nome}")
                return True
    print("Erro nome/senha incorretos")    
    return False

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
        login()
    elif lr.startswith("[2]"):
        cadastro()
    else:
        print("valor invalido tente novamente ")
        os.system("cls")
if login == True:
    area = questionary.select(
        "Escolha sua area de interesse ",
        choices=[
            "1 - Cybersecurity",
            "2 - developer",
            "3 - Data Scienc"
        ]
    ).ask()
    