import time

import pyotp

def gen_key():
    return pyotp.random_base32()

def gen_url(key: str):
    return pyotp.totp.TOTP(key).provisioning_uri(name='Morpheus', issuer_name='My 2fa App')

def generate_code(key: str):
    totp = pyotp.TOTP(key)
    return totp.now()

def verify_code(key: str, code: str):
    totp = pyotp.TOTP(key)
    return totp.verify(code)

key = gen_key() #Put in Database
print(key)
uri = gen_url(key)
print(uri)

code = generate_code(key)
print(code)
time.sleep(30)
code2 = generate_code(key)

print(verify_code(key, code))
print(verify_code(key, code2))