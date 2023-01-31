from flask import Flask
from flask_restful import Resource, Api
from datetime import datetime
from datetime import timezone
import time

app = Flask(__name__)
api = Api(app)

time_unix_ts = time.time()

ANSWER = {
    '1': {'message': 'Automate all the things!', 'timestamp': '{}'.format(time_unix_ts)}
}

class Times(Resource):
    def get(self):
        print("something")
        return ANSWER

api.add_resource(Times, '/times/')

if __name__ == "__main__":
    app.run(debug=True)