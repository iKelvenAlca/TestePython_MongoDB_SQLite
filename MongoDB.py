import pymongo

# Conectar ao MongoDB Atlas
client = pymongo.MongoClient("mongodb+srv://kelvenalca:MF3gKv97fTIfIiYV@clustertesteintegracao.rfsbeyo.mongodb.net/?retryWrites=true&w=majority&appName=ClusterTesteIntegracao")
db = client["bancoMongoDB"]
collection = db["bank"]

# Dados de exemplo
clientes = [
    {
        "nome": "João Silva",
        "cpf": "12345678901",
        "endereco": "Rua A, 123",
        "contas": [
            {"tipo": "Corrente", "agencia": "001", "num": 12345, "saldo": 1500.50},
            {"tipo": "Poupança", "agencia": "001", "num": 54321, "saldo": 2000.00}
        ]
    },
    {
        "nome": "Maria Souza",
        "cpf": "09876543210",
        "endereco": "Rua B, 456",
        "contas": [
            {"tipo": "Poupança", "agencia": "002", "num": 67890, "saldo": 3000.00}
        ]
    }
]

# Inserir os documentos na coleção
collection.insert_many(clientes)

# Recuperar todos os clientes
clientes = collection.find()
for cliente in clientes:
    print(cliente)

# Recuperar cliente por nome
cliente_joao = collection.find_one({"nome": "João Silva"})
print(cliente_joao)

# Recuperar clientes com saldo acima de um valor específico
clientes_com_saldo_alto = collection.find({"contas.saldo": {"$gt": 2000}})
for cliente in clientes_com_saldo_alto:
    print(cliente)

# Recuperar contas de um cliente específico
cliente = collection.find_one({"nome": "Maria Souza"})
for conta in cliente["contas"]:
    print(conta)
