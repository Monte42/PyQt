from .Author import Author

class Book:
    def __init__(self,data):
        self.id = data['id'].decode('utf-8')
        self.title = data['title'].decode('utf-8')
        self.pages = data['pages'].decode('utf-8')
        self.author = None
        self.created_at = data['created_at'].decode('utf-8')
        self.updated_at = data['updated_at'].decode('utf-8')

    def display_full_data(self):
        data = f"""
        BOOK ID# {self.id}
        TITLE: {self.title}
        AUTHOR: {self.author.return_full_name()}
        NUMBER OF PAGES: {self.pages}
        DATE ADDED: {self.created_at}
        """
        return data


    # CLASS METHODS
    @classmethod
    def create_new_book(cls,db,form_data):
        query = f"""
        INSERT INTO books(author_id,title,pages)
        VALUES({form_data['author_id']},"{form_data['title']}",{form_data['pages']});
        """
        print(query)
        db.query(query)


    @classmethod
    def fecth_all_books(cls, db):
        query = """
        SELECT *
        FROM books
        JOIN authors
        ON books.author_id = authors.id
        ORDER BY books.id;
        """
        db.query(query)
        store = db.store_result()
        results = store.fetch_row(0,1)
        all_books = []
        for row in results:
            this_book = cls(row)
            this_author = {
                'id': row['authors.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'created_at': row['authors.created_at'],
                'updated_at': row['authors.updated_at'],
            }
            this_book.author = Author(this_author)
            all_books.append(this_book)
        return all_books