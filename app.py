from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! My application is running on ECS Fargate."

@app.route("/health")
def health():
    return "Application is healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
