from flask import Flask
from app.discord_bot.discord_api import client, discord_token

app = Flask(__name__)

@app.route("/")
def hello_world():  
    #client.run(discord_token)
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run()
    

