from flask import Flask, render_template
from wikipedia import Wikipedia
from wiki2plain import Wiki2Plain
from sys import argv

app = Flask(__name__)
# CORS(app)

from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):

    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

@crossdomain(origin='*')
@app.route("/")
def main():
    return render_template('index.html')

@crossdomain(origin='*')
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
    elif "Vayuj" in  searchString:
        content= "Bol"
    elif "Akxt" in  searchString:
        content= "Sun, abhi tt khelne jaana aake bolta!"
    return content
     
if __name__ == "__main__":
    port = int(argv[1])
    app.run(host='0.0.0.0', port=port)
