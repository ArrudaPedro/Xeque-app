import psycopg2

# Conecta em um Banco de Dados existente.
connect = psycopg2.connect(
   dbname="XXXX",
   user="XXXXX",
   password="XXXXXX",
   host="XXXX",
   ) 

cursor = connect.cursor() # Cria um cursor para controlar as operações do Banco de Dados.

# Define como o User deve ser.
class User: 
  def __init__(self, name, login, password, role):
    self.name = name
    self.login = login
    self.password = password
    self.role = role

# Funçao para criar o cadastro. 
def Register(): 

  print("---CADASTRO INICIAL---")
  name = input("Digite aqui o nome a ser usado: ")
  login = input("Digite aqui o login desejado: ")
  password = input("Digite aqui a senha desejada: ")
  role = input("Digite aqui a função desejada")

  query = "INSERT INTO managers (name, login, password, role) VALUES (%s,%s,%s,%s)"
  newUser = (name, login, password, role)

  try:
      cursor.execute(query,newUser) # Preenche os VALUES do query com os dados do newUser
      connect.commit() # Grava as informações no Banco de Dados
      print("Registrado com sucesso!")
  except Exception as msgError: # Se algo no try der errado:
     connect.rollback() # Evita que o sistema trave 
     print(f"Erro ao registrar. Erro: {msgError}")
     


def Login():
  print("----LOGIN---")
  nameLogin = input("Digite seu Login> ")
  passwordLogin = input("Digite sua senha> ")

  # Consulta o banco
  query = "SELECT name, login, password, role FROM managers WHERE login = %s AND password = %s"

  try:
    
    cursor.execute(query,(nameLogin,passwordLogin)) # Preenche os VALUES do query com os dados do login e password

    # Pega um resultado (1 Linha ou none)
    user_data = cursor.fetchone()
    
    if user_data:
       loggedUser = User(user_data[0], user_data[1], user_data[2], user_data[3])
       print(f"Bem vinda(a), {loggedUser.name}! Nivel de acesso {loggedUser.role}")
       return loggedUser
    else:
       return None

  except Exception as msgError:
      connect.rollback() # Evita que o sistema trave 
      print(f"Erro ao logar. Erro{msgError}")
     
def main(): 
  # Roda a função register
  Register()

  # Roda a função login
  Login()
    
  # Fecha as conexões com o Banco de Dados.
  cursor.close()
  connect.close()
  print("Conexão com Banco de Dados Encerrada")



if __name__ == "__main__":
    main()


