from app.database import config
global db,db_items
db=config.get_db()
db_items=db.items

def get_cat_id(self,cat_name):
    return id
def get_items(cat,subcat):
    pass
def insert_csv_items():
    print db_items.insert({'hello':'hello'})
    import unicodecsv
    with open('products.csv') as products:
        reader=unicodecsv.reader(products,encoding='utf-8-sig',delimiter=',')
        i=0
        header=[]
        items=[]
        
        for row in reader:
            if(i==0):
                for field in row:
                    header.append(field)
                print header

            else:
                i=0
                item={}
                code='PAT00'+str(i)
                for field in row:
                    item[header[i]]=field
                    i=i+1
                items.append(item)
                
            i=i+1
    for item in items:
        item['available']=1     #1 for true 0 for false
        db_items.insert(item)


insert_csv_items()