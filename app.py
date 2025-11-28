from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from MyApp! Deployed with GitOps + ArgoCD "

@app.route("/version")
def version():
    return "Version OK — GitOps automatically updated the deployment."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
