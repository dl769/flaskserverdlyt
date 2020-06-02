from flask import Flask, send_file, request
from flask_cors import CORS 
from os import system

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['POST'])
def dwn():
    url = request.form['url']
    name = url[32:43]

    system('youtube-dl -f 251 -o "'+name+'1" '+url)
    ret = send_file(name+'1', as_attachment=True)
    return ret

if __name__ == '__main__':
    app.run(host="0.0.0.0")

