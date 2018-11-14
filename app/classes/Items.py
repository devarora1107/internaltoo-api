class Items():
    def __init__(self,categories,subcat):
        self.__categories=categories
        self.__subCat=subCat
        self.__catId=None
        self.__subCatId=None
    def get_categories(self):
        return self.__categories
    def set_categories(self,categories):
        self.__categories=categories
    def get_subcat(self):
        return __self.__sub_cat
    def set_subcat(self,subcat):
        self.__sub_cat=subcat
    def get_items(self):
        cat=self.get_categories()
        subcat=self.get_subcat()
        items=[]
        from app.items import database
        database.get_items(self.get_categories(),self.get_subcat())

