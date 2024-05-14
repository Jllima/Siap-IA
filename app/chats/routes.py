from flask import jsonify, request
from app.chats.model import Chat
from app import chat_bp
from app import db
from app.chats.schemas import chat_schema, chats_schema

class ChatRoutes:
  
  @chat_bp.route('/')
  def list():
    chats = Chat.query.all()
    # result = [ {'id': chat.id, 'texto': chat.text} for chat in chats ]
    # return jsonify(result)
    return chats_schema.dump(chats)
  
  @chat_bp.route('/', methods=['POST'])
  def create():
    data = request.get_json()
    # new_chat = Chat(name_user=data['name_user'], text=data['text'])

    errors = chat_schema.validate(data, session=db.session)
    if errors:
      return {"errors": errors}, 400
    
    new_chat = chat_schema.load(data, session=db.session)
    db.session.add(new_chat)
    db.session.commit()
    #return jsonify({'message': 'Criado com sucesso!', 'chat': {'name': new_chat.name_user, 'text': new_chat.text}})
    return chat_schema.dump(new_chat), 201
    
