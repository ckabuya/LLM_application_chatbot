from flask import Flask, request, render_template
from flask_cors import CORS
import json
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = Flask(__name__)
CORS(app)

model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
conversation_history = []

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

conversation_history = []
MAX_HISTORY_TOKENS = 512  # Adjust based on model's capacity

@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    data = request.get_data(as_text=True)
    data = json.loads(data)
    input_text = data['prompt']

    # Truncate conversation history
    truncated_history = conversation_history[-6:]  # Keep last 3 exchanges
    history = "\n".join(truncated_history)

    # Tokenize and manage token count
    input_ids = tokenizer.encode(history + "\n" + input_text, return_tensors="pt")
    if input_ids.shape[1] > MAX_HISTORY_TOKENS:
        # Truncate from the beginning
        input_ids = input_ids[:, -MAX_HISTORY_TOKENS:]

    # Generate the response from the model
    outputs = model.generate(input_ids, max_length=60)

    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # Add interaction to conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)

    # Keep conversation history at a manageable size
    if len(conversation_history) > 20:
        conversation_history = conversation_history[-20:]

    return response

if __name__ == '__main__':
    app.run(debug=True)