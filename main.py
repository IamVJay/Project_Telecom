import numpy as np
from flask import Flask,render_template,request
from utils import CapexPredection
import traceback

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data', methods = ['POST','GET'])
def get_data():
    try: 
        if request.method == "POST":
            data = request.form
            class_obj = CapexPredection(data)
            result = class_obj.Fiber_Capex_Predection()
            return render_template('result.html',prediction = np.round(result, decimals=2))
        else: 
            print(f"wrong method")
            return "Wrong method"
    except: 
        print(traceback.print_exc())
        return "Prediction Failed"
if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)