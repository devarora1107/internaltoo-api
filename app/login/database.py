from app.database import config
global db,db_users
db=config.get_db()
db_users=db.users
def check_email_db(email):
    pass
def get_user_db(email):
    cur=db_users.find({'email':email})
    try:
        for a in cur:
            return a
    except:
        return False


def create_user_db(data):
    try:
        cur=db_users.insert(data)
    except:
        return {'message':'Error Occured inserting'}
