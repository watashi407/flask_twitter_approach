from queue import Empty
from flask import Blueprint, render_template, request, flash, redirect, url_for , jsonify , session
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from flask_login import login_required, current_user
from .models import Note
from .models import Member
from .models import Application
import json
import requests
from authlib.integrations.flask_client import OAuth

# global Auth google
client_id ="161481167666-bo6o274c7nge91vilidt36hncmmsuqna.apps.googleusercontent.com"
global_client ="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"

#other imports

views = Blueprint('views', __name__)

@views.route('/')
def home():
    
    return render_template("home.html")

@views.route('/login')
def loginAuth():
    # get the query agrument
    if request.args.get("next"):
        session["next"] = request.args.get("next")
    return redirect(f"https://accounts.google.com/o/oauth2/v2/auth?scope=https://www.googleapis.com/auth/userinfo.profile&access_type=offline&include_granted_scopes=true&response_type=code&redirect_uri=https://note-web.herokuapp.com/authorized&client_id={GOOGLE_CLIENT_ID}")

@views.route('/auth')
def auth():

    return redirect("/")




# # application for coach
# @views.route('/applicant', methods=['GET', 'POST'])
# def application():

#     if request.method == 'POST':
#         appname = request.form.get('appname')
#         appemail = request.form.get('appemail')
#         appnum = request.form.get('appnum')
#         appdes = request.form.get('appdes')
#         appstat = request.form.get('appstat')
#         appexp = request.form.get('appexp')

#         if len(appname) < 4:
#             flash('appname must be greater than 3 characters.', category='error')
#         elif len(appemail) < 4:
#             flash('appemail must be greater than 3 characters.', category='error')
#         elif len(appnum) < 4:
#             flash('appnum must be greater than 3 characters.', category='error')
#         elif len(appdes) < 4:
#             flash('appdes must be greater than 3 characters.', category='error')
#         # elif appname == " ":
#         #     flash('input fields appname required ', category='error')
#         # elif appemail == " ":
#         #     flash('input fields appemail required ', category='error')
#         # elif appnum == " ":
#         #     flash('input fields  appnum required ', category='error')
#         # elif appdes == " ":
#         #     flash('input fields appdes required ', category='error')
#         else:
#             new_applicant = Application( name=appname , number=appnum , email=appemail , descrip = appdes , experience=appexp, status = appstat)
#             db.session.add(new_applicant)
#             db.session.commit()
#             flash('Send Succesfully , Wait for admin confirmation', category='success')
#             return redirect(url_for('views.home'))

#     return render_template("home.html", user=current_user)



# @views.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password1 = request.form.get('password1')
#         password2 = request.form.get('password2')

#         user = User.query.filter_by(username=username).first()
#         if user:
#             flash('username already exists.', category='error')
#         elif len(username) < 4:
#             flash('username must be greater than 3 characters.', category='error')
#         elif password1 != password2:
#             flash('Passwords don\'t match.', category='error')
#         elif len(password1) < 7:
#             flash('Password must be at least 7 characters.', category='error')
#         else:
#             new_user = User(username=username, password=generate_password_hash(
#             password1, method='sha256'))
#             db.session.add(new_user)
#             db.session.commit()
#             login_user(new_user, remember=True)
#             flash('Account created!', category='success')
#             return redirect(url_for('views.admin'))
            
#     return render_template("signup.html", user=current_user , )


# #search



# # admin

# @views.route('/admin', methods=['GET', 'POST'])
# @login_required
# def admin():
#     # if request.method == 'POST':
#     #     note = request.form.get('note')
#     #     member = request.form.get('Member')

#     #     if len(note) < 1:
#     #         flash('Note is too short!', category='error')
#     #     else:
#     #         new_note = Note(data=note, user_id=current_user.id)
#     #         db.session.add(new_note)
#     #         db.session.commit()
#     #         flash('Note added!', category='success')
#     if request.method == 'POST':
#         appname = request.form.get('appname')
#         appemail = request.form.get('appemail')
#         appnum = request.form.get('appnum')
#         appdes = request.form.get('appdes')
#         appstat = request.form.get('appstat')
#         appexp = request.form.get('appexp')

#         if len(appname) < 4:
#             flash('appname must be greater than 3 characters.', category='error')
#         elif len(appemail) < 4:
#             flash('appemail must be greater than 3 characters.', category='error')
#         elif len(appnum) < 4:
#             flash('appnum must be greater than 3 characters.', category='error')
#         elif len(appdes) < 4:
#             flash('appdes must be greater than 3 characters.', category='error')
#         # elif appname == " ":
#         #     flash('input fields appname required ', category='error')
#         # elif appemail == " ":
#         #     flash('input fields appemail required ', category='error')
#         # elif appnum == " ":
#         #     flash('input fields  appnum required ', category='error')
#         # elif appdes == " ":
#         #     flash('input fields appdes required ', category='error')
#         else:
#             new_Member = Member( name=appname , number=appnum , email=appemail , descrip = appdes , experience=appexp, status = appstat)
#             db.session.add(new_Member)
#             db.session.commit()
#             flash('Accepted successfull', category='success')
#             return redirect(url_for('views.admin'))

#     member = Member.query.order_by(Member.date)
#     searched = Application.query.order_by(Application.date)
#     return render_template("admin.html", user=current_user , applicant=searched , member=member)

# @views.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('views.home'))

# @views.route('/delete-note', methods=['POST'])
# def delete_note():
#     note = json.loads(request.data)
#     appId = note['appId']
#     note = Member.query.get(appId)
#     if note:
#         if note.user_id == current_user.id:
#             db.session.delete(note)
#             db.session.commit()

#     return jsonify({})
