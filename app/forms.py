
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, PasswordField
from wtforms.validators import DataRequired, Optional, InputRequired
from wtforms.widgets import TextArea

class RecipeForm(FlaskForm):
    ingredient_name=StringField('Ingredient Name',validators=[DataRequired()])
    measurements=StringField('Measurements',validators=[DataRequired()])
    calories=IntegerField('Calorie Count',validators=[DataRequired()])


    recipe_name=StringField('Recipe Name',validators=[DataRequired()])
    prep_time=StringField('Preparation Time', validators=[DataRequired()])
    procedure=StringField('Procedure', widget=TextArea(), validators=[DataRequired()])
    mealtype=SelectField('Meal Type', choices= [('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], validators=[Optional()])
    tot_cal=IntegerField('Calorie Count',validators=[DataRequired()])

class SignUpForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    age = StringField('Age', validators=[InputRequired()])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')])
    height = StringField('Height', validators=[InputRequired()])
    weight = StringField('Weight', validators=[InputRequired()])
    goals = SelectField('Goals', choices=[('Gain', 'Gain'), ('Lose', 'Lose'), ('Maintain', 'Maintain')])
    calories = StringField('Calories', validators=[InputRequired()])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])