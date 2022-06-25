from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def odp():
    return "Nic tu nie ma, tez lubisz POSTowac dane?"


@app.route('/',methods=['POST'])
def odp2():
    return "Brawo oto twoja Flaga! CTF{Y0U_D1D_1T!}"


app.run(port=1234)