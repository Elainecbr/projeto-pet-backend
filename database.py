# backend/database.py
"""
Modelos de dados (ORM) para o Pet Web usando Flask-SQLAlchemy.

Cada classe representa uma tabela no banco SQLite e contém métodos
utilitários (`to_dict`) para serializar os objetos para JSON ao serem
retornados pelas rotas da API.

Observe que `db = SQLAlchemy()` é criado aqui sem vínculo com o app.
O vínculo é feito em `app.create_app()` com `db.init_app(app)`. Isso
permite usar os modelos em scripts de seed ou testes sem criar uma
instância global do Flask imediatamente.
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Inicializa o objeto SQLAlchemy, mas não o vincula a um aplicativo Flask ainda.
# O vínculo é feito pela fábrica de aplicação em `app.py` para permitir testes
# e execução de scripts auxiliares (por exemplo, `seed_db.py`).
db = SQLAlchemy()

# Modelo para o Usuário - Representa a tabela 'user' no banco de dados
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Chave primária, auto-incrementável
    nome_completo = db.Column(db.String(100), nullable=False) # Nome completo do usuário, obrigatório
    email = db.Column(db.String(100), unique=True, nullable=False) # Email único e obrigatório
    telefone = db.Column(db.String(20), nullable=True) # Telefone, opcional
    
    # Relacionamento One-to-Many: Um usuário pode ter vários cachorros.
    # 'Cachorro' é o nome da classe do modelo relacionado.
    # 'backref='owner'' cria um atributo 'owner' nos objetos Cachorro para acessar o usuário proprietário.
    # 'lazy=True' significa que os cachorros serão carregados apenas quando acessados.
    cachorros = db.relationship('Cachorro', backref='owner', lazy=True, cascade='all, delete-orphan')
    
    data_cadastro = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # Data de cadastro, preenchida automaticamente em UTC

    # Método para converter o objeto User em um dicionário, útil para JSON.
    def to_dict(self):
        return {
            'id': self.id,
            'nome_completo': self.nome_completo,
            'email': self.email,
            'telefone': self.telefone,
            'data_cadastro': self.data_cadastro.isoformat() + 'Z' # Formato ISO 8601 para Web, com 'Z' para UTC
        }

# Modelo para a Raça do Cachorro - Representa a tabela 'raca'
class Raca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False) # Nome da raça, único e obrigatório
    porte = db.Column(db.String(50), nullable=True) # Ex: Pequeno, Médio, Grande
    grupo = db.Column(db.String(100), nullable=True) # Ex: Cães de Companhia, Farejadores
    imagem = db.Column(db.String(100), nullable=True) # Nome do arquivo da imagem da raça
    cuidados = db.Column(db.Text, nullable=True) # Descrição dos cuidados específicos
    comportamento = db.Column(db.Text, nullable=True) # Descrição do comportamento típico
    racao = db.Column(db.Text, nullable=True) # Recomendação de ração
    
    # Relacionamento One-to-Many: Uma raça pode ter vários cachorros.
    cachorros = db.relationship('Cachorro', backref='breed', lazy=True)

    # Método para converter o objeto Raca em um dicionário.
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'porte': self.porte,
            'grupo': self.grupo,
            'imagem': self.imagem,
            'cuidados': self.cuidados,
            'comportamento': self.comportamento,
            'racao': self.racao
        }

# Modelo para o Cachorro - Representa a tabela 'cachorro'
class Cachorro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Constraint para evitar que o mesmo usuário registre dois cães com o mesmo nome
    __table_args__ = (db.UniqueConstraint('user_id','nome_pet', name='uix_user_pet'),)
    nome_pet = db.Column(db.String(100), nullable=False) # Nome do pet, obrigatório
    idade = db.Column(db.Integer, nullable=True) # Idade em anos, opcional
    peso = db.Column(db.Float, nullable=True) # Peso em kg, opcional
    info_extra = db.Column(db.Text, nullable=True) # Informações adicionais, opcional
    data_registro = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # Data de registro, preenchida automaticamente em UTC

    # Chaves estrangeiras para relacionar com User e Raca (relacionamento Many-to-One)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # ID do usuário proprietário
    raca_id = db.Column(db.Integer, db.ForeignKey('raca.id'), nullable=False) # ID da raça do cachorro

    # Método para converter o objeto Cachorro em um dicionário.
    # 'include_owner' e 'include_breed' permitem incluir os dados completos do owner/breed no dicionário, se necessário.
    def to_dict(self, include_owner=False, include_breed=False):
        data = {
            'id': self.id,
            'nome_pet': self.nome_pet,
            'idade': self.idade,
            'peso': self.peso,
            'info_extra': self.info_extra,
            'data_registro': self.data_registro.isoformat() + 'Z',
            'user_id': self.user_id,
            'raca_id': self.raca_id
        }
        # Se solicitado, inclui os dados serializados do owner (User)
        if include_owner and self.owner:
            data['owner'] = self.owner.to_dict()
        # Se solicitado, inclui os dados serializados da raça (Raca)
        if include_breed and self.breed:
            data['breed'] = self.breed.to_dict()
        return data
