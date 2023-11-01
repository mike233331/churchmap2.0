from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from reader.models import Church

# class BookForm(FlaskForm):
class ChurchForm(FlaskForm):

    title = StringField('Название', validators=[DataRequired(),
                                             Length(min=5, max=100)])
    author = StringField('Дата строительства', validators=[DataRequired(),
                                             Length(min=5, max=100)])
    genre = StringField('Страна', validators=[DataRequired(),
                                             Length(min=5, max=20)])
    cover = FileField('Обложка церкви', validators=[FileAllowed(['jpg', 'png'])])
    rating = IntegerField('Моя оценка', validators=[DataRequired(), NumberRange(min=1, max=5)])
    description = TextAreaField('Краткое описание',
                                validators=[DataRequired(),
                                            Length(max=500)])
    notes = TextAreaField('Заметки',
                                validators=[DataRequired(),
                                            Length(max=500)])
    submit = SubmitField('Добавить')

    def validate_title(self, title):
        title = Church.query.filter_by(title=title.data).first()
        if title:
            raise ValidationError('Такая церковь уже есть в списке.')


# class UpdateBook(FlaskForm):
class UpdateChurch(FlaskForm):

    title = StringField('Название', validators=[DataRequired(),
                                             Length(min=5, max=100)])
    author = StringField('Дата строительства', validators=[DataRequired(),
                                             Length(min=5, max=100)])
    genre = StringField('Страна', validators=[DataRequired(),
                                             Length(min=5, max=20)])
    cover = FileField('Обложка Церкви', validators=[FileAllowed(['jpg', 'png'])])
    rating = IntegerField('Моя оценка', validators=[DataRequired(), NumberRange(min=1, max=5)])
    description = TextAreaField('Краткое описание',
                                validators=[DataRequired(),
                                            Length(max=500)])
    notes = TextAreaField('Заметки',
                                validators=[DataRequired(),
                                            Length(max=500)])
    submit = SubmitField('Обновить')