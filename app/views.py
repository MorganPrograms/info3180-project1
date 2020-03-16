"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app
from app import db
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename
from app.forms import ProfileForm
from app.models import Profile
import datetime 

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
    return render_template('about.html', name="the profiles created for Project 1")

@app.route('/files/')
def files():
    if not session.get('logged_in'):
         abort(401)
    return render_template('files.html', file = get_uploaded_images())



@app.route('/profile', methods=['POST', 'GET'])
def profile():
    # Instantiate your form class
    if request.method == 'GET':
        form = ProfileForm()
        return render_template('profile.html', form = form)

    # Validate file upload on submit
    form = ProfileForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Get file data and save to your uploads folder
        F_Name = form.F_Name.data
        L_Name =  form.L_Name.data
        Gender = form.Gender.data
        Email = form.Email.data
        Location = form.Location.data
        Biography = form.Biography.data
        file = form.file.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        profile = Profile(F_Name,L_Name,Gender,Email,Location,Biography,filename,datetime.datetime.now().strftime("%B %d, %Y"))
        db.session.add(profile)
        db.session.commit()
        
        

        flash('Profile Added', 'success')
        return redirect(url_for('profiles', images = get_uploaded_images()))
    return redirect(url_for('home'))

@app.route('/profiles')
def profiles():
    profiles = Profile.query.all()
    return render_template('profiles.html', images = get_uploaded_images(), profiles = profiles)

@app.route('/profileuserid/<int:userid>')
def profileuserid(userid):
    profile = Profile.query.filter_by(id=userid).first()
    return render_template('profileuserid.html', profile = profile)
    





@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            
            flash('You were logged in', 'success')
            return redirect(url_for('upload'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out', 'success')
    return redirect(url_for('home'))


###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails
def get_uploaded_images():
    rootdir = os.getcwd()
    print (rootdir)
    f = []
    for subdir, dirs, files in os.walk(rootdir + r'\app\static\uploads'):
        for file in files:
            f.append(file)
    return f[1:]
    
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
