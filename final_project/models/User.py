from .Chore import Chore

class User():
    def __init__(self, data):
        super().__init__()
        self.id = data['id'].decode('utf-8')
        self.username = data['username'].decode('utf-8')
        self.password = data['password'].decode('utf-8')
        self.created_at = data['created_at'].decode('utf-8')
        self.updated_at = data['updated_at'].decode('utf-8')
        self.chores = []



    @classmethod
    def create_new_user(cls, db, form_data):
        query = f"""
        INSERT INTO users(username, password)
        VALUES({form_data['username']},{form_data['password']});
        """
        if cls.form_vaildation(form_data): return cls.form_vaildation(form_data)
        try:
            db.query(query)
            return {'results':True}
        except Exception as e:
            print('***ERROR: ',e)
            return {'results':False, 'data':{'error':e}}

    @classmethod
    def fetch_user_by_username(cls,db,username):
        query = f"""
        SELECT * FORM users
        LEFT JOIN chores
        ON chores.user_id = users.id
        WHERE username = {username};
        """
        try:
            db.query(query)
            store = db.store_result()
            results = store.fetch_row(1,1)
            this_user = cls(results[0])
            for row in results:
                this_user.chores.append(Chore(row))
            return {'results':True, 'data':{cls(results[0])}}
        except Exception as e:
            print('***ERROR: ',e)
            return {'results':False, 'data':{'error':e}}

    @classmethod
    def update_user(cls,db,form_data):
        query = f"""
        UPDATE users
        SET 
        username = {form_data['username']}, 
        password = {form_data['password']},
        WHERE id = {form_data['id']};
        """
        try:
            db.query(query)
            return {'results':True, 'data':{'id':form_data['id']}}
        except Exception as e:
            print('***ERROR: ',e)
            return {'results':False, 'data':{'error':e}}

    @classmethod
    def delete_user(cls,id):
        query = f"""
        DELETE FROM users
        WHERE id = {id};
        """
        try:
            db.query(query)
            return {'results':True, 'data':{'id':id}}
        except Exception as e:
            print('***ERROR: ',e)
            return {'results':False, 'data':{'error':e}}



    @staticmethod
    def form_vaildation(form_data):
        errors = {}
        if form_data['username'].decode('utf-8') <= 2:
            is_valid = False
            errors['username'] = 'Username must be at least three characters'
        if form_data['password'].decode('utf-8') <= 5:
            is_valid = False
            errors['password'] = 'Password must be at least five characters'
        return errors