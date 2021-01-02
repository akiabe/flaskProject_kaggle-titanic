from flask import Flask, jsonify
import joblib
import pandas as pd

app = Flask(__name__)


@app.route('/predict', methods=["POST"])
def predict():
    json_ = request.json
    query_df = pd.DataFrame(json_)
    preds = clf.predict(query_df)
    return jsonify({'prediction': list(preds)})


if __name__ == '__main__':
    clf = joblib.load("model_0.bin")
    clf_columns = joblib.load('clf_columns.bin')
    app.run(port=8080)
