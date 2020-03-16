from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextAreaField, TextField, SelectField
from wtforms.validators import DataRequired, Email





class ProfileForm(FlaskForm):
    F_Name = TextField('First Name', validators = [DataRequired()])
    L_Name = TextField('Last Name', validators = [DataRequired()])
    Gender = SelectField('Gender', choices = [('Male', 'Male'),('Female', 'Female')])
    Email = TextField('Email', validators = [DataRequired(), Email()], render_kw={"placeholder": "e.g. jdoe@example.com"})
    Location = TextField('Location', validators = [DataRequired()], render_kw={"placeholder": "e.g. Kingston, Jamaica"})
    Biography = TextAreaField('Biography', validators = [DataRequired()])
    file = FileField('Profile Picture', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])
   
