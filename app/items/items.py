from flask import Blueprint,request,make_response,jsonify
from app.classes.Token import Token
items_blueprint=Blueprint('items',__name__)
@items_blueprint.route('/items',methods=['GET']):
def get_items():
    token=Token()
    
    return jsonify(items)
@items_blueprint.route('/items/categories',method=['GET','POST'])
def get_categories():


@items_blueprint('/items/availabilty/<item_code>',method=['POST'])
def set_availabilty(item_code):
    token=Token()

