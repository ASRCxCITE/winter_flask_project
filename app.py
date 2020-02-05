from flask import Flask, render_template,g, render_template, flash, redirect, url_for

app = Flask(__name__)                                                                                                                                                                               
                                                                                                                                                                                                    
@app.route('/')                                                                                                                                                                                     
def hello_world():                                                                                                                                                                                  
    return render_template("home.html")  

@app.route('/graph1')
def salvador():
    return render_template("graph1.html")  

@app.route('/graph2')
def stan():
    return render_template("graph2.html")  
                                                                                                                                                                                                    
                                                                                                                                                                                                    
if __name__ == "__main__":                                                                                                                                                                          
    app.run(debug=True, host='0.0.0.0',port=5000)
