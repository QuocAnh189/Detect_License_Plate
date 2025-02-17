# from flask import Flask, request, jsonify
# # from src.plate_detector.detector import model
# from plate_detector.detector import model

# app = Flask(__name__)

# @app.route('/detect', methods = ['GET'])
# def classify():
#     license_plate = request.files['image']

#     plate_list, crop_img_list = model.predict(license_plate)

#     return jsonify({
#         "plate_list": plate_list,
#         "crop_img_list": crop_img_list
#     })

# if __name__ == "__main__":
#     app.run(debug=True)

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import create_app

application = create_app()

if __name__ == "__main__":
    application.run(debug=True)