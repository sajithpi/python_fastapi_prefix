from main import User, Session, engine
from sqlalchemy import desc

local_session = Session(bind=engine)

# # Ascending
# users = local_session.query(User).order_by(User.username).all()

# Descending
users = local_session.query(User).order_by(desc(User.username)).all()

for user in users:
    print(f"User : {user.username} Email: {user.email}")