from wikipedia import Wikipedia
from wiki2plain import Wiki2Plain

lang = 'en'
wiki = Wikipedia(lang)
searchString="shahrukh khan"
searchString = searchString.title()
try:
	raw = wiki.article(searchString)
except:
    	raw = None


if raw:
    	wiki2plain = Wiki2Plain(raw)
        content = wiki2plain.text
else: 
    	content= "Sun, abhi football practice ko jaana aake bolta! "
print content
