from wikipedia import Wikipedia
from wiki2plain import Wiki2Plain

lang = 'simple'
wiki = Wikipedia(lang)
searchString="Yuvraj Singh"
searchString = searchString.title()
try:
    
    raw = wiki.article(searchString)
except:
    raw = None

if raw:
    wiki2plain = Wiki2Plain(raw)
    content = wiki2plain.text
    conte=content.splitlines()
    content='-'.join(conte)
    conte=content.splitlines()
    print content
else: 
    print raw
