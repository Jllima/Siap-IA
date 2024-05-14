from flask import jsonify, request
from app.chats.model import Chat
from app import chat_bp
from app import db

class ChatRoutes:
  
  @chat_bp.route('/')
  def list():
    chats = Chat.query.all()
    result = [ {'id': chat.id, 'texto': chat.text} for chat in chats ]
    return jsonify(result)
  
  @chat_bp.route('/', methods=['POST'])
  def create():
    data = request.get_json()
    new_chat = Chat(name_user=data['name_user'], text=data['text'])
    db.session.add(new_chat)
    db.session.commit()
    return jsonify({'message': 'Criado com sucesso!', 'chat': {'name': new_chat.name_user, 'text': new_chat.text}})
    
