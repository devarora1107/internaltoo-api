from app.database import config
global db,db_users
db=config.get_db()
db_users=db.users

def get_user_db(email):
    cur=db_users.find({'email':email})
    try:
        for a in cur:
            return a
    except:
        return False


