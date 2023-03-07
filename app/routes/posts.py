from app.queries.posts import (get_all_films, get_film_by_id, create_post)
from fastapi import APIRouter

router = APIRouter()

@router.get('/posts')
def get_films():
    return get_all_films()