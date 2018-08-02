# Upload files to google drive automatically after desired time.
If you have to process a file for a longer period and you are not available then just upload the results to drive automatically. Similarly, it is beneficial for other use cases too.

Link for getting access to required things : https://help.talend.com/reader/Ovc10QFckCdvYbzxTECexA/bJwFI2onuIj4YcX0VJIX7g
Remember: not to log out from your google account.

# other library requirements:
selenium
argparse
subprocess

# terminal command to run the script:
refresh_token_link help = paste the link where button to refresh token can be seen
folder_id help = id of google drive folder where file has to be uploaded(last part of opened folder url)
files help = write space separated names(path) of all file(s) to be uploaded
time help = waiting time(in sec)

```python3 zip.py refresh_token_link # folder_id # files # time #```
(replace # with required values)




