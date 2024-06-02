from pathlib import Path
from apps.config import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
csrf = CSRFProtect()

# LoginManager 설정
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message = ""

def create_app(config_key) :
    app = Flask(__name__)
    # config_key에 매치하는 환경의 config 클래스를 읽어들인다
    app.config.from_object(config[config_key])
    app.config.from_mapping(
        SECRET_KEY="sksms12qkqh34dpdy",
        SQLALCHEMY_DATABASE_URI=
        f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        # SQL을 콘솔 로그에 출력하는 설정
        SQLALCHEMY_ECHO=True,
    
        WTF_CSRF_SECRET_KEY="AuwyszU5sugKN7KZs6f" # 폼의 확장 기능 관련 시크릿키
    )
    
    db.init_app(app)
    Migrate(app, db)
    csrf.init_app(app)

    # 로그인 매니저 초기화
    login_manager.init_app(app)
    
    # 인증 블루프린트 등록
    from apps.auth import views as auth_views
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    from apps.blog import views as crud_views
    app.register_blueprint(crud_views.blog, url_prefix="/blog")
    
    return app