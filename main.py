import pymongo
from flask import Flask, request

app = Flask(__name__)
URL = "mongodb+srv://Hajdu:renato@cluster0.4rfc7.mongodb.net/system?retryWrites=true&w=majority"
client = pymongo.MongoClient(URL)
db = client.get_database('users')
data = db.get_collection('data')


@app.route('/output', methods=['GET'])
def output():
    respond = {}
    y = 0
    for x in data.find():
        respond[y] = str(x)+'</br>'
        y = y + 1
    return f'Users: {respond}</br>'


@app.route('/', methods=['GET'])
def Hello():
    return """<html>
    <head><title>User Database</title></head>
   <body>
      <form action = "http://127.0.0.1:5000/" method = "post">
        <h1>Üdvözlet</h1>
        <h3>Mongo adatbázis kiiratása: (GET)</h3>
        <p>http://127.0.0.1:5000/output</p>
        <h3>Mongo adatbázis feltöltése adatokkal: (POST)</h3>
        <p>http://127.0.0.1:5000/input</p>
      </form>
   </body>
</html>"""


@app.route('/input', methods=['POST'])
def input():
    f = request.args.get('fname')
    l = request.args.get('lname')
    g = request.args.get('gender')
    p = request.args.get('passw')
    if f and l and p and g == 'male' or g == 'female' and f and l and p:
        new_input = {
            'fname': f,
            'lname': l,
            'gender': g,
            'passw': p
        }
        data.insert_one(new_input)
        return f'''<p>The First Name is: {f} </p> <p>The Last Name is: {l}</p> <p>The Gender value is: {g}</p>  
        <p>The Password is: {p}</p> '''
    else:
        return 'Wrong data! Please give them again!'


@app.route('/login', methods=['GET'])
def login():
    f = request.args.get('fname')
    l = request.args.get('lname')
    g = request.args.get('gender')
    p = request.args.get('passw')
    if f and l and p and g == 'male' or g == 'female' and f and l and p:
        new_input = {
            'fname': f,
            'lname': l,
            'gender': g,
            'passw': p
        }
    return'Logged in.'

if __name__ == '__main__':
    app.run()
