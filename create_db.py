from model import User
from main import Base, engine

Base.metadata.create_all(engine)