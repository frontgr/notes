from pymongo import MongoClient
from AES_Encrypt_Decrypt import DataProtection
from os import getenv


class Database:
    def __init__(self):
        mongo_user = getenv("MONGO_INITDB_ROOT_USERNAME")
        mongo_password = getenv("MONGO_INITDB_ROOT_PASSWORD")
        mongo_location = getenv("APP_DB_LOCATION")
        client = MongoClient(f'mongodb://{mongo_user}:{mongo_password}@{mongo_location}/')
        self.db = client.UserNotes
        self.aes = DataProtection()

    def user_input(self, content: tuple):
        try:
            collection = self.db['StoredNotes']
            very_secret_collection = self.db['UserKeys']

            last_element = collection.find_one(sort=[('id', -1)])
            id = last_element['id'] + 1 if last_element else 1
            stored_content = collection.insert_one({'id': id, 'content': content[0]}).inserted_id
            very_secret_collection.insert_one({'stored_content': stored_content, 'user_key': content[1], 'nonce': content[2]})
            return True

        except:
            return False

    def give_me_my_notes(self):
        try:
            collection = self.db['StoredNotes']
            very_secret_collection = self.db['UserKeys']

            cur = collection.find()
            db_notes = []

            for d in cur:
                vsc_instance = very_secret_collection.find_one({'stored_content': d['_id']})
                key = vsc_instance['user_key']
                nonce = vsc_instance['nonce']
                note_to_decrypt = d['content']
                d['content'] = self.aes.aes_decryption(note_to_decrypt, key, nonce)
                d.pop('_id')
                db_notes.append(d)
            return db_notes

        except Exception:
            return False

    def clean_this_mess_up(self):
        try:
            collection = self.db['StoredNotes']
            collection.drop()
            return True
        except:
            return False







