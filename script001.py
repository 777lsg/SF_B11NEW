import hashlib
import requests
import subprocess


def calculate_md5(file_path):
    with open(file_path, 'rb') as file:
        md5_hash = hashlib.md5()
        while chunk := file.read(4096):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()


nginx_url = 'http://127.0.0.1:9889/index.html'
local_file_path = '/tmp/index.html'


response = requests.get(nginx_url)
nginx_file_content = response.content


local_file_md5 = calculate_md5(local_file_path)


nginx_file_md5 = hashlib.md5(nginx_file_content).hexdigest()


if local_file_md5 == nginx_file_md5:
    print("MD5 суммы совпадают.")
else:
    print("MD5 суммы не совпадают.")
    curl_command = ['curl', 'https://api.telegram.org/bot<token>/sendMessage?chat_id=<chatid>=MD5_суммы_не_совпадают']
    subprocess.call(curl_command)
