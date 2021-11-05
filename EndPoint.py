from flask import Flask, request
from flask_restx import Api, Resource, Namespace, fields

app = Flask(__name__)

api = Api(app,
		  version = "1.0",
		  title = "Name Recorder",
		  description = "Manage names of various users of the application")


Data=[]

# @api.route("/main")
# class MainClass(Resource):
# 	def get(self):
#
# 		return {
# 			"status": "Got new data"
# 		}
# 	def post(self):
# 		return {"Tem"}


name_space = api.namespace('names', description='Manage names')

model = api.model('Name Model',
		  {'name': fields.String(required = True,
					 description="Name of the person",
help="Name cannot be blank.")})

list_of_names = {}

@name_space.route("/<int:id>")

class MainClass(Resource):

	@api.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' },
			 params={ 'id': 'Specify the Id associated with the person' })
	def get(self, id):
		try:
			name = list_of_names[id]
			return {
				"status": "Person retrieved",
				"name" : list_of_names[id]
			}
		except KeyError as e:
			name_space.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
		except Exception as e:
			name_space.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

	@api.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' },
			 params={ 'id': 'Specify the Id associated with the person' })
	@api.expect(model)
	def post(self, id):
		# try:
		# 	list_of_names[id] = request.json['name']
		#
		# 	return {
		# 		"status": "Person retrieved",
		# 		"name" : list_of_names[id],'name3': request.json['name']
		# 	}
		try:
			list_of_names[id] = request.json
			master.run_report()
			return {
				"status": "Person retrieved",
				"name" : list_of_names[id]
			}



		except KeyError as e:
			name_space.abort(500, e.__doc__, status = "Could not save information", statusCode = "500")
		except Exception as e:
			name_space.abort(400, e.__doc__, status = "Could not save information", statusCode = "400")

from flask import Flask

if __name__ == '__main__':
	app.run(debug=True)
	app = Flask(__name__)


	@app.route('/')
	def home():
		return "Hey there!"

