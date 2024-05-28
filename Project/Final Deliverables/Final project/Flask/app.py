import pickle
from flask import Flask , request, render_template
app = Flask(__name__)
model = pickle.load(open("rf_acc_68.pkl","rb"))
model1 = pickle.load(open("dt_acc_68.pkl","rb"))

@app.route('/')
def welcome():
    return render_template('rr.html')

'''@app.route('/signin')
def signin():
     return render_template('signin.html')'''
 
'''@app.route('/contact')
def contact():
     return render_template('contact.html')'''
 
@app.route('/input')
def input():
     return render_template('input.html')
 
@app.route('/inci')
def inci():
     return render_template('inci.html')
 
@app.route('/input1')
def input1():
     return render_template('input1.html')
 
@app.route('/mor')
def mor():
     return render_template('mor.html')
 
'''@app.route('/reg')
def reg():
     return render_template('reg.html')'''

@app.route('/input',methods = ['GET','POST'])
def output():
    index=float(request.form["index"])
    FIPS=float(request.form["fips"])
    abc=float(request.form["age"])
    lowerabc=float(request.form["lowerinci"])
    upperabc=float(request.form["upperinci"])
    average=float(request.form["avg_count"])
    rates=float(request.form["rec_5trends"])
    lowerconf=float(request.form["lowertrends"])
    upperconf=float(request.form["uppertrends"])
    total=[[index,FIPS,abc,lowerabc,upperabc,average,rates,lowerconf,upperconf]]
    print(total)
    prediction = model.predict(total)
    print(prediction)
    prediction=int(prediction[0])
    print(prediction)
    '''prediction = 1'''
    if prediction==1:
        return render_template('inci.html',predict="PARTIALLY STABLE",file='stable.png')
    elif prediction==2:
         return render_template('inci.html',predict="DECREASING",file='decreasing.png')
    elif prediction==3:
         return render_template('inci.html',predict="STURDY",file='stable.png')
    elif prediction==4:
         return render_template('inci.html',predict="RAPIDLY INCREASING",file='increasing.png')
    elif prediction==5:
         return render_template('inci.html',predict="STABLE",file='stable.png')
    elif prediction==6:
         return render_template('inci.html',predict="FALLING",file='decreasing.png')
    elif prediction==7:
         return render_template('inci.html',predict="RISING",file='increasing.png')

@app.route('/input1',methods = ['GET','POST'])
def outputs():
    index_1=float(request.form["index_1"])
    FIPS_1=float(request.form["fips_1"])
    abc_1=float(request.form["ageD"])
    lowerabc_1=float(request.form["lowerDD"])
    upperabc_1=float(request.form["upperDD"])
    average_1=float(request.form["avg_DD"])
    rates_1=float(request.form["rec_5trendsDD"])
    lowerconf_1=float(request.form["lowertrendsDD"])
    upperconf_1=float(request.form["uppertrendsDD"])
    
    totals=[[index_1,FIPS_1,abc_1,lowerabc_1,upperabc_1,average_1,rates_1,lowerconf_1,upperconf_1]]
    print(totals)
    predictions = model1.predict(totals)
    #predictions = 1
    print(predictions)
    predictions=int(predictions[0])
    print(predictions)
    '''predictions = 1'''
    
    if predictions==1:
        return render_template('mor.html',predicts="PARTIALLY STABLE",file='stable.png')
    elif predictions==2:
         return render_template('mor.html',predicts="DECREASING",file='decreasing.png')
    elif predictions==5:
         return render_template('mor.html',predicts="STABLE",file='stable.png')
    elif predictions==6:
         return render_template('mor.html',predicts="FALLING",file='decreasing.png')
    elif predictions==7:
         return render_template('mor.html',predicts="RISING",file='increasing.png')

if __name__ == '__main__':
    app.run(debug=False, port=4000)