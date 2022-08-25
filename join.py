from main import User, Profile, Account, engine, Session, exc

class Joining:
    def __init__(self):
        self.local_session = Session(bind=engine)
        print("ID\t USERNAME\t ADDRESS\t BALANCE")
    def Join_Table(self):
        for u, p, a in self.local_session.query(User, Profile,Account).filter(User.id == Profile.user_id,User.id == Account.user_id).all():
            print (u.id,u.username, p.address, a.balance)
            
            
ob1 = Joining()
ob1.Join_Table()