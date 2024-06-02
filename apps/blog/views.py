from flask import Blueprint, render_template, redirect, url_for, request
from apps.blog.forms import PostForm
from apps.app import db
from apps.blog.models import Post
from flask_login import login_required

blog = Blueprint(
    "blog",
    __name__,
    template_folder="templates",
    static_folder="static"
)

# 페이징 기능 넣기 전
# @blog.route("/post")
# def post():
#     posts = Post.query.all()
#     page = request.args.get('page', type=int, default=1)
#     posts = posts.paginate(page=page, per_page=2)
#     for post in posts :
#         post.content = post.content.replace('\n', '<br>')

@blog.route("/post")
def post():
    page = request.args.get('page', type=int, default=1)

    # 게시물을 가져오는 쿼리 
    posts_query = Post.query.order_by(Post.created_at.desc())

    # 게시물을 페이징하여 가져오기
    posts_paginated = posts_query.paginate(page=page, per_page=9)

    return render_template("blog/post.html", posts=posts_paginated)

@blog.route('/post/detail/<post_id>')
def detail(post_id):
    post = Post.query.get(post_id)
    post.content = post.content.replace('\n', '<br>')
    return render_template('blog/detail_post.html', post=post)

@blog.route("/post/new", methods=["GET", "POST"])
@login_required
def create_post():
    form = PostForm()

    # 폼 유효성 검사 및 데이터 처리
    if form.validate_on_submit():
        post = Post(
            title = form.title.data,
            content = form.content.data
        )

        db.session.add(post)
        db.session.commit()

        return redirect(url_for("blog.post"))
    return render_template("blog/create_post.html", form=form, title="게시물 작성")

@blog.route("/post/edit/<post_id>", methods=["GET", "POST"])
@login_required
def edit_post(post_id):
    form = PostForm()

    # 기존 게시물 조회
    post = Post.query.filter_by(id=post_id).first()

    # 폼 유효성 검사 및 데이터 처리
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.updated_at = form.updated_at.data
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("blog.post"))
    return render_template("blog/edit.html", post=post, form=form, title="게시물 수정")

@blog.route("/post/<post_id>/delete", methods=["GET", "POST"])
@login_required
def delete_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("blog.post"))

# 일명 관리자모드..?
# @blog.route("/users")
# def users():
#     users = User.query.all()
#     return render_template("blog/users.html", users=users)

# @blog.route("/users/<user_id>", methods=["GET", "POST"])
# def edit_user(user_id):
#     form = UserForm()
#     user = User.query.filter_by(id=user_id).first()
#     if form.validate_on_submit():
#         user.nickname = form.nickname.data
#         user.email = form.email.data
#         user.password = form.password.data
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for("blog.post"))
#     return render_template("blog/edit_user.html", user=user, form=form, title="회원정보 수정")

# @blog.route("/users/<user_id>/delete", methods=["POST"])
# def delete_user(user_id):
#     user=User.query.filter_by(id=user_id).first()
#     db.session.delete(user)
#     db.session.commit()
#     return redirect(url_for("blog.post"))