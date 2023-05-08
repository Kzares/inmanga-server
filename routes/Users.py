from flask import Blueprint, jsonify, request
import uuid
import json

#Entities 
from models.entities.User import User

#Models
from models.UserModel import UserModel

main=Blueprint('movie_blueprint', __name__)


@main.route('/register', methods=['POST'])
def create_user():
    try:
        username = request.json['username']
        password = request.json['password']
        id = uuid.uuid4()
        hidden = []
        saved = []
        liked = []

        user = User(str(id), username, password, hidden, saved, liked)
        affected_rows = UserModel.create_user(user)

        if affected_rows == 1:
            return jsonify(user.to_JSON())
        else:
            return jsonify({
                'message': 'Error on insert'
            }), 500

    except Exception as ex:
        return jsonify({
            "message": str(ex)
        }), 500

@main.route('/login', methods=['POST'])
def login_user():
    try:
        username = request.json['username']
        password = request.json['password']

        user = UserModel.login_user(username, password)
        if user != None:
            return jsonify(user)
        else:
            return jsonify({}), 404
        
    except Exception as ex:
        return jsonify({
            "message": str(ex)
        }), 500

######__get user saved mangas
@main.route('/get-saved-mangas', methods=['POST'] )
def get_saved(): 
    try:
        mangasArray = request.json['mangas']
        mangas = UserModel.get_saved(mangasArray)

        return jsonify(mangas)
    except Exception as ex:
        return jsonify({
            "message": str(ex)
        }), 500


@main.route('/top-rated', methods=['POST'])
def get_top_rated():
    try:
        hidden = request.json['hidden']
        start = int(request.args.get('start', 0))
        end = int(request.args.get('end', 4))

        mangas = UserModel.get_top_rated_mangas(hidden,start,end)
        return jsonify(mangas)
    except Exception as ex:
        return jsonify({
            "message": str(ex)
        }), 500
@main.route('/category/<category>', methods=['POST'])
def get_single_category(category):
    try:
        hidden = request.json['hidden']
        start = int(request.args.get('start', 0))
        end = int(request.args.get('end', 4))

        mangas = UserModel.get_single_category(hidden, category,start,end)
        return jsonify(mangas)
    except Exception as ex:
        return jsonify({
            "message": str(ex)
        }), 500
    

@main.route('/login-admin', methods=['POST'])
def login_admin():
    try:
        username = request.json['username']
        password = request.json['password']

        admin = UserModel.login_admin(username, password)
        if admin != None:
            return jsonify(admin)
        else:
            return jsonify({}), 404
        
    except Exception as ex:
        return jsonify({
            "message": str(ex)
        }), 500


######__Update users liked
@main.route('/update-user/liked', methods=['POST'])
def update_user_liked():
    try:
        id = request.json['id']
        liked = json.dumps(request.json['liked'])

        affected_rows = UserModel.update_users_likes(id,liked)
        if affected_rows == 1:
            return jsonify(id)
        else:
            return jsonify({'message' : 'Error on insert'}), 500



    except Exception as ex:
        return jsonify({
            "message": str(ex)
        }), 500
    
######__Update users saved
@main.route('/update-user/saved', methods=['POST'])
def update_user_saved():
    try:
        id = request.json['id']
        saved = json.dumps(request.json['saved'])

        affected_rows = UserModel.update_users_saved(id,saved)
        if affected_rows == 1:
            return jsonify(id)
        else:
            return jsonify({'message' : 'Error on insert'}), 500



    except Exception as ex:
        return jsonify({
            "message": str(ex)
        }), 500
    
######__Update users hidden
@main.route('/update-user/hidden', methods=['POST'])
def update_user_hidden():
    try:
        id = request.json['id']
        hidden = json.dumps(request.json['hidden'])

        affected_rows = UserModel.update_users_hidden(id,hidden)
        if affected_rows == 1:
            return jsonify(id)
        else:
            return jsonify({'message' : 'Error on insert'}), 500



    except Exception as ex:
        return jsonify({
            "message": str(ex)
        }), 500

