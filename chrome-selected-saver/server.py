from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()
    text = data.get("text", "")

    print("Received:", text)

    result = process_text(text)

    return jsonify({"result": result})

def process_text(text):
    # YOUR LOGIC HERE
    # Example:
    processed = text.upper()
    print("Processed:", processed)

    # You can:
    # - save to file
    # - call APIs
    # - run LLM
    # - automate workflows

    return processed

if __name__ == "__main__":
    app.run(port=5000)