from main import User,Session,engine,Profile
from sqlalchemy import desc
import numpy as np
import time
local_session = Session(bind=engine)

    
# filtering
count = local_session.query(User).order_by(desc(User.id)).first()
count = count.id
print("count:",count)


def get_data(val):
    if val==count:
        return 1
    else:
        result = local_session.query(User).filter(User.id==val).first()
        print(result.username)
        val = val + 1
        return get_data(val)
def get_details(val):
    # if val == count:
    #     return 1
    # else:
        result = local_session.query(User).join(Profile).filter(User.id==val, User.username == 'selin', Profile.sponser_id==3).all()
        # print(result.user.id)
        for user in result:
            for profile in user.child:
                print("id:",user.id,profile.sponser_id,user.username)
        # print(result)
        # return get_details(val)


def get_user():
    start = time.time()
    arr1 = np.array([])
    arr1 = np.append(arr1,{'name':'sajith'})
    result = local_session.query(User).all()
    for user in result:
        users = {}
        users = {'id':user.id,
                'name':user.username}
        arr1 = np.append(arr1, users)
    # print("user name:",result.username)
    time.sleep(1)

    print(arr1)
    end = time.time()
    print("Time taken for to calculate using numpy:",end-start)

def get_user_list():
    start = time.time()
    arr1 = []
    result = local_session.query(User).all()
    for user in result:
        users = {}
        users = {'id':user.id,
                'name':user.username}
        arr1.append(users)
    # print("user name:",result.username)
    time.sleep(1)

    print(arr1)
    end = time.time()
    print("Time taken for to calculate using list:",end-start)

get_user()
get_user_list()

