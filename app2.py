from flask import Flask
from flask import Flask, render_template,json, request
from SearchMethod import SearchMethod
from wikipedia import Wikipedia
from wiki2plain import Wiki2Plain
from flask import jsonify
def wait_minute():
    import time
    time.sleep(20)
import scrapy
from selenium import webdriver
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



app = Flask(__name__)




@app.route("/")
def main():
     return render_template('index.html')

@app.route('/AboutVayuj')
def showSignUp():
    return render_template('signup.html')

@app.route('/search',methods=['POST'])
def signUp():
     
     searchString = request.form['inputPassword']
     
     return searchString
@app.route('/hello/', methods=['POST'])
def hello():
    
    lang = 'simple'
    wiki = Wikipedia(lang)
    searchString=request.form['yourname']
    searchString = searchString.title()
    browser = webdriver.Chrome("/home/akxt/chromedriver")
    browser.get('https://www.tools4noobs.com/summarize/')
    url1='https://en.wikipedia.org/wiki/Nelson_Mandela'
    username = browser.find_element_by_id("url1")
    username.send_keys(roll)
    browser.find_element_by_id("show_sentences").click()
    
    return  jsonify(content )

if __name__ == "__main__":
    app.run()
