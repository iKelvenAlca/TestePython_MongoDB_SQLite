# Integração Python com SQLite e MongoDB
Este projeto demonstra a integração de um banco de dados SQLite e MongoDB com SQLAlchemy e Pymongo.

## Estrutura do Projeto
SQLite.py: Script para manipular o banco de dados SQLite.<br>
MongoDB.py: Script para conectar ao MongoDB Atlas e manipular o banco de dados NoSQL.<br>
requirements.txt: Dependências do projeto.<br>

## Pré-requisitos
Python 3.x <br>
Bibliotecas: sqlalchemy, pymongo <br>

Instalação<br>
Clone o repositório e instale as dependências:
```
git clone https://github.com/iKelvenAlca/TestePython_MongoDB_SQLite.git <br>
cd TestePython_MongoDB_SQLite
```
## Uso
### Banco de Dados Relacional com SQLite
Execute SQLite.py para criar e manipular o banco de dados:
SQLite.py


### Banco de Dados NoSQL com MongoDB
Configure a URI no MongoDB.py:
> client = pymongo.MongoClient("mongodb+srv://<username>:<password>@<cluster-url>/test?retryWrites=true&w=majority&appName=ClusterTesteIntegracao")

Execute MongoDB.py para inserir e consultar dados:

Consultas de Exemplo
Recuperar todos os clientes:
```
clientes = collection.find()
for cliente in clientes:
    print(cliente)
```    
Recuperar cliente por nome:
```
cliente_joao = collection.find_one({"nome": "João Silva"})
print(cliente_joao)
