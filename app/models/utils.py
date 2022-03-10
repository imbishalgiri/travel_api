from passlib.hash import sha256_crypt

# To encrypt the provided password
def encrypt_password(password):
    return sha256_crypt.encrypt(password)

# comparison of hashed password with plane password
# @params:
#     db_pass --> hashed password
#     user_pass --> password from form input

def verify_encrypted_password(db_pass, user_pass):
    return sha256_crypt.verify(user_pass, db_pass)
	