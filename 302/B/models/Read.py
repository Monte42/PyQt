from .Book import Book
from .User import User

class Read():
    def __init__(self,data):
        super().__init__()
        self.user = data['user_id'].decode('utf-8')
        self.book = data['book_id'].decode('utf-8')

    def create_new_read(self,db):
        query = f"""
        INSERT INTO user_read_books(user_id,book_id)
        VALUES({self.user},{self.book});
        """
        db.query(query)
        print('read create success')


    @classmethod
    def get_reads_by_user_or_book(cls,db,instance,id):
        query = f"""
        SELECT * 
        FROM user_read_books
        JOIN users
        ON user_read_books.user_id = users.id
        JOIN books
        ON user_read_books.book_id = books.id
        WHERE user_read_books.{instance}_id = {id}; 
        """
        db.query(query)
        store = db.store_result()
        results = store.fetch_row(0,1)
        all_returned_reads = []
        for row in results:
            this_read = cls(row)
            this_read.user = User(row)
            this_read.book = Book(row)
            all_returned_reads.append(this_read)
        return all_returned_reads


    def delete_read(self,db):
        query = f"""
        DELETE FROM user_read_books 
        WHERE user_id = {self.user}
        AND book_id = {self.book};
        """
        db.query(query)
        print('delete read success')