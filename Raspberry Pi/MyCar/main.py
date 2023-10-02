import json
from flask import Flask,  render_template,request
from tools.Mapper import map

app = Flask(__name__)


@app.route('/info', methods=['GET'])
def info():
    return json.dumps({'Author': 'Saman Azadi'})

@app.route('/', methods=['GET'])
def Index():
       return render_template('Index.html')

@app.route('/Ctrl', methods=['GET'])
def Ctrl():
    x =int(request.args.get('x'))
    y = int(request.args.get('y'))

    print("x : "+ str(map(x,0,150,0,10)))
    return json.dumps({'Author': 'Saman Azadi'})


app.run(port=8085, debug=True,host="192.168.55.159")
