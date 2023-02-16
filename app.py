# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 21:06:57 2023

@author: YESHU
"""


import numpy as np
from flask import Flask,request , jsonify , render_template
import pickle



app = Flask(__name__)

# RENDER PREDICTION PAGES

# render crop recommendation result page

@ app.route('/', methods=['POST', 'GET'])
def crop_prediction():
    title = 'Harvestify - Crop Recommendation'

    if request.method == 'POST':
        Ipv = float(request.form['Ipv'])
        Vpv = float(request.form['Vpv'])
        Vdc= float(request.form['Vdc'])
        ia = float(request.form['ia'])
        ib = float(request.form['ib'])
        ic = float(request.form['ic'])
        va = float(request.form['va'])
        vb = float(request.form['vb'])
        vc  = float(request.form['vc'])
        Iabc = float(request.form['Iabc'])
        If = float(request.form['If'])
        Vabc = float(request.form['Vabc'])
        Vf = float(request.form['Vf'])
        
        
        
        data = np.array([[Ipv,Vpv,Vdc,ia,ib,ic,va,vb,vc,Iabc,If,Vabc,Vf]])
        



        model_path = 'C://DATA solor//models//RandomForest.pkl'
        model = pickle.load(open(model_path, 'rb'))
        my_prediction = model.predict(data)
        if my_prediction == 1:
            print('fault')
        else:
            print('no fault')
        
        
        
       
        
        final_prediction = my_prediction[0]
        
               
             
                     
        
         

        return render_template('solar-result.html' ,prediction=final_prediction,title=title)

    else:
        return render_template('solar.html')



# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=True)
