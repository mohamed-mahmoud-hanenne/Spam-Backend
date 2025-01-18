import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.over_sampling import RandomOverSampler
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

# Charger le dataset
data = pd.read_csv('data/spam_dataset_optimized.csv')

# Prétraitement des emails
def preprocess_email(email):
    email = email.lower()
    email = re.sub(r'[^a-z\s]', '', email)
    return email

data['email'] = data['email'].apply(preprocess_email)

# Features et labels
X = data['email']
y = data['label']

# Vectorisation avec TF-IDF
tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
X_tfidf = tfidf_vectorizer.fit_transform(X)

# Gestion du déséquilibre
oversampler = RandomOverSampler(random_state=42)
X_resampled, y_resampled = oversampler.fit_resample(X_tfidf, y)

# Division en ensemble d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.3, random_state=42)

# Entraîner le modèle
model = LogisticRegression(class_weight='balanced', C=0.1, max_iter=1000)
model.fit(X_train, y_train)

# Évaluation
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Afficher la matrice de confusion
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Ham', 'Spam'], yticklabels=['Ham', 'Spam'])
plt.xlabel('Prédictions')
plt.ylabel('Vrais labels')
plt.title('Matrice de Confusion')
plt.show()

# Sauvegarde du modèle et du vectoriseur
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(tfidf_vectorizer, open('tfidf.pkl', 'wb'))

print("Modèle et vectoriseur TF-IDF sauvegardés avec succès.")
