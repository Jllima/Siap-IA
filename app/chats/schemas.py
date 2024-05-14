from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .model import Chat

class ChatSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = Chat
    # Para carregar dados em um modelo existente
    load_instance = True
  
  # preco = fields.Decimal(as_string=True) # Formata o preço como string

chat_schema = ChatSchema()
chats_schema = ChatSchema(many=True)