import tempfile
from pyfsig import constants
import httpx
import mimetypes
import exploadlib.parse
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
        with httpx.Client(http2=args.http2) as client:

            try:
                r = client.post(args.url, files=files)

            except httpx.ReadTimeout:
                print("Error: Response timed out but file may have been uploaded")
                exit()

            except httpx.RemoteProtocolError:
                print("Error: Server disconnected without sending a response") 
                exit()

            except httpx.ConnectError:
                print("Error: Connection refused") 
                exit()

        print("file posted")      

if __name__ == "__main__":
    args=exploadlib.parse.parser()
    fileupload()
