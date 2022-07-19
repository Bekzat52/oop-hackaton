from views import *
urlpatterns = [
    ('product-retrieve/id', retrieve), 
    ('product-create/', product_create), 
    ('product-list/', product_list),
    ('product-update/id', product_update),
    ('product-delete/id', product_delete),
]