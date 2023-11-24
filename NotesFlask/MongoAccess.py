from pymongo import MongoClient


def __connect_db():

    client = MongoClient('mongodb://notesmongo:password@mongo/')
    db = client.UserNotes
    return db


def user_input(content:str, db=__connect_db()):

    try:
        collection = db['StoredNotes']
        lastelement = collection.find_one(sort=[('id', -1)])

        if lastelement:
            collection.insert_one({'id': lastelement['id'] + 1, 'content': content})
        else:
            collection.insert_one({'id': 1, 'content': content})
        return True

    except:
        return False


def give_me_my_notes(id:int=None, content:str=None, db=__connect_db()):

    try:
        collection = db['StoredNotes']
        criteria = {}

        if id:
            criteria['id'] = id
        if content:
            criteria['content'] = content

        cur = collection.find(criteria, {'_id': 0})
        dbnotes = []

        for dict in cur:
            dbnotes.append(dict)

        return dbnotes

    except:
        return False


def clean_this_mess_up(db=__connect_db()):

    collection = db['StoredNotes']
    collection.drop()








