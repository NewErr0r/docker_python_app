from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
        <title>Oaklet.org </title>
        <h1>Welcome to Oaklet.org web-app for running Flask inside Docker!</h1>        
        """

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
