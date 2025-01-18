import pandas as pd
import random

# Modèles pour spams et non-spams
spam_templates = [
    "Congratulations! You've won a {prize}! Click here to claim your {reward}.",
    "Limited time offer: {discount}! Shop now before the deal expires.",
    "Win a {product}! Just provide your {details} to enter the lottery.",
    "Your account is at risk! {action_required} immediately to secure it.",
    "Exclusive deal: Get {cashback} cashback on every {purchase}. Join now!"
]

non_spam_templates = [
    "Hi {name}, can you send me the {report} by tomorrow?",
    "Reminder: The {event} is scheduled for {day} at {time}.",
    "Hello team, the {document} has been uploaded to the shared drive.",
    "Thank you for your {order}. Your package will arrive by {date}.",
    "Hi {name}, the {meeting} agenda is ready for review. Please share feedback."
]

# Remplacements dynamiques
spam_replacements = {
    "prize": ["$1000 Walmart gift card", "free vacation package", "brand-new car"],
    "reward": ["voucher", "promo code", "reward"],
    "discount": ["50% off", "buy one get one free", "limited time deal"],
    "product": ["iPhone 14", "MacBook Pro", "luxury watch"],
    "details": ["email address", "phone number", "shipping details"],
    "action_required": ["Reset your password", "Verify your account", "Update your credentials"],
    "cashback": ["20%", "30%", "40%"],
    "purchase": ["order", "transaction", "checkout"]
}

non_spam_replacements = {
    "name": ["John", "Sarah", "Mike", "Emily", "Jessica", "David"],
    "report": ["financial report", "project proposal", "status update"],
    "event": ["team lunch", "company meeting", "weekly sync"],
    "day": ["Monday", "Wednesday", "Friday"],
    "time": ["10 AM", "3 PM", "5 PM"],
    "document": ["latest report", "updated document", "presentation slides"],
    "order": ["purchase", "order", "request"],
    "date": ["tomorrow", "next week", "within 3 days"]
}

# Générer des emails
def generate_emails(templates, replacements, n):
    emails = []
    for _ in range(n):
        template = random.choice(templates)
        email = template
        for key, values in replacements.items():
            email = email.replace(f"{{{key}}}", random.choice(values))
        emails.append(email)
    return emails

# Générer des spams et non-spams
spam_emails = generate_emails(spam_templates, spam_replacements, 400)
non_spam_emails = generate_emails(non_spam_templates, non_spam_replacements, 400)

# Supprimer les doublons et limiter à 250
spam_emails = list(set(spam_emails))
non_spam_emails = list(set(non_spam_emails))

# Compléter les listes si nécessaire
while len(spam_emails) < 250:
    spam_emails.append(random.choice(spam_emails))

while len(non_spam_emails) < 250:
    non_spam_emails.append(random.choice(non_spam_emails))

# Limiter à 250 au cas où il y aurait des doublons
spam_emails = spam_emails[:250]
non_spam_emails = non_spam_emails[:250]

# Vérifications finales
print(f"Nombre final d'emails spams : {len(spam_emails)}")
print(f"Nombre final d'emails non-spams : {len(non_spam_emails)}")

# Créer le DataFrame
data = {"email": spam_emails + non_spam_emails, "label": [1] * 250 + [0] * 250}
df = pd.DataFrame(data)

# Mélanger les données
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Sauvegarder le dataset
df.to_csv("spam_dataset.csv", index=False)
print("Fichier 'spam_dataset.csv' créé avec succès !")
