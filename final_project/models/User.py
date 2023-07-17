from .Chore import Chore
from utils.general import decode_model

class User():
    def __init__(self, data):
        super().__init__()
        self.id = data['id']
        self.username = data['username']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['update_at']
        self.chores = []



    @classmethod
    def create_new_user(cls, db, form_data):
        query = f"""
        INSERT INTO users(username, password,is_admin)
        VALUES('{form_data['username']}','{form_data['password']}','{form_data['is_admin']}');
        """
        if cls.form_vaildation(form_data):
            data = {'errors':cls.form_vaildation(form_data)}
            data['status'] = False
            return data
        try:
            db.query(query)
            return {'status':True}
        except Exception as e:
            print('***ERROR: ',e)
            return {'status':False, 'data':{'error':e}}

    @classmethod
    def fetch_all_users(cls,db):
        query = 'SELECT username FROM users;'
        try:
            db.query(query)
            store = db.store_result()
            results = store.fetch_row(0,1)
            return results
        except Exception as e:
            print('***ERROR: ',e)
            return {'status':False, 'data':{'error':e}}

    @classmethod
    def fetch_user_by_username(cls,db,username):
        query = f"""
        SELECT * FROM users
        LEFT JOIN chores_on_users as chores
        ON chores.user_id = users.id
        WHERE username = '{username}';
        """
        try:
            db.query(query)
            store = db.store_result()
            results = store.fetch_row(1,1)
            this_user = cls(decode_model(results[0]))
            for row in results:
                this_user.chores.append(Chore(row))
            return {'status':True, 'data': cls(decode_model(results[0]))}
        except Exception as e:
            print('***ERROR: ',e)
            return {'status':False, 'data':{'error':e}}

    @classmethod
    def update_user(cls,db,form_data):
        query = f"""
        UPDATE users
        SET 
        username = '{form_data['username']}', 
        password = '{form_data['password']}'
        WHERE id = {form_data['id']};
        """
        if cls.form_vaildation(form_data):
            data = {'errors':cls.form_vaildation(form_data)}
            data['status'] = False
            return data
        try:
            db.query(query)
            return {'status':True, 'data':{'id':form_data['id']}}
        except Exception as e:
            print('***ERROR: ',e)
            return {'status':False, 'data':{'error':e}}

    @classmethod
    def delete_user(cls,db,username):
        query = f"""
        DELETE FROM users
        WHERE username = '{username}';
        """
        try:
            db.query(query)
            return {'status':True, 'data':{'username':username}}
        except Exception as e:
            print('***ERROR: ',e)
            return {'status':False, 'data':{'error':e}}



    @staticmethod
    def form_vaildation(form_data):
        errors = []
        if len(form_data['username']) <= 2:
            is_valid = False
            errors.append('** Username must be at least three characters')
        if len(form_data['password']) < 5:
            is_valid = False
            errors.append('** Password must be at least five characters')
        return errors