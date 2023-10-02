import json
from flask import Flask,  render_template,request
import RPi.GPIO as GPIO

servoPIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)
p.start(2)


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
    p.ChangeDutyCycle(x)

    print("x : "+ str(x)+" y: "+str(y))
    return json.dumps({'Author': 'Saman Azadi'})

def map_value(value, old_min, old_max, new_min, new_max):
    return (value - old_min) / (old_max - old_min) * (new_max - new_min) + new_min

app.run(port=8085, debug=True,host="172.16.10.108")
