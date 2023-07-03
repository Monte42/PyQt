from models.User import User

class UserController():

    # CREATE
    def create_new_user(db,new_user):
        return User.create_new_user(db,new_user)

    # READ
    @staticmethod
    def get_all_users(db):
        return User.fetch_all_users(db)
    @staticmethod
    def get_user_by_username(self,username):
        return User.fetch_user_by_username(self.db, username)

    # UPDATE
    def update_user(db,updated_user):
        return User.update_user(db,updated_user)

    # DELETE
    def delete_user(self,id):
        return User.delete_user(id)
