import joblib

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Predik')
def Predik():
    return render_template('Predik.html')


@app.route('/result', methods=['POST'])
def hasil():
    if request.method == 'POST':
        input = request.form 
        Y = float(input['Y'])
        pv = float(input['pv'])
        pi = float(input['pi'])
        iq = float(input['iq'])
        eq = float(input['eq'])
        pv = float(input['pv'])
        tc = float(input['tc'])
        d = float(input['d'])
        predik = model.predict([[Y,pv,pi,iq,eq,pv,tc,d]])[0]
    return render_template('Predik.html')






if __name__ == "__main__":
    model = joblib.load('Model_LR_PRICE')
    app.run(debug=True) 