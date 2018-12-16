

import database


def get_sub_category(category):
    items=database.get_items()
    sub_category=[]
    for item in items:
        if(item['category']==category):
            if(item['sub_category'] in sub_category):
                pass
            else:
                sub_category.append(item['sub_category'])
        else:
            pass

    return sub_category
def get_categories():
    items=database.get_items()
    categories=[]
    
    for item in items:
        if(item['category'] in categories ):
            pass
        else:
            categories.append(item['category'])

    i=0
    for category in categories:
        subcategories=get_sub_category(category)
        
        sub_category=[]
        for subcategory in subcategories:
            
            objectid=database.get_subcategory_objectid(subcategory)
            if(objectid!=None):
                sub_category.append(objectid)
            else:
                
                pass
        cat={
            'title':category,
                
            'sub_category':sub_category
            }
        database.set_category(cat)
        print category
        
    return categories

print get_categories()
def get_items_cat(category,sub_category):
    items=database.get_items()
    item_list=[]
    for item in items:
        if(item['category']==category):
            if(item['sub_category']==sub_category):
                item_list.append(item)
    return item_list
def set_sub_category_db():
    categories= get_categories()
    for category in categories:
        sub_categories=get_sub_category(category)
        for sub_category in sub_categories:
            itemList=[]
            items=get_items_cat(category,sub_category)
            for item in items:
                itemList.append(item['_id'])
            data={
                'title':sub_category,
                'itemList':itemList
            }
            database.set_subcategory(data)


#set_sub_category_db()


def put_item_in_category():
    data=[]
    categories=get_categories()
    for category in categories:
        data_sub=[]
        sub_categories=get_sub_category(category)
        for sub_category in sub_categories:
            item_list=get_items_cat(category,sub_category)
            data_sub.append({sub_category:item_list})
        data.append({category:data_sub})
    return data

