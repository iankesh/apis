from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/")
def home():
# http://127.0.0.1:5000/
	return "Home"

@app.route("/get-user/<user_id>")
def get_user(user_id):
# http://127.0.0.1:5000/get-user/444?extra=abc
	user_data = {
		"user_id": user_id,
		"name": "Ankesh",
		"email": "iankesh@hotmail.com"
	}

	extra = request.args.get("extra")
	if extra:
		user_data["extra"] = extra
	
	return jsonify(user_data), 200

@app.route("/create-user", methods=["POST", "GET"])
# curl --location 'http://127.0.0.1:8000/create-user' \
# --header 'Content-Type: application/json' \
# --data '{
#     "user": "Ankesh"
# }'
def create_user():
	if request.method == "POST":
		data = request.get_json()
		return jsonify(data), 201

	elif request.method == "GET":
		return "create user home"





if __name__ == "__main__":
	app.run(debug=True)


