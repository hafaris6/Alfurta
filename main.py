from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "أهلاً بك في الفرات"

if __name__ == "__main__":
    app.run()
