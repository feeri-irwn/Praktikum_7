from config import app, db
from flask import jsonify, request
from routes.Book_bp import book_bp
from routes.Category_bp import category_bp
from routes.User_bp import user_bp
from routes.Level_bp import level_bp
from controllers.UserController import check_password_hash
from models.UserModel import User

app.register_blueprint(book_bp)
app.register_blueprint(category_bp)
app.register_blueprint(user_bp)
app.register_blueprint(level_bp)



db.create_all()
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

@app.before_request
def before_request():
    excluded_routes = ['/api/login', '/api/register']
    if request.path in excluded_routes:
        return None
    
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({"message": "missing or invalid credentials"}), 401
    
    user = User.query.filter_by(username=auth.username).first()
    if not user or not check_password_hash(user.password, auth.password):
        return jsonify({"message":"Invalid username or password"}), 401
    
    request.current_user=user
