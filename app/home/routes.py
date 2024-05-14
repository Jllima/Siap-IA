from app import home_bp

@home_bp.route("/")
def hello():
  return "Olá Mundo 2"