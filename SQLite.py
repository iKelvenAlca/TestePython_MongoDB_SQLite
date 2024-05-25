from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.types import LargeBinary

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    endereco = Column(String(50), nullable=False)
    contas = relationship("Conta", back_populates="cliente")

class Conta(Base):
    __tablename__ = 'conta'
    id = Column(LargeBinary, primary_key=True)
    tipo = Column(String, nullable=False)
    agencia = Column(String, nullable=False)
    num = Column(Integer, nullable=False)
    id_cliente = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    saldo = Column(Numeric, nullable=False)
    cliente = relationship("Cliente", back_populates="contas")

# Criar um motor de banco de dados
engine = create_engine('sqlite:///bancoSQLite.db')
Base.metadata.create_all(engine)


# Adicionando Dados


# Criar uma sessão
Session = sessionmaker(bind=engine)
session = Session()

# Adicionar clientes
cliente1 = Cliente(nome='João Silva', cpf='12345678901', endereco='Rua A, 123')
cliente2 = Cliente(nome='Maria Souza', cpf='09876543210', endereco='Rua B, 456')

session.add(cliente1)
session.add(cliente2)
session.commit()

# Adicionar contas
conta1 = Conta(id=b'1', tipo='Corrente', agencia='001', num=12345, id_cliente=cliente1.id, saldo=1500.50)
conta2 = Conta(id=b'2', tipo='Poupança', agencia='002', num=67890, id_cliente=cliente2.id, saldo=3000.00)

session.add(conta1)
session.add(conta2)
session.commit()


# Consultando Dados


# Recuperar todos os clientes
clientes = session.query(Cliente).all()
for cliente in clientes:
    print(f"ID: {cliente.id}, Nome: {cliente.nome}, CPF: {cliente.cpf}, Endereço: {cliente.endereco}")

# Recuperar todas as contas
contas = session.query(Conta).all()
for conta in contas:
    print(f"ID: {conta.id}, Tipo: {conta.tipo}, Agência: {conta.agencia}, Número: {conta.num}, Saldo: {conta.saldo}")

# Recuperar contas de um cliente específico
cliente = session.query(Cliente).filter_by(nome='João Silva').first()
for conta in cliente.contas:
    print(f"Conta ID: {conta.id}, Tipo: {conta.tipo}, Saldo: {conta.saldo}")