from flask_app.models.user import User
from flask_app import app
from flask import render_template, jsonify, request, redirect

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users')
def users():
    return jsonify(User.get_all_json())

@app.route('/create/user',methods=['POST'])
def create_user():
    new_user_id= User.save(request.form)
    new_user = User.get_user_by_user_id({new_user_id})
    print(new_user)
    this_user = {
        'user_name': new_user.user_name,
        'email' : new_user.email
    }
    print(new_user)
    return jsonify(this_user)



