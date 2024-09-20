import argparse
def parser():
	parser = argparse.ArgumentParser(description="expload args")
	parser.add_argument("-u", "--url",required=True,help="url to upload to")
	parser.add_argument("-p", "--payload",required=True,help="path to file to upload")
	parser.add_argument("-e", "--ext",required=True,help="extension to spoof")
	parser.add_argument("-n", "--name",required=True,help="field name for file upload")
	parser.add_argument("-f", "--filename",required=True,help="file name to upload with")

	args = parser.parse_args()
	return args