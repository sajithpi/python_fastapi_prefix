from main import User, Profile, Account, Session, engine,exc,desc


class create_users:
    def __init__(self):
        self.local_session = Session(bind=engine)
    def add_user(self):
        try:
            self.username = input("Enter the username:")
            self.email = input("Enter the email id:")
            self.new_user = User(username=self.username,email=self.email)
        # Adding user details into user
            self.local_session.add(self.new_user)
        # Getting the newly inserted user id
            self.new_id = self.local_session.query(User).order_by(desc(User.id)).first()
            print("new id:",self.new_id.id)
        # inserting into profile table
            self.sponser_id = int(input("Enter your sponser user id:"))
            self.address = input("Enter your address:")
            self.user_profile = Profile(user_id=self.new_id.id, sponser_id=self.sponser_id,address = self.address)
            self.local_session.add(self.user_profile)
            
        #calculating amount for the sponser and adding into amount table
            self.amount_table_result = self.local_session.query(Account).filter(Account.user_id == self.sponser_id).first()
        
            if self.amount_table_result:
                self.amount_table_result.balance = self.amount_table_result.balance + 1000
            else:
                self.amount_table_result = Account(user_id=self.sponser_id,balance=1000)
                self.local_session.add(self.amount_table_result)
            
        # self.user_amount = Amount (user_id = self.sponser_id, balance = )
        
        
        
        
            self.local_session.commit()
        except exc.SQLAlchemyError as error:
            print("Error",error)


    def show_user(self):
        self.user = self.local_session.query(User).first()
        print("username:",self.user.username)
ob1 = create_users()
# ob1.add_user()
ob1.show_user()