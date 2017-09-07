from flask import Flask
from flask import Flask, render_template,json, request
from wikipedia import Wikipedia
from wiki2plain import Wiki2Plain
from flask import jsonify
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def main():
     return render_template('index.html')

@app.route('/test',methods=['POST'])
def test():
    lang = 'en'
    wiki = Wikipedia(lang)
    searchString=request.json["yourname"]
    searchString = searchString.title()
    with open("SearchData.txt", "a") as myfile:
    	myfile.write(searchString+ "\n")
    try:
      	raw = wiki.article(searchString)
    except:
    	raw = None
    if raw:
    	wiki2plain = Wiki2Plain(raw)
        content = wiki2plain.text
    else: 
    	content= "Sun, abhi football practice ko jaana aake bolta! "

    if "Akshat" in  searchString :
	content= "Sun, abhi tt khelne jaana aake bolta!"
    elif searchString == 'Ninja':
	content= "Ninja ek soch hai, aur yeh soch humare dil mein hai"
    elif "Vayuj" in  searchString
	content= "Bol"
    elif "Akxt" in  searchString
	content= "Sun, abhi tt khelne jaana aake bolta!"
    return content
     
if __name__ == "__main__":
    app.run()
