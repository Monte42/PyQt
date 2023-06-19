from .Author import Author

class Book:
    def __init__(self,data):
        self.id = data['id'].decode('utf-8')
        self.title = data['title'].decode('utf-8')
        self.page = data['page'].decode('utf-8')
        self.author = None
        self.created_at = data['created_at'].decode('utf-8')
        self.updated_at = data['updated_at'].decode('utf-8')




    # CLASS METHODS
    @classmethod
    def fecth_all_books(self, db):
        pass