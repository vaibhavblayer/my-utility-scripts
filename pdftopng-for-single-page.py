import sys
import itertools
import pdf2image

file = sys.argv[1]
outputfile = sys.argv[2]

pages = pdf2image.convert_from_path("./{}".format(file), dpi=320)

for page in pages:
	page.save('{0}.png'.format(outputfile), 'PNG')
