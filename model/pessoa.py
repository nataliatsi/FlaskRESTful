from flask_restful import fields
from database import db

pessoa_fields = {
  'id': fields.Integer,
  'nome': fields.String,
  'email': fields.String
}

class Pessoa(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, unique=True, nullable=False)
  email = db.Column(db.String)

  def __init__(self, name, email):
    self.name = name
    self.email = email
    
  def __repr__(self):
      return f'<Pessoa {self.name}, {self.email}>'
