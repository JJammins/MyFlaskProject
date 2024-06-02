from datetime import datetime

from apps.app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String, unique=True, index=True)
    email = db.Column(db.String, unique=True, index=True)
    password_hash = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)

    # 비밀번호 프로퍼티와 관련 메서드
    @property
    def password(self):
        raise AttributeError("읽어들일 수 없음")
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 비밀번호 검증 메서드
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    # 중복 검사 메서드
    def is_duplicate_email(self):
        return User.query.filter_by(email=self.email).first() is not None
    
    def is_duplicate_nickname(self):
        return User.query.filter_by(nickname=self.nickname).first() is not None

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, index=True)
    content = db.Column(db.String, index=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

