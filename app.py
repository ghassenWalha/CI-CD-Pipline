from flask import Flask
from flask_restful import Api
from resources.hello_resource import HelloWorld
app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, "/api/v1/helloWorld")

if __name__ == "__main__":
    app.run(debug=True, port=3400)
