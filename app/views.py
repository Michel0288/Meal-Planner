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
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
from flask_mysqldb import MySQL
import MySQLdb.cursors



app.config['MYSQL_HOST']='127.0.0.1'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='meal_planner'

mysql=MySQL(app)

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

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('SELECT * FROM account WHERE username = % s AND password = % s', (username, password))        
        user = cur.fetchone()
        
        if user:
            session['loggedin'] = True
            session['id'] = user['account_id']
            session['username'] = user['username']
            flash('Success.', 'danger')
            return redirect(url_for('home'))
        else:
            flash('Error.', 'danger')
            return "error"
        # user = UserProfile.query.filter_by(username=username).first()
        # if user is not None and check_password_hash(user.password,password):
        #     remember_me = False
        #     if 'remember_me' in request.form:
        #         remember_me = True
        #     login_user(user, remember=remember_me)
        #     flash('Login successful!', 'success')
        #     return redirect(url_for("secure_page"))
        # else:
        #     flash('Username or password is incorrect.', 'danger')   
    flash_errors(form)
    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))    

@app.route("/profile")
# @login_required
def profile():

    return render_template("profile.html")

@app.route('/recipe', methods=['POST', 'GET'])
def recipe():
    recipeform=RecipeForm()

    if request.method == 'POST' and recipeform.validate_on_submit():
        ingredient_name = recipeform.ingredient_name.data
        measurements = recipeform.measurements.data
        calories = recipeform.calories.data
        recipe_name = recipeform.recipe_name.data
        prep_time = recipeform.prep_time.data
        cook_time = recipeform.cook_time.data
        procedure = recipeform.procedure.data
        mealtype = recipeform.mealtype.data
        servings = recipeform.servings.data
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('YOu have sucessfully added a recipe', 'success')
        return render_template()
    
    flash_errors(recipeform)
    return render_template('recipe.html', form=recipeform)

def get_uploaded_images():
    rootdir = os.getcwd()
    photolist = []

    for subdir, dirs, files in os.walk(rootdir + '/uploads'):
        for file in files:
            photolist += [file]
    photolist.pop(0)
    return photolist

@app.route('/uploads/<filename>')
def get_image(filename):
    rootdir2 = os.getcwd()

    return send_from_directory(os.path.join(rootdir2, app.config['UPLOAD_FOLDER']), filename)

@app.route('/SignUp', methods=['POST', 'GET'])
def signup():
    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        username = form.username.data
        password = form.password.data
        age = form.age.data
        gender = form.gender.data
        height = form.height.data
        weight = form.weight.data
        allergies = form.allergies.data
        dietarylifestyle = form.dietarylifestyle.data
        dietaryrestrictions = form.dietaryrestrictions.data 
        goal = form.goal.data
        dailycalories = form.dailycalories.data
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO account (firstname,lastname,username,password,age,gender,height,weight,allergies,dietarylifestyle,dietaryrestrictions,goal,dailycalories,photo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (firstname,lastname,username,password,age,gender,height,weight,allergies,dietarylifestyle,dietaryrestrictions,goal,dailycalories,photo))
        mysql.connection.commit()
        cur.close()
        flash("Signup Successful!", 'success')
        return redirect(url_for('login'))
    return render_template('signup.html',form=form)
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
