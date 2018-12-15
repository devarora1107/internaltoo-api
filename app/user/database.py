from app.database import config
global db, db_users

db=config.get_db()
db_users=db.db_users


def create_user_db(data):
    
    try:
        cur=db_users.insert(data)
    except:
        return False
