from main import User,Session,engine,exc
class update_users:
    def __init__(self):
        
        # Using sessions for update operation and bind for connecting with engine
        
        self.local_session = Session(bind=engine)
    def update_user(self):
        try:
    
            self.user_id = input("Enter the user id to update:")

            self.user_to_update = self.local_session.query(User).filter(User.id == self.user_id).first()
            if self.user_to_update:
                self.user_to_update.username = input("Enter your new username:")
                self.user_to_update.email = input("Enter your email:")

                self.local_session.commit()
                print("Successfully updated user")
            else:
                print("User Does't exist")
        except exc.IntegrityError as e:
            print("Error")
            self.errorInfo = e.orig.args
            print(self.errorInfo[0])  #This will give you error code
            print(self.errorInfo[1])  #This will give you error message
            self.local_session.rollback()

ob1 = update_users()
ob1.update_user()