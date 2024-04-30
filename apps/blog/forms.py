from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Email, Length
from datetime import datetime

class UserForm(FlaskForm):
    nickname = StringField(
        "닉네임",
        validators=[
            DataRequired(message = "닉네임을 입력해주세요."),
            Length(max=10, message = "10글자 이내로 입력해주세요.")
        ]
    )
    email = StringField(
        "이메일",
        validators=[
            DataRequired(message = "이메일을 입력해주세요."),
            Email(message = "이메일 형식이 잘못되었습니다.")
        ]
    )
    password = PasswordField(
        "비밀번호",
        validators=[DataRequired(message="비밀번호를 입력해주세요.")]
    )
    submit = SubmitField("회원가입")


class PostForm(FlaskForm):
    title = StringField(
        "제목",
        validators=[
            DataRequired(message = "제목을 작성해주세요.")
        ]
    )
    content = TextAreaField(
        "내용",
        validators=[
            DataRequired(message = "내용을 입력해주세요.")
        ]
    )
    created_at = DateTimeField("생성일", default=datetime.now)
    updated_at = DateTimeField("업데이트일", default=datetime.now)
    submit = SubmitField("등록")