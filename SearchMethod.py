from wikipedia import Wikipedia
from wiki2plain import Wiki2Plain
class SearchMethod:
    def __init__(self, wiki):
        
        self.wiki = wiki
        self.text = wiki
        self.text = self.article(self.text)
   
    def __str__(self):
        return self.text

    def article(self, article):
        lang = 'simple'
	wiki = Wikipedia(lang)
	searchString=article

	try:
    
    		raw = wiki.article(searchString)
	except:
    		raw = None

	if raw:
    		wiki2plain = Wiki2Plain(raw)
    		content = wiki2plain.text
    		print content
	else: 
    		content=raw
        
        return content


