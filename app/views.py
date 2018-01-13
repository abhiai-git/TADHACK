from app import app, lm
from flask import request, redirect, render_template, url_for, flash,session,make_response
from flask.ext.login import login_user, logout_user, login_required
from .forms import LoginForm
import flask ,random
from .user import User
from datetime import datetime
import pandas as pd
import numpy as np
import json,time ,hmac,hashlib,binascii,base64,urllib2
from collections import defaultdict
import os, sys,csv
from pymongo import MongoClient
from bson import json_util
from scipy import stats
import numpy as np
import os
from pandas.stats.moments import ewma
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from phaxio import PhaxioApi
import requests


def urlEncodeReplace(encoded_token):
    for pat, txt in [['%2F','/'], ['%2B','+'], ['%3D','='], ['%23','#']]:
        encoded_token = encoded_token.replace(pat, txt)
    return encoded_token
def getVidyoIOToken(userName):
                type    = 'provision'
                key     = '4f7b5a34db3a4fa28769fcc8faea7646'
                jid     = userName + "@" + '29ebdc.vidyo.io'
                expires = 10000 + 62167219200 + int(time.mktime(datetime.now().timetuple()))
                vCard   = ""
 
                def to_bytes(o):
                                return str(o).encode("utf-8")
 
                sep = b"\0" # Separator is a NULL character
                body = to_bytes(type) + sep + to_bytes(jid) + sep + to_bytes(expires) + sep + to_bytes(vCard)
                mac = hmac.new(bytearray(key, 'utf8'), msg=body, digestmod=hashlib.sha384).digest()
                ## Combine the body with the hex version of the mac
                serialized = body + sep + binascii.hexlify(mac)
                b64 = base64.b64encode(serialized)
                token = b64.encode("utf8")
                encoded_token = urllib2.quote(token)
                return urlEncodeReplace(encoded_token);


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = app.config['USERS_COLLECTION'].find_one({"_id": form.username.data})
        if user and User.validate_login(user['password'], form.password.data) and user[u'status']==u'true':
            user_obj = User(user['_id'])
            login_user(user_obj)
	    session['logged_in'] = True
	    session['user'] = user            
	    flash("Logged in successfully!", category='success')
	    if user['role']=='admin':
	    	return render_template('admin.html', title='login', form=form)
            else:
            	return redirect(request.args.get("next") or url_for("index"))
        flash("Wrong username or password!", category='error')
    return render_template('login.html', title='login', form=form)

@app.route('/user',methods=["POST"])
def user():
	user_obj=session.get('user',None)
	user_obj['group']=list(set(user_obj['group']))
	return json.dumps(user_obj)

@app.route('/sendfax',methods=["GET","POST"])
def sendfax():
	user_obj=session.get('user', None)
	username = ''.join(random.choice('0123456789ABCDEF') for i in range(16))
	token = getVidyoIOToken(username)
	user_obj[u'token'] = token
	api = PhaxioApi("9ypqp9sv1nwwmrq7hn7u3ou26ljoi4xzoavsp74o", "lkpmjrcv730w4m3w7pitaowp6copk77gudi0jyhq")
	response = api.Fax.send(to=['4412345671'],
	    files='app/send.doc')
	return render_template('index.html',user=user_obj)

@app.route('/sendsms',methods=["GET","POST"])
def sendsms():
	user_obj=session.get('user', None)
	username = ''.join(random.choice('0123456789ABCDEF') for i in range(16))
	token = getVidyoIOToken(username)
	user_obj[u'token'] = token
	r = requests.post("https://sms.telnyx.com/send",
		data=json.dumps({
			"from": "+17733022716",
			"to": "+19084196960",
			"body": "Hi Sachin and Alan,  Join Me @AICollab!!!! at Call : Surgery1 at 1 pm Sunday 24th September 2017 Cheer AI Collab, RoomName: demo"
			}),
		headers={
			"x-profile-secret": "jSqkQ280CinfZkBBMQj3Do9K",
			"content-type": 'application/json'
		})
	r= r = requests.post("https://sms.telnyx.com/send",
		data=json.dumps({
			"from": "+17733022716",
			"to": "+14252838779",
			"body": "Hi Sachin and Alan,  Join Me @AICollab!!!! at Call : Surgery1 at 1 pm Sunday 24th September 2017 Cheer AI Collab, RoomName: demo"
			}),
		headers={
			"x-profile-secret": "jSqkQ280CinfZkBBMQj3Do9K",
			"content-type": 'application/json'
		})
	return render_template('index.html',user=user_obj)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    logout_user()
    return redirect(url_for('login'))
 
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    user_obj=session.get('user', None)
    username = ''.join(random.choice('0123456789ABCDEF') for i in range(16))
    token = getVidyoIOToken(username)
    user_obj[u'token'] = token
    return render_template('index.html',user=user_obj,)

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html')

@lm.user_loader
def load_user(username):
    u = app.config['USERS_COLLECTION'].find_one({"_id": username})
    if not u:
        return None
    return User(u['_id'])
