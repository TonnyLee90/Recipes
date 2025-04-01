from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime

# To reload a user from the session.
# so Flask-Login knows who is logged in 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# UserMixin is a class and used to implemented for user authentication    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
    # create a connection to the table 2
    recipes = db.relationship('Recipe', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}')"
    
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Recipe('{self.title}', '{self.created}')"