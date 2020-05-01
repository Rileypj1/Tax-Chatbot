from flask import Flask
from flask import render_template, jsonify, request
import requests
from models import *
import random

app= Flask(__name__)

@app.route('/')
def hello_world():
    """
    Sample hello world
    """
    return render_template('base.html')


def format_entities(entities):
    """
    formats entities to key value pairs
    """
    # Should be formatted to handle multiple entity values
    e = {"day": None, "time": None, "place": None}
    for entity in entities:
        e[entity["entity"]] = entity["value"]
    return e



@app.route('/chat', methods=["GET" "POST"])
def chat():
    """
    chat end point that performs NLU using rasa.ai
    and constructs response from response.py
    """
    try:
        response = requests.get("http://localhost:5005/", params={"q": request.form["text"]})
        response = response.json()
        print (response)
        intent = response.get("intent", {}).get("name", "default")
        entities = format_entities(response.get("entities", []))
        if intent == "event-request":
            response_text = get_event(entities["day"], entities["time"], entities["place"])
        else:
            response_text = get_random_response(intent)
        return jsonify({"status": "success", "response": response_text})
    except Exception as e:
        print(e)
        return jsonify({"status": "success", "response": "Sorry I am not trained to do that yet..."})


app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8000)