from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired
from datetime import datetime

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