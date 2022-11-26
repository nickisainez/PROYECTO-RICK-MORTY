from flask import Blueprint, render_template, redirect, url_for
from app.models.profiles import Personaje
from app.db import db
import requests

personajes_ruta = Blueprint("personajes_ruta",__name__)

@personajes_ruta.route("/")
def index():
    personajes = db.personajes.aggregate([{"$sort":{"id":-1}}])
    print(personajes)
    return render_template("index.html",personajes=personajes)

@personajes_ruta.route("/insert")
def guardar_personaje():
    for pagina in range(1,22):
        url = 'https://rickandmortyapi.com/api/character?page='+ str(pagina)
        r_perfil = requests.get(url)
        newp = r_perfil.json()
        newp = newp["results"]

        for pj in newp:
            new_p = Personaje(
                pj['id'],
                pj['name'],
                pj['status'],
                pj['species'],
                pj['gender'],
                pj['origin']['name'],
                pj['location']['name'],
                pj['image'],
                pj['created']
            )
                      
        db.personajes.insert_one(new_p.to_json())
    
    return redirect(url_for("personajes_ruta.index"))

@personajes_ruta.route("/<int:id>")
def detalle_perfiles(id):
    uniqe = db.personajes.find_one({'id':id})
    
    return render_template("detalle_perfiles.html",uniqe=uniqe)