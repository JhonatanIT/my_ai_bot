from flask import Flask
from app.discord_bot.discord_api import client, discord_token
import threading

app = Flask(__name__)

def callClientDiscord():
     if not client.application:
        client.run(discord_token)

@app.route("/")
def chatgptBot():  
    threading.Thread(target=callClientDiscord).start()
    return "<p>ChatGPT Bot activated!</p>"

if __name__ == '__main__':
    app.run()
    

