from main import User, Session, engine
class delete_user:
    
    def __init__(self):
        self.local_session = Session(bind=engine)

    def delete_user(self):
        try:
            self.user_id = int(input("Enter the user id for delete:"))
            self.user_to_delete = self.local_session.query(User).filter(User.id==self.user_id).first()
            if self.user_to_delete:
                self.local_session.delete(self.user_to_delete)
                self.local_session.commit()
                print("Deleted Successfully")
            else:
                print("User Does't Exist")
        except:
            self.local_session.rollback()
            print("Not Deleted")
        
ob1 = delete_user()
ob1.delete_user()