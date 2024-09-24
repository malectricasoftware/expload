import argparse
def parser():
	parser = argparse.ArgumentParser(description="expload args")
	parser.add_argument("-u", "--url",required=True,help="url to upload to")
	parser.add_argument("-p", "--payload",required=True,help="path to file to upload")
	parser.add_argument("-e", "--ext",required=True,help="extension to spoof")
	parser.add_argument("-n", "--name",required=True,help="field name for file upload")
	parser.add_argument("-f", "--filename",required=True,help="file name to upload with")
	parser.add_argument("-d", "--doubleextend",action="store_true",help="spoofed extension inserted into filename")
	parser.add_argument("-h2", "--http2",action="store_true",help="use http2 if supported")
	parser.add_argument("-he", "--headers",help="headers and keys colon seperated",nargs="+")
	parser.add_argument("-c", "--cookies",help="cookies seperated by ; and wrapped in quotes")
	parser.add_argument("-r", "--response",action="store_true",help="display the response from the target webapp")
	

	args = parser.parse_args()
	if args.headers:
		args.headers={header.split(":")[0]:header.split(":")[1] for header in args.headers}
	if args.cookies:
            args.headers["cookie"]=args.cookies

	return args
