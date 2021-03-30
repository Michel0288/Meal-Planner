
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    Image =FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png'],"Only images are accepted")])
