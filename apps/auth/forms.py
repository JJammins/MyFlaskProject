from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class EditUserForm(FlaskForm):
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
    submit = SubmitField("회원정보 수정")


class SignUpForm(FlaskForm):
    nickname = StringField(
        "닉네임",
        validators=[
            DataRequired("닉네임을 입력해주세요."),
            Length(1, 10, "10글자 이내로 입력해주세요.")
        ]
    )
    email = StringField(
        "이메일",
        validators=[
            DataRequired("이메일을 입력해주세요."),
            Email("이메일 형식이 잘못되었습니다.")
        ]
    )
    password = PasswordField(
        "비밀번호",
        validators=[DataRequired("비밀번호를 입력해주세요.")])
    submit = SubmitField("회원가입")

class LoginForm(FlaskForm):
    email = StringField(
        "이메일",
        validators=[
            DataRequired("이메일을 입력해주세요."),
            Email("이메일 형식이 잘못되었습니다.")
        ]
    )
    password = PasswordField("비밀번호", validators=[DataRequired("비밀번호를 입력해주세요.")])
    submit = SubmitField("로그인")
