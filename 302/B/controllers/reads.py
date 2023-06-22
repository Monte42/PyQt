from models.Read import Read

class ReadController():


    def fetch_reads(self,instance,id):
        readers = "Who's read this book:\n"
        reads = Read.get_reads_by_user_or_book(self.db,instance,id)
        for read in reads:
            readers += f'   {read.user.username.decode("utf-8")}\n'
        return readers