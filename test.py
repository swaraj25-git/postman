from flask import Flask,request

app = Flask(__name__)

@app.route("/")

def helo_world():
    return "Hello World!"

@app.route('/sit')
def sit():
    return "Sit Rocks!!"


stored_age = 26

@app.route('/sheela')
def sheela_age():
    return "Sheela"

@app.route('/sheela/<age>')
def sheela(age):
    return f"Sheela ke umar hai {age}"


@app.route('/sheela/<age>', methods=['POST'])
def sheela_post():
    global stored_age
    age = request.form.get('age')
    stored_age = age
    return "Done"




app.run()

