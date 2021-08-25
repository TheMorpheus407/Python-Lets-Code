import ftplib
import os
from datetime import datetime

FTP_HOST = ""
FTP_USER = ""
FTP_PASS = ""

def get_size(n, suffix="B"):
    for u in ["", "K", "M", "G", "T", "P"]:
        if n < 1024:
            return f"{n:.3f}{u}{suffix}"
        n /= 1024

def save_file_binary(data):
    with open("out.pdf", "ab") as out:
        out.write(data)

ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
ftp.encoding = "utf-8"
print(ftp.getwelcome())
home = "/"

ftp.dir()
ftp.cwd(home)
dirs = []
files = []
for d in ftp.nlst():
    if d == "." or d == "..":
        continue
    try:
        ftp.cwd(d)
        dirs.append(d)
        print(f"Success: {d}")
    except:
        files.append(d)
        print(f"Error: {d}")
    ftp.cwd(home)

print(files)
print(dirs)

if len(files) > 0:
    ftp.retrbinary(f'RETR {files[0]}', save_file_binary)

upload_file = open(r"G:\Tuts\Archive\Python LetsCodes\files\1984_image.PNG", "rb")
ftp.storbinary("STOR 1984_image.PNG", upload_file)
upload_file.close()

ftp.quit()











