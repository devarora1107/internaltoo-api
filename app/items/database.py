#from app.database import config
global db,db_items,db_category,db_subcategory

def get_db():
    from pymongo import MongoClient
    client=MongoClient('localhost:27017')
    db=client.internaltool
    return db
db=get_db()
db_items=db.items
db_category=db.category
db_subcategory=db.subcategory

def get_category():
    categories=[]
    cur=db_category.find()
    try:
        for cat in cur:
            categories.append(cat)
    except:
        return []
    return categories

def set_category(category):
    cat_id='CAT00'+str(len(get_category())+1)
    category['cat_id']=cat_id
    db_category.insert(category)


def get_subcategory_objectid(subcategory):
    cur=db_subcategory.find({'title':subcategory})
    
    try:
        for data in cur:
            return data['_id']

    except:
        return None


def get_subcategory():
    subcategories=[]
    cur=db_subcategory.find()
    try:
        for subcat in cur:
            subcategories.append(subcat)
    except:
        return []

    return subcategories

def set_subcategory(subcategory):
    sub_cat_id='SCAT00'+str(len(get_subcategory())+1)
    subcategory['subcat_id']=sub_cat_id
    db_subcategory.insert(subcategory)
def get_items():
    cur=db_items.find()
    items=[]
    for item in cur:
        items.append(item)

    return items

def insert_csv_items():
    
    import unicodecsv
    with open('products.csv') as products:
        reader=unicodecsv.reader(products,encoding='utf-8-sig',delimiter=',')
        i=0
        header=[]
        items=[]
        j=0
        for row in reader:
            j+=1
            if(i==0):
                for field in row:
                    header.append(field)
                print header

            else:
                i=0
                item={}                                                                                                                                                                                                 
                
                for field in row:
                    code='PAT00'+str(j)
                    item[header[i]]=field
                    item['code']=code
                    
                    i=i+1
                items.append(item)
                
                
            i=i+1
    for item in items:
        item['available']=True
        item.pop("")   #1 for true 0 for false
        db_items.insert(item)


