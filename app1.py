from flask import Flask


app=Flask(__name__)
def home():
    return "<h1> MN's Flask App<\h1>"

if __name__ == "__main__":
    app.run()
