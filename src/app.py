from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/detect', methods = ['GET'])
def classify():
    return jsonify({
        "message": "detected",
    })

if __name__ == "__main__":
    app.run(debug=True)