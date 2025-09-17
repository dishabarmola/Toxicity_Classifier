
# Toxicity Comment Classifier

## Overview

The **Toxicity Comment Classifier** is a machine learning project that automatically detects and classifies toxic comments. This model helps in moderating online platforms by identifying comments that are harmful, offensive, or inappropriate. The classifier predicts multiple categories of toxicity, such as `toxic`, `severe_toxic`, `obscene`, `threat`, `insult`, and `identity_hate`.

---

## Features

* Detects and classifies toxic comments in real-time.
* Multi-label classification for nuanced toxicity detection.
* User-friendly web interface for easy input and result visualization.
* Provides probability scores for each type of toxicity.

---

## Technologies Used

* **Python**
* **Flask** for web interface
* **Keras / TensorFlow** for deep learning model
* **scikit-learn** for preprocessing
* **HTML/CSS** for front-end

---

## Usage

1. Run the Flask application:

```bash
python app.py
```

2. Open your browser and navigate to:

```
http://127.0.0.1:5000
```

3. Enter a comment in the input box and click **Classify**. The prediction will be displayed below the form.

---

## Model Information

* The model is trained on a dataset of online comments labeled with multiple categories of toxicity.
* Text input is preprocessed using tokenization and vectorization before being fed into the model.
* The output shows probability scores for each class. Any score above 0.5 is considered positive for that category.

---


