from pymongo import MongoClient


def __connect_db():
    client = MongoClient('mongodb://notesmongo:password@mongo/')
    db = client.UserNotes
    return db


def user_input(content: tuple, db=__connect_db()):
    try:
        collection = db['StoredNotes']
        very_secret_collection = db['UserKeys']

        last_element = collection.find_one(sort=[('id', -1)])
        id = last_element['id'] + 1 if last_element else 1
        stored_content = collection.insert_one({'id': id, 'content': content[0]}).inserted_id
        very_secret_collection.insert_one({'stored_content': stored_content, 'user_key': content[1], 'nonce': content[2]})
        return True

    except:
        return False


def give_me_my_notes(db=__connect_db()):
    from AES_Encrypt_Decrypt import aes_decryption
    try:
        collection = db['StoredNotes']
        very_secret_collection = db['UserKeys']

        cur = collection.find()
        db_notes = []

        for d in cur:
            vsc_instance = very_secret_collection.find_one({'stored_content': d['_id']})
            key = vsc_instance['user_key']
            nonce = vsc_instance['nonce']
            note_to_decrypt = d['content']
            d['content'] = aes_decryption(note_to_decrypt, key, nonce)
            d.pop('_id')
            db_notes.append(d)
        return db_notes

    except Exception:
        return False


def clean_this_mess_up(db=__connect_db()):
    collection = db['StoredNotes']
    collection.drop()








