secret_key = 'quatro&20'

# Configuração do banco de dados
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{usuario}:{senha}@{host}/{database}'.format(
    usuario='root',
    senha='cmb110205',
    host='localhost',
    database='collectionstep'
)


SQLALCHEMY_TRACK_MODIFICATIONS = False

