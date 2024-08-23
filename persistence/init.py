from peewee import SqliteDatabase

def init_db():
    db = SqliteDatabase('ideias.db')
    db.connect()
    db.create_tables([])
    