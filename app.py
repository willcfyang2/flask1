from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy

from Ocrbytext import text_ocr
from dbsession import db
from models import User, ImageFile
from Languageconversion import en_to_zh, zh_to_en
from ObjectRecognition import ObjectRecognition
from imagesRecognition import images_recognition

app = Flask(__name__)
db.init_app(app)
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_RECORD_QUERIES"] = False
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_POOL_SIZE"] = 100


@app.route('/chang/zh', methods=['POST'])
def zh():
	text = request.json.get("text")
	if not text:
		return jsonify({"data": "please post args", "status": 400})
	resp = zh_to_en(text)
	return jsonify({"data": resp})


@app.route('/chang/en', methods=['POST'])
def en():
	text = request.json.get("text")
	if not text:
		return jsonify({"data": "please post args", "status": 400})
	resp = en_to_zh(text)
	return jsonify({"data": resp, "status": 200})


# 物体识别
@app.route("/ocr/recognition", methods=["POST"])
def recognition():
	data = request.json.get("url")
	if not data:
		return jsonify({"data": "please post args", "status": 400})
	resp = ObjectRecognition(data)
	return jsonify({"data": resp, "status": 200})


# 图片文字提取
@app.route("/images/recognition", methods=["POST"])
def recognition_images():
	data = request.json.get("url")
	if not data:
		return jsonify({"data": "please post args", "status": 400})
	resp = images_recognition(data)
	return jsonify({"data": resp, "status": 200})


# 正文提取
@app.route("/text/ocr", methods=["POST"])
def ocr_to_text():
	data = request.json.get("text")

	if not data:
		return jsonify({"data": "please post args", "status": 400})
	with open("./text_files/content_moderator_text_moderation.txt", encoding="utf8", mode="w") as f:
		f.write(data)
	resp = text_ocr()
	return jsonify({"data": eval(resp), "status": 200})


@app.route("/user", methods=["GET"])
def test():
	data = [i.to_json() for i in User.query.all()]
	return jsonify({"data": data, "status": 200})


@app.route("/user/create", methods=["POST"])
def user_create():
	data = request.json.get("data")
	if not data:
		return jsonify({"data": "please post args", "status": 400})
	user = User(**data)
	try:
		db.session.add(user)
		db.session.commit()
		return jsonify({"data": data, "status": 200})
	except Exception as e:
		print(e)
		return jsonify({"data": "register fail maybe this user is already exists.", "status": 400})


@app.route("/user/login", methods=["POST"])
def login():
	data = request.json.get("data")
	if not data:
		return jsonify({"data": "please post args", "status": 400})
	user = User.query.filter_by(username=data["username"], password=data["password"]).first()
	if user:
		result = user.to_json()
		del result["password"]
		return jsonify({"data": result, "status": 200, "message": "login success"})
	else:
		return jsonify({"data": "login fail", "status": 400})


@app.route("/images/upload", methods=["POST"])
def upload():
	file = request.files['file'].read()
	if len(file) > 65535:
		return jsonify({"status": 400, "message": "images is too big, please upload less then 64 kb image"})
	file_name = request.form.get("name")
	belong_user = request.form.get("uid")
	image_file = ImageFile(image_name=file_name, image=file, belong_user=belong_user)
	db.session.add(image_file)
	db.session.commit()
	return jsonify({"status": 200, "message": "upload success"})


@app.route("/images/read", methods=["GET"])
def read_images():
	belong_user = request.values.get("uid")
	images = ImageFile.query.filter_by(belong_user=belong_user).all()
	data = [i.to_json() for i in images]
	return jsonify({"status": 200, "message": "read success", "data": data})


@app.route("/dig/count", methods=["GET"])
def dig_count():
	image_id = request.values.get("id", 0)
	image = ImageFile.query.filter(ImageFile.id==image_id).first()
	image.dig_count = image.dig_count + 1 if image.dig_count else 1
	db.session.add(image)
	db.session.commit()
	return jsonify({"status": 200, "message": "dig count success"})


@app.route("/images/comment", methods=["GET"])
def comment():
	pass



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)