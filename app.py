from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import re

# Initialisation de Flask
app = Flask(__name__)
CORS(app)

# Charger le modèle et le TF-IDF vectorizer
model = pickle.load(open('model.pkl', 'rb'))
tfidf_vectorizer = pickle.load(open('tfidf.pkl', 'rb'))

# Fonction pour prétraiter les emails
def preprocess_email(email):
    # Convertir en minuscules
    email = email.lower()
    # Supprimer les caractères spéciaux (sauf les espaces)
    email = re.sub(r'[^a-z0-9\s]', '', email)
    return email

# Route pour prédire si un email est un spam
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    email = data.get('email', '')
    if not email:
        return jsonify({'error': 'Email is required'}), 400

    print("Email reçu :", email)  # Log pour debug
    cleaned_email = preprocess_email(email)
    email_vector = tfidf_vectorizer.transform([cleaned_email])
    prediction = model.predict(email_vector)[0]
    print("Prédiction :", prediction)  # Log pour debug

    return jsonify({'spam': bool(prediction == 1)})



if __name__ == '__main__':
    app.run(debug=True)
