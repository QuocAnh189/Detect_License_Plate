from flask import Flask, request, jsonify
from src.plate_detector.detector import model  

def create_app():
    app = Flask(__name__)

    @app.route('/detect', methods=['POST'])
    def classify():
        license_plate = request.files['image']

        if not license_plate:
            return {"error": "No image provided"}, 400

        # Call the model's predict function
        plate_list, crop_img_list = model.predict(license_plate)  

        return jsonify({
            "license_plate_detect": list(plate_list),
            "crop_img_list": crop_img_list
        })
    
        # return jsonify({
        #     "license_plate_detect": "license_plate_detect",
        #     "crop_img_list": "crop_img_list"
        # })

    return app
