# Expload  
![image](https://github.com/user-attachments/assets/fbae4274-21d0-4233-9c96-5e19bab88488)

## what is expload
A tool for injecting magic bytes of allowed files, and spoofing the mime type. In order to exploit vulnerable file upload forms that use these as the sole validation mechanism

## useage
```
expload.py [-h] -u URL -p PAYLOAD -e EXT -n NAME -f FILENAME

expload args

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     url to upload to
  -p PAYLOAD, --payload PAYLOAD
                        path to file to upload
  -e EXT, --ext EXT     extension to spoof
  -n NAME, --name NAME  field name for file upload
  -f FILENAME, --filename FILENAME
                        file name to upload with
```
