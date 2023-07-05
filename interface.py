from flask import Flask, jsonify, request, render_template
from utils import Mobileprice
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"Result":"Successful"})

@app.route('/Mobile_Price', methods = ["POST"])
def get_mobileprice():
    data=request.form
    print("Data : ", data)

    System=data['System']
    Memory = data['Memory']
    RAM = data['RAM']
    Display = data['Display']
    Display_Quality= data['Display_Quality']
    Camera = data['Camera']
    Battery = data['Battery']
    Sim = data['Sim']
    Screen_Refresh_Rate= data['Screen_Refresh_Rate']
    Make = data['Make']

    obj1 = Mobileprice()
    predicted_price = obj1.get_predicted_mobileprice(System,Memory,RAM,Display,Display_Quality,Camera,Battery,Sim,Screen_Refresh_Rate,Make)
    return jsonify({"Result" :f"Predicted Mobile price is{predicted_price} Rs. only/-"})

if __name__ == "__main__":
    app.run()


