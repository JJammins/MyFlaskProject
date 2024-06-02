from flask import Blueprint, render_template, flash, url_for, redirect, request
from apps.app import db
from apps.auth.forms import SignUpForm, LoginForm, EditUserForm
from apps.blog.models import User
from flask_login import login_user, logout_user

auth = Blueprint(
    "auth",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm() # 로그인 폼 초기화
    user = None  # user 변수 초기화

    # 폼 데이터 검증 및 사용자 인증
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for("blog.post"))
        else:
            flash("이메일 또는 비밀번호가 일치하지 않습니다.")
    return render_template("auth/login.html", form=form, title="로그인")

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(
            nickname=form.nickname.data,
            email=form.email.data,
            password=form.password.data
        )

        if user.is_duplicate_email():
            flash("이 이메일은 이미 등록되어 있습니다.")
            return redirect(url_for("auth.signup"))
        if user.is_duplicate_nickname():
            flash("이 닉네임은 이미 등록되어 있습니다.")
            return redirect(url_for("auth.signup"))

        db.session.add(user)
        db.session.commit()
        login_user(user)
        next_ = request.args.get("next")
        if next_ is None or not next_.startswith("/"):
            next_ = url_for("blog.post")
        return redirect(next_)
    return render_template("auth/signup.html", form=form, title="회원가입")

@auth.route("/users/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    form = EditUserForm()
    user = User.query.filter_by(id=user_id).first()
    if form.validate_on_submit():
        user.nickname = form.nickname.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("blog.post"))
    return render_template("auth/edit_user.html", user=user, form=form, title="회원정보 수정")

@auth.route("/users/<user_id>/delete", methods=["POST"])
def delete_user(user_id):
    user=User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("blog.post"))

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("blog.post"))
