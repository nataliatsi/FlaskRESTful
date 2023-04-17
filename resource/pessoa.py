from flask_restful import Resource, reqparse, marshal_with, marshal
from model.pessoa import Pessoa, pessoa_fields
from model.mensagem import Mensagem, mensagem_fields
from database import db

parser = reqparse.RequestParser()
parser.add_argument('nome', type=str, help='Problema na conversão do nome!')
parser.add_argument('email', type=str, help='Problema na conversão do e-mail!')

class PessoaResource(Resource):
  # GET --->
  @marshal_with(pessoa_fields)
  def get(self):
    pessoas = Pessoa.query.all()
    return (pessoas, 200)

  # POST --->
  @marshal_with(pessoa_fields)  
  def post(self):
    args = parser.parse_args()
    nome = args['nome']
    email = args['email']
    
    pessoa = Pessoa(nome, email)

    db.session.add(pessoa)
    db.session.commit()

    return pessoa, 201

  # PUT --->
  def put(self, pessoa_id):

    args = parser.parse_args()
    nome = args['nome']
    email = args['email'] 

    pessoa = Pessoa.query.get(pessoa_id)

    if pessoa is not None:
      pessoa.nome = nome
      pessoa.email = email

      db.session.add(pessoa)
      db.session.commit(pessoa)
      return marshal(pessoa, pessoa_fields), 201
    else:
      mensagem = Mensagem('Pessoa não encontrada.', 1)
      return marshal(mensagem, mensagem_fields), 404 
    return pessoa