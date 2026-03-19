# import psycopg2

class User: # Define como o User deve ser
  def __init__(self, name, login, password, role):
    self.name = name
    self.login = login
    self.password = password
    self.role = role

managers = []  # Lista que funciona temporariamente como DB
 
def Register(): # Funçao para criar o cadastro
  print("---CADASTRO INICIAL---")
  name = input("Digite aqui seu nome")
  login = input("Digite aqui seu login")
  password = input("Digite aqui seu pass")
  role = input("Digite aqui sua função")

   
  newUser = User(name,login,password,role) # Cria um objeto no molde do da CLASS USER
  managers.append(newUser) # Guarda o objeto criado na lista que serve como DB

def Login():
  print("----LOGIN---")
  nameLogin = input("Digite seu Login> ")
  passwordLogin = input("Digite sua senha> ")
  return nameLogin, passwordLogin # Esse Return serve para a informação de login não ser perdida


def UserLogin(loginAttempt,password_attempt):
  
  # Procura na lista para achar se o que foi digitado está certo
  for user in managers:
        if user.login == loginAttempt and user.password == password_attempt:
            return user  # Se existe na lista, retorna os valores para o UserLogged() na função main().
  return None 


  
def main(): 
  Register()


  login, password = Login() # Aqui você recebe as informações do return da função LOGIN() e guarda nas variaveis locais: login e password

  # Aqui envia o login e password para a função UserLogin() para conferir e retornar.
  UserLogged = UserLogin(login,password)

  if UserLogged: 
     print("Voce logou") # Caso o valor retornado exista
  else:
    print("\n❌ Usuário ou senha incorretos.") # Caso o valor retornado não exista


if __name__ == "__main__":
    main()



