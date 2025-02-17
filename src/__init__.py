from flask import Flask, request, jsonify
from src.plate_detector.detector import model  
import cv2

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
            # "crop_img": str(list(crop_img_list[0]))
        })

    return app
