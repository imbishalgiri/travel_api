from app import mysql
from app.models.utils import encrypt_password, verify_encrypted_password





def add_user(firstName, lastName, email,  password):
    cur = mysql.connection.cursor()
    cur.execute("insert into users (first_name, last_name, email, password) values(%s, %s, %s, %s)",(firstName, lastName, email, encrypt_password(password)));
    mysql.connection.commit()
    cur.close()
    return True;


def get_single_user(email):
    cur = mysql.connection.cursor()
    cur.execute("select * from users where email = %s", (email,))
    user = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    if user:
        return user
    return False

def verify_password(email, password):
    cur = mysql.connection.cursor()
    cur.execute("select password from users where email = %s",(email,))
    db_pass = cur.fetchone()
    mysql.connection.commit()
    
    cur.close()
    if db_pass and verify_encrypted_password(str(db_pass[0]), password):
        return True
    return False




# TODO --> make a separate function for wrapping cursor extra codes 
# this is a simple approach to work on that -->

# ------------------------------------------ function
# def jello(func):
    
#     def get_name(*args):
#         print('hey there')
#         func(*locals()['args'])
#     return get_name

# def my_name(f, l):
#     print (f + l)
    
# cool_name = jello(my_name)
# cool_name('jane', 'miller')
# -------------------------------------------- endFunction


