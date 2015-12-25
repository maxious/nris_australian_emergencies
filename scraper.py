import scraperwiki
import requests
page = requests.get('https://register.redcross.org.au/_api/disaster/public').json()
print page
for disaster in page['D']:
	print disaster
	# Write out to the sqlite database using scraperwiki library
	scraperwiki.sqlite.save(unique_keys=['id'], data=disaster)
