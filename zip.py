# waiting time = 5000 seconds
import time
time.sleep(5000)

import json
import requests
from selenium import webdriver
import time
from subprocess import call
import argparse

parser = argparse.ArgumentParser(description='automatic files upload')
parser.add_argument('refresh_token_link', help='paste the link where button to refresh token can be seen')
parser.add_argument('folder_id', help='id of google drive folder where file has to be uploaded')
parser.add_argument('files', help='write space separated names(path) of all file(s) to be uploaded')
args = parser.parse_args()


browser = webdriver.Firefox() # or chrome()
browser.get(args.refresh_token_link)

browser.find_element_by_id('refreshAccessToken').click()
token = browser.find_elements_by_tag_name('span.str')[1].text[1:-1]

#compress all the files to be uploaded to a single file called compressed.zip
# or if you don't want to upload multiple files then just comment next 2 lines and change the filename(next 3rd line) accordingly
command = "tar -czvf compressed.zip " + args.files
call(command, shell=True)

headers = {"Authorization": "Bearer " + str(token)}
para = {
    "name": "compressed.zip",
    "parents": [args.folder_id]
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("./compressed.zip", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)

