from pymongo import MongoClient


def connect_db():
    # client = MongoClient('localhost', 27018)
    client = MongoClient('mongodb://notesmongo:password@localhost:27018/')
    db = client.UserNotes
    return db


db = connect_db()


def user_input(user:str, note:str, db=db):
    try:
        collection = db['StoredNotes']
        collection.insert_one({'user': user, 'note': note})
        return True
    except:
        return False


def give_me_my_notes(user:str=None, note:str=None, db=db):

    try:
        collection = db['StoredNotes']
        criteria = {}
        if user:
            criteria['user'] = user
        if note:
            criteria['note'] = note
        cur = collection.find(criteria)
        dbnotes = []
        for dict in cur:
            dbnotes.append(dict)
        return dbnotes

    except:
        return False

def clean_thiss_mess_up(db=db):
    collection = db['StoredNotes']
    collection.drop()







