
class Author:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.books = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def return_full_name(self):
        return f'{self.first_name.decode("utf-8")} {self.last_name.decode("utf-8")}'

    def display_full_data(self):
        data = f"""
        AUTHOR ID# {self.id.decode("utf-8")}
        NAME: {self.first_name.decode("utf-8")} {self.last_name.decode("utf-8")}
        BOOKS WRITTEN:
        """
        for book in self.books:
            data += f' -- {book["title"].decode("utf-8")}'
        return data



    @classmethod
    def fecth_all_authors(cls,db):
        query = f"""
        SELECT * 
        FROM authors
        LEFT JOIN books
        ON authors.id = books.author_id
        ORDER BY authors.id;
        """
        db.query(query)
        store = db.store_result()
        results = store.fetch_row(0,1)
        all_authors = []
        current_author_id = 0
        for row in results:
            book = {
                'id': row['books.id'],
                'title': row['title'],
                'pages': row['pages']
            }
            if row['id'] == current_author_id:
                all_authors[-1].books.append(book)
            else:
                current_author_id = row['id']
                all_authors.append(cls(row))
                if book['id']:
                    all_authors[-1].books.append(book)
        return all_authors