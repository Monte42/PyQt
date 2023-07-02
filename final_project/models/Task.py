
class Task():
    def __init__(self,data):
        super().__init__()
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @classmethod
    def create_new_task(cls,db,form_data):
        query = f"""
        INSERT INTO tasks(title,description)
        VALUES({form_data['title']},{form_data['description']});
        """
        try:
            db.query(query)
            return {'results':True}
        except Exception as e:
            print('***ERROR: ',e)
            return {'results':False, 'data':{'error':e}}

    @classmethod
    def fetch_task_by_id(cls,db,id):
        query = f"""
        SELECT * FROM tasks
        WHERE id = {id};
        """
        try:
            db.query(query)
            store = db.store_result()
            results = store.fetch_row(1,1)
            return {'results':True, 'data': cls(results[0])}
        except Exception as e:
            print('***ERROR: ',e)
            return {'results':False, 'data':{'error':e}}

    @classmethod
    def update_task(cls,db,form_data):
        query = f"""
        UPDATE tasks
        SET 
        title={form_data['title']},
        description={form_data['description']}
        WHERE id = {form_data['id']};
        """
        try:
            db.query(query)
            return {'results':True, 'data':{'id':form_data['id']}}
        except Exception as e:
            print('***ERROR: ',e)
            return {'results':False, 'data':{'error':e}}

    @classmethod
    def delete_task(cls,db,id):
        query = f"""
        DELETE FROM tasks
        WHERE id = {id};
        """
        try:
            db.query(query)
            return {'results':True, 'data':{'id':id}}
        except Exception as e:
            print('***ERROR: ',e)
            return {'results':False, 'data':{'error':e}}


