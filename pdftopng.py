import sys
import itertools
import pdf2image



input_path = str(input('Where pdf is located -> path : '))
out_path = str(input('Where you want images to be saved -> path : '))
dpi = input('dpi -> 72/144/320 : ')
image_name = input('Image name -> string part : ')
first_page = int(input('Starting page -> integer : '))
last_page = int(input('Last page -> integer : '))

page_number = itertools.count(first_page)


#input_path = '/Users/vaibhavblayer/python.pdf'
#output_path = '/Users/vaibhavblayer/images/'

pages = pdf2image.convert_from_path(input_path, dpi=dpi, first_page=first_page, last_page=last_page)

for page in pages:
	page.save('{0}{1}.png'.format(image_name, str(next(page_number)).zfill(2)), 'PNG')
