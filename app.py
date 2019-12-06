from flask import Flask                                                                                                                                                                             
app = Flask(__name__)                                                                                                                                                                       
@app.route('/')                                                                                                                                                                                     
def hello_world():                                                                                                                                                                                  
    return 'Flask working in Docker container!'       

@app.route("/test")
def salvador():
    return "Hello, this is a new route"

if __name__ == "__main__":                                                                                                                                                                          
    app.run(debug=True, host='0.0.0.0')
