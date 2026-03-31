# Xeque-app

O **Xeque-app** é uma solução para gestão de checklists empresariais. Projetado para substituir processos manuais e garantir a rastreabilidade, o sistema permite a criação de checklists dinâmicos com fluxos de preenchimento e conferência auditáveis.

# Funcionalidades 
- **Gestão de Checklists:** Criação e personalização de formulários de verificação.

- **Fluxo de Aprovação:**  Identificação clara e registrada de quem preencheu e quem conferiu.

- **Interface Multiplataforma:** Desenvolvido em Flet para rodar em Desktop e Web.

# Stack Utilizada

- **Linguagens:** Python 
- **Interface Gráfica:** Flet
- **Banco de Dados:** PostgreSQL

# Como rodar o projeto (Em desenvolvimento)

 1. **Clone o Repositorio** 
 ```bash
  git clone https://github.com/seu-usuario/xeque-app.git
  cd Xeque-app
  ```
 2. **Configure o Ambiente Virtual**
 ```bash
  python -m venv .venv
  # No Windows:
  .venv\Scripts\activate
  # No Linux/Mac:
  source .venv/bin/activate
  ```
 3. **Instale as dependências**
```bash
  pip install -r requirements.txt
  ```
4. **Configuração de Ambiente**
   Crie um arquivo `.env` na raiz do projeto (utilize o `.env.example` como base) com as seguintes chaves:
```env
   DB_NAME=nome_do_banco
   DB_USER=seu_usuario
   DB_PASS=sua_senha
   DB_HOST=localhost
   DB_PORT=5432
```

## Banco de Dados 🗄️
O projeto utiliza **PostgreSQL** para persistência de dados. 

### Estrutura (Schema)
A definição das tabelas está no arquivo `schema.sql`. Para inicializar o banco, execute o comando abaixo no terminal do PostgreSQL (ou use uma ferramenta como o DBeaver/PGAdmin):

```bash
psql -U seu_usuario -d nome_do_banco -f schema.sql
```