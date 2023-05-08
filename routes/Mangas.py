from flask import Blueprint, jsonify, request
import uuid
import json
#Entities
from models.entities.Manga import Manga

#Models
from models.MangaModel import MangaModel

main = Blueprint('manga_blueprint', __name__)

####_get all the mangas
@main.route('/')
def get_posts():
    try:
        mangas = MangaModel.get_all_mangas()
        return jsonify(mangas)
    except Exception as ex:
        return jsonify({
            'message' : str(ex)
        }),500
    
#####_get single manga
@main.route('/<id>')
def get_manga(id):
    try:
        manga = MangaModel.get_manga(id)
        if manga != None:
            return jsonify(manga)
        else: 
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message' : str(ex)}), 500


#####_search by name
@main.route('/search/<param>')
def search_by_name(param):
    try:
        mangas = MangaModel.search_by_name(param)
        return jsonify(mangas)
    except Exception as ex:
        return jsonify({'message' : str(ex)}), 500
    
#####_search by author
@main.route('/search-author/<param>')
def search_by_author(param):
    try:
        mangas = MangaModel.search_by_author(param)
        return jsonify(mangas)
    except Exception as ex:
        return jsonify({'message' : str(ex)}), 500


#####__top rated mangas
@main.route('/top-rated')
def get_top_rated_mangas():
    try:
        start = int(request.args.get('start', 0))
        end = int(request.args.get('end', 4))
        mangas = MangaModel.get_top_rated_mangas(start,end)
        return jsonify(mangas)
    except Exception as ex:
        return jsonify({
            'message' : str(ex)
        }),500
    
#####_most popular mangas
@main.route('/most-popular')
def get_most_popular_mangas():
    try:
        start = int(request.args.get('start', 0))
        end = int(request.args.get('end', 4))
        mangas = MangaModel.get_most_popular_mangas(start,end)
        return jsonify(mangas)
    except Exception as ex:
        return jsonify({
            'message' : str(ex)
        }),500

#####__post manga
@main.route('/add', methods=['POST'] )
def add_manga():
    try: 
        id = uuid.uuid4()
        title = request.json['title']
        released = request.json['released']
        author = request.json['author']
        sinopsis = request.json['sinopsis']
        review = request.json['review']
        categories = json.dumps(request.json['categories'])
        likes = 0
        score = request.json['score'] 
        points = 0

        manga = Manga( str(id), title, released, author, sinopsis, review, likes, score, points, categories)

        affected_rows = MangaModel.add_manga(manga)
        if affected_rows == 1:
            return jsonify(manga.id)
        else:
            return jsonify({'message' : 'Error on insert'}), 500

    except Exception as ex:
        return jsonify({'message' : str(ex)}), 500

#####__edit manga
@main.route('/edit/<id>', methods=['PUT'])
def edit_manga(id):
    try:
        title = request.json['title']
        released = request.json['released']
        author = request.json['author']
        sinopsis = request.json['sinopsis']
        review = request.json['review']
        categories = json.dumps(request.json['categories'])
        likes = 0
        score = request.json['score'] 
        points = 0


        manga = Manga(id, title, released, author, sinopsis, review, likes, score, points, categories)
        affected_rows = MangaModel.edit_manga(manga)

        if affected_rows == 1:
            return jsonify(manga.id)
        else:
            return jsonify({'message' : 'No movie updated'}), 500

    except Exception as ex:
        return jsonify({'message' : str(ex)}), 500
    

#####__Search by Category

@main.route('/category/<category>')
def search_by_categories(category):
    try:
        start = int(request.args.get('start', 0))
        end = int(request.args.get('end', 4))
        mangas = MangaModel.search_by_single_category(category, start, end)
        return jsonify(mangas)
    except Exception as ex:
        return jsonify({'message' : str(ex)}), 500

######__Get all categories
@main.route('/category/get-all')
def get_all_categories():
    try:
        
        categories = MangaModel.get_all_categories()
        return jsonify(categories)
    except Exception as ex:
        return jsonify({'message' : str(ex)}), 500



######__Like Manga 
@main.route('/like/<id>')
def like_manga(id):
    try:
        score = int(request.args.get('score', 5))
        like = int(request.args.get('like', 1))

        like_count = MangaModel.like_manga(id, like)
        score_count = MangaModel.increase_manga_score(id, score)

        if like_count == score_count == 1 :
            return jsonify({'mesage': 'succes'})
        else :
            return jsonify({'message': 'An error Ocurred'})

    except Exception as ex:
        return jsonify({'message': str(ex) }), 500

 ######__Increase manga score 
@main.route('/increase-score/<id>')
def increase_manga_score(id):
    score = int(request.args.get('score', 1))

    score_count = MangaModel.increase_manga_score(id, score)

    if score_count == 1 :
            return jsonify({'mesage': 'succes'})
    else :
        return jsonify({'message': 'An error Ocurred'})
    


