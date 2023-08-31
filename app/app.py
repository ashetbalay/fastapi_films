from fastapi import FastAPI
from database.init_db import session, Films


app = FastAPI()


@app.get("/films")
def get_films():
    films = session.query(Films).all()
    result = []
    for film in films:
        result.append({
            "title": film.title,
            "genre": film.genre,
            "year": film.year,
            "director": film.director
        })

    return result


@app.get("/films/{pk}")
def get_film(pk: int):
    return session.get(Films, pk)


@app.post("/film")
def set_film(title, genre, year, director):
    req = Films(
        title=title,
        genre=genre,
        year=year,
        director=director
    )

    session.add(req)
    session.commit()
    session.close()

    return "Created!"


@app.put("/film/{pk}")
def update_film(pk: int, title, genre, year, director):
    film = session.get(Films, pk)
    film.title = title
    film.genre = genre
    film.year = year
    film.director = director

    session.commit()
    session.close()
    return "Update!"


@app.delete("/film/{pk}")
def delete_film(pk: int):
    film = session.get(Films, pk)
    session.delete(film)
    session.commit()
    return "Delete!"
