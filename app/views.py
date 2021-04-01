"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app
from flask import render_template, request, redirect, url_for, flash, session, abort,send_from_directory
from werkzeug.utils import secure_filename
from .forms import RecipeForm, SignUpForm, LoginForm





###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/login/', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    
    if request.method == "POST" and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        flash('Login successful!', 'success')
        return redirect(url_for("home"))
    return render_template('login.html', form=form)

@app.route('/logout/')
def logout():
    """Render the website's login page."""
    return render_template('logout.html')


@app.route('/recipe', methods=['POST', 'GET'])
def recipe():
    recipeform=RecipeForm()

    if request.method == 'POST' and recipeform.validate_on_submit():
        ingredient_name=recipeform.ingredient_name.data
        measurements=recipeform.measurements.data
        calories=recipeform.calories.data
        recipe_name=recipeform.recipe_name.data
        prep_time=recipeform.prep_time.data
        procedure=recipeform.procedure.data
        mealtype=recipeform.mealtype.data
        tot_cal=recipeform.tot_cal.data


        

        flash('You have sucessfully added a recipe', 'success')
        return render_template()
    
    flash_errors(recipeform)
    return render_template('recipe.html', form=recipeform)

@app.route('/Sign-Up', methods=['POST', 'GET'])
def signup():
    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        age = request.form['age']
        height = request.form['height']
        weight = request.form['weight']
        goals = request.form['goals']
        calories = request.form['calories']


        flash("Signup Successful!", 'success')
        return redirect(url_for('login'))

    return render_template('signup.html', form=form)
###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
