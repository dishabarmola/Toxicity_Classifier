from flask import Flask, request, render_template
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import TextVectorization
import json
import numpy as np

app = Flask(__name__)
model = load_model("comment_toxicity.h5", compile=False)
with open("vocab.json", "r") as f:
    vocab = json.load(f)

vectorizer = TextVectorization(max_tokens=len(vocab), output_sequence_length=100)
vectorizer.set_vocabulary(vocab)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        comment = request.form["comment"]
        seq = vectorizer([comment])
        pred = model.predict(seq)
        result = []
        list = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult',
       'identity_hate']
        for i in range(len(list)):
            if pred[0][i]>=0.5:
                result.append(f"{list[i]}: {pred[0][i]*100:.2f}%")
        if(not result):
            result.append("The comment is not toxic.")

        return render_template("index.html", prediction=result, comment=comment)

if __name__ == "__main__":
    app.run(debug=True)
