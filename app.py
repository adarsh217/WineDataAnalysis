from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the model from disk
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    review = data['review_description']
    prediction = model.predict([review])
    return jsonify({'prediction': prediction[0]})


if __name__ == '__main__':
    app.run(port=5000)
