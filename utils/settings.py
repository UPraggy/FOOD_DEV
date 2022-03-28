from template import *
order = Order()
client = Client()
product = Product()

def mod_order(app, option, type_user):
    if (option  == 'create'):
        order.create(app)
    elif (option  == 'status'):
        order.status(app)
    elif (option  == 'update'):
        order.update(app)
    elif (option  == 'select'):
        order.select(app)

def mod_client(app, option, type_user):
    if (option  == 'create'):
        client.create(app)
    elif (option  == 'update'):
        client.update(app)
    elif (option  == 'select'):
        client.select(app)
    elif (option  == 'cancel'):
        client.cancel(app)

def mod_product(app, option, type_user):
    if (option  == 'create'):
        product.create(app)
    elif (option  == 'update'):
        product.update(app)
    elif (option  == 'select'):
        product.select(app)
    elif (option  == 'cancel'):
        product.cancel(app)
