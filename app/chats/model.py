from app import db

class Chat(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name_user = db.Column(db.String(100))
  text = db.Column(db.String(100))

  def __repr__(self):
        return f'<Chat {self.name_user}>'