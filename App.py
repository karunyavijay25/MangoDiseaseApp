import random
from flask import Flask, render_template, request from disease_data import disease_database
app = Flask( name ) # TEMP STORAGE
last_tree = None last_disease = None @app.route('/')
def home():
return render_template('index.html') @app.route('/predict', methods=['POST']) def predict():
global last_tree, last_disease
# TEMP RANDOM (replace with AI later)
tree = random.choice(list(disease_database.keys()))
disease = random.choice(list(disease_database[tree].keys())) last_tree = tree
last_disease = disease
data = disease_database[tree][disease] return render_template(
'result.html', tree=tree, disease=disease, cause=data["cause"], why=data["why"],
environment=data["environment"], severity=data["severity"], prevention=data["prevention"]
)
@app.route('/treatment') def treatment():
data = disease_database[last_tree][last_disease] return render_template(
'treatment.html', disease=last_disease, info=data
)
if  name	== ' main ': app.run(debug=True)
