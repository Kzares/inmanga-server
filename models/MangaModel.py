from database.db import get_conection
from .entities.Manga import Manga 
import json

class MangaModel: 

    ######__get all mangas 
    @classmethod
    def get_all_mangas(self):
        try:
            connection = get_conection()
            mangas = [] 

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM mangas ORDER BY title ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    
                    manga = Manga(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    mangas.append(manga.to_JSON())

            connection.close()
            return mangas

        except Exception as ex:
            raise Exception(ex)
        

    ######__get single manga
    @classmethod
    def get_manga(self, id):
        try:
            connection = get_conection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM mangas WHERE id = %s", (id,) )
                row = cursor.fetchone()
                
                manga = None
                if row != None:
                    manga = Manga(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9] )
                    manga = manga.to_JSON()

            connection.close()
            return manga
                
        except Exception as ex:
            raise Exception(ex)

    ######__get manga links
    @classmethod
    def get_manga_links(self, id):
        try:
            connection = get_conection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT links FROM mangas WHERE id = %s", (id,) )
                row = cursor.fetchone()
                
                links = row[0]

            connection.close()
            return links
                
        except Exception as ex:
            raise Exception(ex)
        
    ######__Search manga by name
    @classmethod
    def search_by_name(self, param):
        try:
            connection = get_conection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM mangas WHERE title LIKE %s ", ('%' +  (param) + '%' ,) )
                resultset = cursor.fetchall()
                mangas = []
                
                for row in resultset:
                    
                    manga = Manga(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    mangas.append(manga.to_JSON())

            connection.close()
            return mangas
                
        except Exception as ex:
            raise Exception(ex)
    
    ######__Search manga by author
    @classmethod
    def search_by_author(self, param):
        try:
            connection = get_conection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM mangas WHERE author LIKE %s ", ('%' +  (param) + '%' ,) )
                resultset = cursor.fetchall()
                mangas = []
                
                for row in resultset:
                    
                    manga = Manga(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    mangas.append(manga.to_JSON())

            connection.close()
            return mangas
                
        except Exception as ex:
            raise Exception(ex)

    ######__get top rated mangas 
    @classmethod
    def get_top_rated_mangas(self, start, end):
        try:
            connection = get_conection()
            mangas = [] 

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM mangas ORDER BY score DESC LIMIT %s OFFSET %s", (end - start, start))
                resultset = cursor.fetchall()

                for row in resultset:
                    
                    manga = Manga(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    mangas.append(manga.to_JSON())

            connection.close()
            return mangas

        except Exception as ex:
            raise Exception(ex)
    
    ######__get most popular mangas 
    @classmethod
    def get_most_popular_mangas(self, start,end):
        try:
            connection = get_conection()
            mangas = [] 

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM mangas ORDER BY points DESC LIMIT %s OFFSET %s", (end - start, start))
                resultset = cursor.fetchall()

                for row in resultset:
                    
                    manga = Manga(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    mangas.append(manga.to_JSON())

            connection.close()
            return mangas

        except Exception as ex:
            raise Exception(ex)

    
    ######__post manga  
    @classmethod
    def add_manga(self, manga):
        try:
            connection = get_conection()

            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO mangas (id, title, released, author, sinopsis, review,likes, score, points, categories) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )", (manga.id, manga.title, manga.released, manga.author, manga.sinopsis, manga.review, manga.likes, manga.score, manga.points, manga.categories) )

                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)

    ######__update manga
    @classmethod
    def edit_manga(self, manga):
        try:
            connection = get_conection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE mangas SET title = %s , released = %s , author = %s , sinopsis = %s , review = %s , score = %s, categories = %s
                                WHERE id = %s """, (  manga.title, manga.released, manga.author, manga.sinopsis, manga.review, manga.score,manga.categories,  manga.id ) )
                affected_rows= cursor.rowcount
                connection.commit()
            
            connection.close()
            return affected_rows
                
        except Exception as ex:
            raise Exception(ex)

    ######__update download links
    @classmethod
    def update_download_liks(self, id, links):
        try:
            connection = get_conection()

            with connection.cursor() as cursor:
                cursor.execute('UPDATE mangas SET links = %s WHERE id = %s', [json.dumps(links), id])
                affected_rows= cursor.rowcount
                connection.commit()
            
            connection.close()
            return affected_rows
                
        except Exception as ex:
            raise Exception(ex)

    ######__Search by one category
    @classmethod
    def search_by_single_category(self,category, start, end):
        try:
            mangas = []
            connection = get_conection()

            with connection.cursor() as cursor:

                # Buscar mangas por categoria
                query = "SELECT * FROM mangas WHERE categories @> %s ORDER BY title"
                query += " LIMIT %s OFFSET %s"

                cursor.execute(query, (json.dumps([category]), end - start , start))    
                
                resultset = cursor.fetchall()
                for row in resultset:
                    print(row)
                    manga = Manga(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]) 
                    mangas.append(manga.to_JSON())

            connection.close()
            return mangas

        except Exception as ex:
            raise Exception(ex)
        
    
    ######__Get all categories
    @classmethod
    def get_all_categories(self):
        try:
            connection = get_conection()
            categories = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT DISTINCT jsonb_array_elements_text(categories) FROM mangas;")
    
                categories = [result[0] for result in cursor.fetchall()]
            connection.close()
            return categories    
     
        except Exception as ex:
            raise Exception(ex)
    

    ######__Increase the manga score 
    @classmethod 
    def increase_manga_score(self, id, points):
        try:
            connection = get_conection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT points FROM mangas WHERE id = %s", (id,))  

                actual_points = cursor.fetchone()[0]
    
                new_points = actual_points + points

                cursor.execute("UPDATE mangas SET points = %s WHERE id = %s", (new_points, id))

                affected_rows= cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)


    ######__Like Manga
    @classmethod
    def like_manga(self, id, like):
        try:
            connection = get_conection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT likes FROM mangas WHERE id = %s", (id,))  

                actual_likes = cursor.fetchone()[0]
    
                new_likes = actual_likes + like

                cursor.execute("UPDATE mangas SET likes = %s WHERE id = %s", (new_likes, id))

                affected_rows= cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
      

        except Exception as ex:
            raise Exception(ex)

    




