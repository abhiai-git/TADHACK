#!/usr/bin/python

from app import app
app.run(debug = True,host='127.0.0.1', port=9090,threaded=True)
