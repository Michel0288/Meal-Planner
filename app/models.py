from . import db

class RecipeProperty(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'recipe_property'

    id = db.Column(db.Integer, primary_key=True)
    recipe_name= db.Column(db.String(255))
    prep_time = db.Column(db.String(255))
    procedure = db.Column(db.String(255))
    mealtype = db.Column(db.String(255))
    tot_cal = db.Column(db.Integer(255))


    def __init__(self,recipe_name,prep_time,procedure,mealtype,tot_cal):
        self.recipe_name=recipe_name
        self.prep_time=prep_time
        self.procedure=procedure
        self.mealtype=mealtype
        self.tot_cal=tot_cal
       
class IngredientProperty(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'ingredient_property'

    id = db.Column(db.Integer, primary_key=True)
    ingredient_name= db.Column(db.String(255))
    measurements = db.Column(db.String(255))
    calories= db.Column(db.Integer(255))


    def __init__(self,ingredient_name,measurements,calories):
        self.ingredient_name=ingredient_ename
        self.measurements=measurements
        self.calories=calories