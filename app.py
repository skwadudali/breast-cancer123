import flask
from flask import request, render_template
import joblib
model = joblib.load('project3.pkl')
app=flask.Flask(__name__,static_url_path='')
@app.route('/',methods=['GET'])
def sendMainpage():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def doPredict():
    s1=float(request.form['f1'])
    s2=float(request.form['f2'])
    s3=float(request.form['f3'])
    s4=float(request.form['f4'])
    s5=float(request.form['f5'])
    x=[[s1,s2,s3,s4,s5]]
    prediction = model.predict(x)[0]
    return render_template('predict.html',predict=prediction)
if __name__ == '__main__':
    app.run()



    
