from flask import Flask, request, jsonify
from transformers import pipeline

# Load grammar correction pipeline
corrector = pipeline("text2text-generation", model="vennify/t5-base-grammar-correction")

app = Flask(__name__)

@app.route('/grammar-check', methods=['POST'])
def grammar_check():
    data = request.get_json()
    user_text = data.get('text')

    # Perform grammar correction using Hugging Face model
    prompted_text = user_text
    result = corrector(prompted_text, max_length=128)[0]['generated_text'] 
    
    return jsonify({"corrected_text": result})

if __name__ == '__main__':
    app.run(debug=True)
