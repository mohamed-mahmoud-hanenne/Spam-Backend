# Spam Email Classifier — Backend (Flask + Logistic Regression)

Backend d’une application IA qui **classe un email en Spam / Non-Spam** à l’aide d’un modèle de **Régression Logistique** entraîné sur un dataset préparé (texte + labels).  
Ce backend expose une API REST consommée par l’interface Angular.

---

## 🚀 Fonctionnalités
- Entraînement d’un modèle **Logistic Regression**
- Prétraitement texte (nettoyage + vectorisation)
- Sauvegarde/chargement du modèle et du vectorizer
- API Flask pour prédire un email saisi dans l’interface

---

## 🧱 Tech Stack
- Python 3.x
- Flask
- scikit-learn
- pandas / numpy
- joblib (sauvegarde modèle)

---

---

## ⚙️ Installation

git clone https://github.com/mohamed-mahmoud-hanenne/Spam-Backend.git

cd backend
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate

pip install -r requirements.txt

Entraîner le modèle :
python train.py

Lancer l’API Flask
python app.py
