from database import db, Usuario, Anuncio

db.connect()

db.create_tables([Usuario, Anuncio])