
import psycopg2 as conector

# Abertura de conexão
conexao = conector.connect("URL PostgreSQL")

# Aquisição de um cursor
cursor = conexao.cursor()

# Execução comandos: SELECT..CREATE...
cursor.execute("CREATE")
cursor.fetchall()


class Register:
  def __init__(self, name, password):
    self.name = name
    self.password = password

class Login:
  def __init__(self, name, password):
    self.name = name
    self.password = password
    

managers = []  
 
  
def main(): 

  print("----CADASTRO-----")
  nameCad = input("Nome do Gerente> ")
  passwordCad = input("Defina sua senha> ")

  newManager = Register(nameCad, passwordCad)
  managers.append(newManager)


  print("----LOGIN---")
  nameLogin = input("Digite seu Login> ")
  passwordLogin = input("Digite sua senha> ")

  tryLogin = Login(nameLogin,passwordLogin)

  loggedIn = False  
  for g in managers:
      if tryLogin.name == g.name and tryLogin.password == g.password:
       loggedIn = True
       break

  if loggedIn:
     print("VOCE LOGOU COM SUCESSO")

     input("Digite 1 para criar checklists, Digite 2 para conferir")
  else:
    print("ESSE GERENTE NAO EXISTE")
 
  

if __name__ == "__main__":
  main()



