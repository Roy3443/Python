from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")



def to_dict(self):
    dictionary={}
    for column in self.__table__.columns:
        dictionary[column.name]=getattr(self,column.name)
    return dictionary


@app.route("/random",methods=["GET"])
def random_cafe():
    result=db.session.execute(db.select(Cafe))
    all_cafes=result.scalars().all()
    random_cafe=random.choice(all_cafes)
    #
    # return jsonify(cafe={
    #     "id":random_cafe.id,
    #     "name":random_cafe.name,
    #     "map_url":random_cafe.map_url,
    #     "img_url":random_cafe.img_url,
    #     "location":random_cafe.location,
    #     "seats":random_cafe.seats,
    #     "has_toilet":random_cafe.has_toilet,
    #     "has_wifi":random_cafe.has_wifi,
    #     "has_sockets":random_cafe.has_sockets,
    #     "can_take_calls":random_cafe.can_take_calls,
    #     "coffee_price":random_cafe.coffee_price,
    # })
    return jsonify(cafe=to_dict(random_cafe))


@app.route("/all", methods=["GET"])
def all():
    result = db.session.execute(db.select(Cafe))
    all_cafe=result.scalars().all()
    dic=[]
    for cafe in all_cafe:
        ind_dic=to_dict(cafe)
        dic.append(ind_dic)
    return jsonify(cafe=dic)


@app.route("/search")
def search():
    query_loc=request.args.get("loc")
    result=db.session.execute(db.select(Cafe).where(Cafe.location==query_loc)).scalars().all()
    if result:
        dic=[]
        for cafe in result:
            ind_dic=to_dict(cafe)
            dic.append(ind_dic)
        return jsonify(cafe=dic)
    else:
        return jsonify(error={"Not found":"Sorry no cafe"}),404


@app.route("/add", methods=["POST"])
def add():
    new_cafe=Cafe(
        id=request.form.get("id"),
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("has_sockets")),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success":"successfully added"})


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update(cafe_id):
    query_price=request.args.get("new_price")
    cafe=db.session.get(Cafe,cafe_id)
    if cafe:
        cafe.coffee_price=query_price
        db.session.commit()
        return jsonify(response={"success":"updated successfully"}),200
    else:
        return jsonify(error={"failed":"not found"}),404

# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record
@app.route("/delete/<int:cafe_id>",methods=["DELETE"])
def delete(cafe_id):
    api_key=request.args.get("api-key")
    if api_key=="TopSecretapikey":
        cafe=db.session.get(Cafe,cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success":"deleted successfully"}),200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(forbidden={"error":"not allowed"})


if __name__ == '__main__':
    app.run(debug=True)
