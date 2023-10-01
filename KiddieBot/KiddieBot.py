from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
time.clock = time.time

app = Flask(__name__)
english_bot = ChatBot("ChatterBot",storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
trainer.train("data/data.yml")

@app.route("/")
def index():
    return render_template("indexx.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    return str(english_bot.get_response(userText))

if __name__ == "__main__":
    app.run(debug = True)