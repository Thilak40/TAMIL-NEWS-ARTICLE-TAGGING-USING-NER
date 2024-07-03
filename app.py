from flask import Flask, render_template, request
import spacy
from spacy import displacy

app = Flask(__name__)

# Load the custom SpaCy model
nlp = spacy.load(r"C:\Users\Mohamed Kani P K\Desktop\Thilak NLP\output\model-best")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_text():
    text = request.form['text']
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    html = displacy.render(doc, style="ent", page=True)
    
    return render_template('index.html', entities=entities, text=text, html=html)

if __name__ == '__main__':
    app.run(debug=True)
