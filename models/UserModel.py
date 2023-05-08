from database.db import get_conection
from .entities.User import User
from .entities.Admin import Admin
from .entities.Manga import Manga
import json
class UserModel:

        ######__Create User
    @classmethod
    def create_user(self, user):
        try:
            connection = get_conection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO users (id, username, password, hidden, saved, liked)
                                VALUES  (%s, %s, %s, %s, %s, %s)""", (user.id, user.username, user.password, user.hidden, user.saved, user.liked ))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
                
        except Exception as ex:
            raise Exception(ex)

    ######__login user
    @classmethod
    def login_user(self, username, password):
        try:
            connection = get_conection()

            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM users
                                WHERE username = %s AND password = %s """, (username, password ) )
                row = cursor.fetchone()

                data = None
                if row != None:
                    data = User(row[0], row[1], row[2], row[3], row[4], row[5] )
                    data = data.to_JSON()

            connection.close()
            return data
                
        except Exception as ex:
            raise Exception(ex)

    ######__get user saved mangas
    @classmethod
    def get_saved(self, mangasArray):
        try:
            connection = get_conection()
            mangas = []
            with connection.cursor() as cursor:
                for id in mangasArray:
                    cursor.execute("SELECT * FROM mangas WHERE id = %s", (id,) )
                    row = cursor.fetchone()

                    manga = None
                    if row != None:
                        manga = Manga(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9] )
                        manga = manga.to_JSON()
                        mangas.append(manga)
            connection.close()
            return mangas



        except Exception as ex:
            raise Exception(ex)

    ######__get top rated mangas exepting the hide mangas
    @classmethod
    def get_top_rated_mangas(self,hidden, start, end):
        try:
            connection = get_conection()
            mangas = [] 
            excluded_ids_str = tuple(hidden)

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM mangas WHERE id NOT IN %s LIMIT %s OFFSET %s ", (excluded_ids_str, end - start, start ) ) 
                resultset = cursor.fetchall()
                for row in resultset:
                    print(row)
                    manga = Manga(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]) 
                    mangas.append(manga.to_JSON())

            connection.close
            return mangas

        except Exception as ex:
            raise Exception(ex)

    ######__get mangas by categoris exepting the hide mangas
    @classmethod
    def get_single_category(self,hidden,category, start, end):
        try:
            mangas = []
            connection = get_conection()
            excluded_ids = tuple(hidden)

            with connection.cursor() as cursor:
                # Buscar mangas por categoria
                query = "SELECT * FROM mangas WHERE categories @> %s"
                if excluded_ids:
                    query += " AND id NOT IN %s" # agregar cláusula para excluir elementos
                query += " ORDER BY title LIMIT %s OFFSET %s"

                cursor.execute(query, (json.dumps([category]), tuple(excluded_ids), end - start, start))  

                resultset = cursor.fetchall() 
                for row in resultset:
                    manga = Manga(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    mangas.append(manga.to_JSON())

            connection.close()
            return mangas

        except Exception as ex:
            raise Exception(ex)

    ######__login admin
    @classmethod
    def login_admin(self, username, password):
        try:
            connection = get_conection()

            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM admins
                                WHERE username = %s AND password = %s """, (username, password ) )
                row = cursor.fetchone()

                data = None
                if row != None:
                    data = Admin(row[0], row[1], row[2])
                    data = data.to_JSON()

            connection.close()
            return data
                
        except Exception as ex:
            raise Exception(ex)

    ######__update user likes
    @classmethod
    def update_users_likes(self,id,likes_array):
        try:
            connection = get_conection()

            with connection.cursor() as cursor:
                cursor.execute("UPDATE users SET liked = %s WHERE id = %s ", ( likes_array, id ) )
                affected_rows= cursor.rowcount
                connection.commit()
            
            connection.close()
            return affected_rows
                
        except Exception as ex:
            raise Exception(ex)
    
    ######__update user saved
    @classmethod
    def update_users_saved(self,id,saved_array):
        try:
            connection = get_conection()

            with connection.cursor() as cursor:
                cursor.execute("UPDATE users SET saved = %s WHERE id = %s ", ( saved_array, id ) )
                affected_rows= cursor.rowcount
                connection.commit()
            
            connection.close()
            return affected_rows
                
        except Exception as ex:
            raise Exception(ex)
    
    ######__update user hidden
    @classmethod
    def update_users_hidden(self,id,hidden_array):
        try:
            connection = get_conection()

            with connection.cursor() as cursor:
                cursor.execute("UPDATE users SET hidden = %s WHERE id = %s ", ( hidden_array, id ) )
                affected_rows= cursor.rowcount
                connection.commit()
            
            connection.close()
            return affected_rows
                
        except Exception as ex:
            raise Exception(ex)














