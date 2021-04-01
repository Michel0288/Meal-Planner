
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, PasswordField
from wtforms.validators import DataRequired, Optional, InputRequired
from wtforms.widgets import TextArea


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class SignUpForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()], description="Please enter your first name.")
    lastname = StringField('Last Name', validators=[DataRequired()], description="Please enter your last name.")
    username = StringField('Username', validators=[DataRequired()], description="Please enter a username.")
    password = PasswordField('Password', validators=[DataRequired()], description="Please enter a password.")
    age = IntegerField('Age', validators=[DataRequired()], description="Please enter your age.")
    gender = SelectField('Gender', choices=[('Male'), ('Female'), ('Other')], description="Please select your gender.")
    height = StringField('Height', validators=[DataRequired()], description="Please select you height.")
    weight = StringField('Weight', validators=[DataRequired()], description="Please eneter your weight.")
    allergies = StringField('Food Allergies', validators=[DataRequired()], description="Please enter any food or ingredients you are allergic to.")
    dietarylifestyle = SelectField('Dietary Lifestyle', validators=[DataRequired()], choices=[('None'), ('Vegan'), ('Vegetarian'), ('Pescatarian')], description="Please select a dietary lifestyle.")
    dietaryrestrictions = SelectField('Dietary Restrictions', validators=[DataRequired()], choices=[('None'), ('Lactose Intolerance'), ('Diabetic'), ('High Blood Pressure')], description="Please select a dietary restriction.")
    goal = SelectField('Goals', validators=[DataRequired()], choices=[('None'), ('Gain Weight'), ('Lose Weight'), ('Maintain Weight')], description="Please select your weight goal.")
    dailycalories = StringField('Daily Calories Intake', validators=[DataRequired()], description="Please select your expected daily calorie intake.")

class RecipeForm(FlaskForm):
    ingredient_name = StringField('Ingredient Name',validators=[DataRequired()], description="Please enter ingredient name.")
    measurements = StringField('Measurement', widget=TextArea(), validators=[DataRequired()], description="Please enter recipe procedure.")
    calories = IntegerField('Calorie Count',validators=[DataRequired()], description="Please enter amount of calories for ingredient.")
    recipe_name = StringField('Recipe Name',validators=[DataRequired()], description="Please enter name of recipe.")
    prep_time = StringField('Preparation Time', validators=[DataRequired()], description="Please enter amount of time for prepare recipe.")
    cook_time = StringField('Cooking Time', validators=[DataRequired()], description="Please enter amount of time to cook recipe." )
    procedure = StringField('Procedure', widget=TextArea(), validators=[DataRequired()], description="Please enter recipe procedure.")
    mealtype = SelectField('Meal Type', choices= [('Breakfast'), ('Lunch'), ('Dinner')], validators=[Optional()], description="Please select type of meal.")  
    servings = IntegerField('Servings',validators=[DataRequired()], description="Please enter amount of servings.")