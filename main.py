from app.models.posts.post_model import Genre, Post, PostGenres

from app.models.basemodel import db_connection, db

from app.queries.genres import create_genre, delete_genre, get_genres

from app.queries.posts import create_post, get_all_films, get_film_by_id

from app.schemas.posts import PostCreateSchema

from app.routes.posts import router

from fastapi import FastAPI

@db
def create_tables():
    db_connection.create_tables([Genre, Post, PostGenres])

create_tables()

app = FastAPI()

app.include_router(router)

# create_genre('Детектив')
# create_genre('Ужас')

# delete_genre('Детектив')
# print(get_genres())
# create_post('Ходячие мертвецы', "Сериал про зомби", "2003", 'USA', ['Детектив', 'Ужас'])
# create_post('Шерлок Холмс', "Сериал про детектива", '2005', 'USA', ['Детектив'])

# print(get_all_films())
# print(get_film_by_id(10))
# from datetime import date
# create_post(PostCreateSchema(title='Batman',description='Фильм про мышь', year=date(2015, 1, 1), country='USA', genre=['Детектив', 'Ужас']))