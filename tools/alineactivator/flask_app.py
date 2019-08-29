from flask import Flask
from flask import request
from flask import jsonify
import db_worker as dat
app = Flask(__name__)


@app.route('/activate/', methods=['POST','GET'])
def accept():
    db = dat.database('prod.db')
    data = request.get_json()
    data = dict(data)
    skey = data['skey']
    akey = data['akey']
    skey = db.get_settings(skey)[0][1]
    akey = db.get_apikey(akey)[0][0]
    print(akey,skey)
    if akey:
        return(skey)
    else:
        return('500')

app.run()
