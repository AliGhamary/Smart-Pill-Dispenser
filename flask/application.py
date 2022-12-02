from flask import Flask, render_template
#import RPi.GPIO as GPIO
#from adafruit_servokit import ServoKit
#kit = ServoKit(channels=16)

app = Flask(__name__)

#Manipulate GPIO pins

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/container.html')
def container():
    return render_template("container.html")

@app.route('/1')
def container1():
    kit.servo[0].angle = 0
    sleep(1)
    kit.servo[0].angle = 180
    sleep(1)
    kit.servo[0].angle = 0
    return render_template("index.html")

@app.route('/2')
def container2():
    kit.servo[1].angle = 0
    sleep(1)
    kit.servo[1].angle = 180
    sleep(1)
    kit.servo[1].angle = 0
    return render_template("index.html")

@app.route('/3')
def container3():
    kit.servo[2].angle = 0
    sleep(1)
    kit.servo[2].angle = 180
    sleep(1)
    kit.servo[2].angle = 0
    return render_template("index.html")

@app.route('/4')
def container4():
    kit.servo[3].angle = 0
    sleep(1)
    kit.servo[3].angle = 180
    sleep(1)
    kit.servo[3].angle = 0
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)