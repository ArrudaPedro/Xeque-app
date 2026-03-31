import os
import sys

import psycopg2
from dotenv import load_dotenv

load_dotenv()


# Conecta em um Banco de Dados existente.
try:
    connect = psycopg2.connect(
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT")
    ) 
    connect.set_client_encoding('utf-8')  # Evita erro de Unicode
    cursor = connect.cursor()  # Cria um cursor para controlar as operações do Banco de Dados.
except Exception as e:
    print(f"Erro ao conectar no Banco de dados. Erro: {e}")
    print(f"Erro real detectado: {repr(e)}")
    sys.exit()  # Encerra o programa caso de Erro.


class User:
    """Define como o User deve ser."""

    def __init__(self, name, login, password, role):
        self.name = name
        self.login = login
        self.password = password
        self.role = role


def user_register(): 
    """ Funçao para criar o cadastro."""

    print("---CADASTRO INICIAL---")
    name = input("Digite aqui o nome a ser usado: ")
    login = input("Digite aqui o login desejado: ")
    password = input("Digite aqui a senha desejada: ")
    role = input("Digite aqui a função desejada: ")

    query = "INSERT INTO managers (name, login, password, role) VALUES (%s, %s, %s, %s)"
    new_user = (name, login, password, role)

    try:
        cursor.execute(query, new_user)  # Preenche os VALUES do query com os dados do newUser
        connect.commit()  # Grava as informações no Banco de Dados
        print("Registrado com sucesso!")
    except Exception as e:  # Se algo no try der errado:
        connect.rollback()  # Evita que o sistema trave 
        print(f"Erro ao registrar. {e}")


def user_login():
    """Consulta e autenticação no banco."""
    print("----LOGIN---")
    name_login = input("Digite seu Login> ")
    password_login = input("Digite sua senha> ")

    # Consulta o banco
    query = "SELECT name, login, password, role FROM managers WHERE login = %s AND password = %s"
    
    try:

        cursor.execute(query,(name_login, password_login))  # Preenche os VALUES do query com os dados do login e password

        # Pega um resultado (1 Linha ou none)
        user_data = cursor.fetchone()
    
        if user_data:
            logged_user = User(user_data[0], user_data[1], user_data[2], user_data[3])
            print(f"Bem vindo(a), {logged_user.name}! Nivel de acesso: {logged_user.role}")
            return logged_user, True
        else:
            print("Esse login não existe!")
            return None, False

    except Exception as e:
        connect.rollback()  # Evita que o sistema trave 
        print(f"Erro ao logar. {e}")

def create_checklist():
    """Cria e inseri um novo checklist no banco de dados"""

    print("Criando Checklist")
    title = input("O que tem que ser feito?... ")
    description = input("Explique detalhadamente o checklist ")
    sector = input("Para qual setor é esse checklist? ")

    query = "INSERT INTO checklist (title, description, sector) VALUES (%s, %s, %s)"
    new_checklist = (title, description, sector)
    try:
        cursor.execute(query, new_checklist)
        connect.commit()  
        print("Checklist criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar checklist. {e}")


def main():
    user_logged = False
    while not user_logged:
        try:
            choice = int(input("O que deseja fazer? 1- Para logar, 2- Para Registrar: "))
            if choice == 1:
                # Roda a função login
                _, user_logged = user_login()
            elif choice == 2:
                user_register()
                _, user_logged = user_login() 
            elif choice == 0:
                break
            else:
                print("Opção invalida")
        except ValueError:
            print("Digite apenas 1 ou 2.")

    if user_logged:
        while True:
            print("O que deseja fazer?")
            try:
                edit_checklist = int(input("1- Criar checklists.\n 2- Conferir checklists.\n 0- Sair\n"))

                if edit_checklist == 1:
                     create_checklist()
                elif edit_checklist == 2:
                    query = "SELECT title FROM checklist"
                    cursor.execute(query)

                    results = cursor.fetchall()
                    if results:
                        print(results[0])
                    else:
                        print("Nenhum checklist criado ainda.")

                elif edit_checklist == 0:
                    break
                else:
                    print("Opção invalida")
            except ValueError:
                print("Erro: Por favor, digite apenas números.")
    else:
        # Fecha as conexões com o Banco de Dados.
        cursor.close()
        connect.close()
        print("Conexão com Banco de Dados Encerrada!")


if __name__ == "__main__":
    main() 