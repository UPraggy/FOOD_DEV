from order import * #create, status, update, select, cancel 
from client import * #create, select, update, delete

order = Order_functions()
client = Client_functions()

def mod_order(app, option, type_user):
    if (option  == 'create'):
        order.create()
    elif (option  == 'status'):
        order.status(app)
    elif (option  == 'update'):
        order.update(app)
    elif (option  == 'select'):
        order.select(app)
    elif (option  == 'cancel'):
        order.cancel(app)

def mod_client(app, option, type_user):
    if (option  == 'create'):
        client.create(app)
    elif (option  == 'status'):
        client.status(app)
    elif (option  == 'update'):
        client.update(app)
    elif (option  == 'select'):
        client.select(app)
    elif (option  == 'cancel'):
        client.cancel(app)