import pysftp

cnopts = pysftp.CnOpts(knownhosts='files/known_hosts')
with pysftp.Connection('host', port=22, username='demo', password='password', cnopts=cnopts) as sftp:
    print(sftp.listdir())

with pysftp.Connection('host', port=22, username='morpheus', private_key=r'C:\Users\mykey.priv', private_key_pass='password') as sftp:
    print(sftp.listdir())