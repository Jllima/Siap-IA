from flask import jsonify, request
from app.chats.model import Chat
from app import chat_bp

class ChatRoutes:
  
  @chat_bp.route('/')
  def list():
    chats = Chat.query.all()
    result = [ {'id': chat.id, 'texto': chat.text} for chat in chats ]
    return jsonify(result)
