from utils.general import decode_model

class Chore():
    def __init__(self, data):
        super().__init__()
        self.chore_id = data['id']
        self.due_date = data['due_date']
        self.comment = data['comment']
        self.user = data['user_id']
        self.task = data['task_id']



    @classmethod
    def create_new_chore(cls,db,form_data):
        query = f"""
        INSERT INTO chores_on_users(due_date,comment,user_id,task_id)
        VALUES({form_data['due_date']},{form_data['comment']},{form_data['user_id']},{form_data['task_id']});
        """
        try:
            db.query(query)
            return {'results':True}
        except Exception as e:
            print('***ERROR: ',e)
            return {'results':False, 'data':{'error':e}}

    @classmethod
    def fetch_chores_by_userId(cls,db,user_id):
        query = f"""
        SELECT * FROM chores_on_users
        WHERE user_id = {user_id};
        """
        try:
            db.query(query)
            store = db.store_result()
            results = store.fetch_row(0,1)
            all_chores = []
            for row in results:
                row = decode_model(row)
                this_chore = cls(row)
                all_chores.append(this_chore)
            return {'results':True, 'data':all_chores}
        except Exception as e:
            print('***ERROR: ',e)
            return {'results':False, 'data':{'error':e}}

    @classmethod
    def update_chore(cls,db,form_data):
        query = f"""
        UPDATE chores_on_users
        SET
        due_date = {form_data['due_date']},
        comment = {form_data['comment']},
        user_id = {form_data['user_id']},
        task_id = {form_data['task_id']}
        WHERE id = {form_data['id']}
        """
        try:
            db.query(query)
            return {'results':True, 'data':{'id':form_data['id']}}
        except Exception as e:
            print('***ERROR: ',e)
            return {'results':False, 'data':{'error':e}}

    @classmethod
    def delete_chore(cls,db,id):
        query = f"""
        DELETE FROM chores_on_users
        WHERE id = {id};
        """
        try:
            db.query(query)
            return {'results':True, 'data':{'id':id}}
        except Exception as e:
            print('***ERROR: ',e)
            return {'results':False, 'data':{'error':e}}