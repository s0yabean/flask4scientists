#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 10:04:17 2018

@author: tonytonggg
"""

# From  http://wtforms.simplecodes.com/docs/1.0.1/crash_course.html

#So you’ve cracked your knuckles and started working on that 
#awesome python webapp you want to write. You get through writing
#a few pages and finally you need to tackle that loathsome task: 
#form input handling and validation. Enter WTForms.
#
#But why do I need yet another framework? Well, some webapp
#frameworks take the approach of associating database models 
#with form handling. While this can be handy for very basic 
#create/update views, chances are not every form you need 
#can map directly to a database model. Or maybe you already 
#use a generic form handling framework but you want to customize 
#the HTML generation of those form fields, and define your own 
#validation.
#
#With WTForms, your form field HTML can be generated for you, 
#but we let you customize it in your templates. This allows 
#you to maintain separation of code and presentation, and 
#keep those messy parameters out of your python code. Because 
#we strive for loose coupling, you should be able to do that 
#in any templating engine you like, as well.

from flask import Flask, render_template, request
from wtforms import Form, FloatField, validators

from compute import compute #my own function

app = Flask(__name__)

# Model
# From wtforms package
class InputForm(Form):
    r = FloatField(validators=[validators.InputRequired()])
    # the 2 validators here are for 2 purposes. The outside 
    # on is to validate that a number is provided by user, 
    # and the inner one is to prompt the user to must submit
    # an imput and not leave it blank.
    
# View
    
#Essentially, decorators work as wrappers, modifying the behavior
#of the code before and after a target function execution, without
#the need to modify the function itself, augmenting the original
#functionality, thus decorating it.    
    
@app.route('/hw1', methods = ['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        r = form.r.data
        s = compute(r) #from compute function which is my own file
        return render_template("view_output.html", form = form, s = s)
    else:
        return render_template("view_input.html", form = form)
    
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True, use_reloader=True)
    






    
