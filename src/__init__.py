import cv2
import os
from flask import Flask, request, jsonify
from src.plate_detector.detector import model  
import cloudinary.uploader
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/detect', methods=['POST'])
    def classify():
        license_plate = request.files['image']

        if not license_plate:
            return {"error": "No image provided"}, 400

        # Call the model's predict function
        plate_list, crop_img_list = model.predict(license_plate)  

        cv2.imwrite("crop.jpg", crop_img_list[0])
        crop_response=cloudinary.uploader.upload(
        'crop.jpg',
        folder="parking",
        unique_filename = True, 
        overwrite=True,
        eager=[{"width": 200, "crop": "fill"}])
        os.remove('crop.jpg')

        return jsonify({
            "license_plate_detect": list(plate_list),
            "crop_img_list": crop_response["url"],
        })

    
        # return jsonify({
        #     "license_plate_detect": "license_plate_detect",
        #     "crop_img_list": "crop_img_list"
        # })

    return app
