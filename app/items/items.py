from flask import Blueprint,request,make_response,jsonify
from app.classes.Token import Token
items_blueprint=Blueprint('items',__name__)
@items_blueprint.route('/items',methods=['GET'])
def get_items():
    token=Token()
    user=token.verify_token()
    if(user):
        pass
    else:
        return {'message':'token problem'}
    
    return jsonify(items)
@items_blueprint.route('/items/itemList',methods=['GET','POST'])
def get_categories():

    list=[]
    return 


@items_blueprint.route('/items/availabilty/<item_code>',methods=['POST'])
def set_availabilty(item_code):
    token=Token()

