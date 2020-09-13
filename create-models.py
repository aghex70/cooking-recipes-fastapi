import database
from models import Recipe


def run():
    pass

if __name__ == '__main__':
    database.Base.metadata.create_all(database.engine)
    run()