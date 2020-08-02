from flask import Flask, send_file, request
from flask_cors import CORS 
from os import system

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['POST'])
def dwn():
    url = request.form['url']
    ext = request.form['ext']
    qal = request.form['qal']
    name = url[32:43]
    print('w',url,ext,qal)

    if (ext == "mp3"):
        system('youtube-dl -f 251 -o "'+name+'1" '+url)
    elif (ext == 'mp4'):
        if (qal == '720'):
            system('youtube-dl --add-metadata -f "best[height<=720]" --recode-video mp4 -o "'+name+'1" '+url)
        if (qal == '1080'):
            system('youtube-dl --add-metadata -f "best[height<=1080]" --recode-video mp4 -o "'+name+'1" '+url)

    if (ext=="mp3" or ext =="mp4"):
        ret = send_file(name+'1', as_attachment=True)
    
    return ret

if __name__ == '__main__':
    app.run(host="0.0.0.0")

