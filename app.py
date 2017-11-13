#Taylor Wong
#SoftDev1 pd7
#HW13 -- A RESTful Journey Skyward
#2017-11-09


from flask import Flask, render_template, urllib2, json
import os

app = Flask(__name__)
app.secret_key = os.random(32)

@app.route("/")
def root():
    uResp = urllib2.urlopen(https://api.nasa.gov/planetary/apod?api_key=xHFN4eZTXW4cpg8q5GL6Q9QEf1baxtBWjDw0OA3A)
    url = uResp.geturl()
    header = uResp.info()
    content = uResp.read()

    d = json.loads(header)
    return render_template



if __name__ == "__main__":
    app.debug = True
    app.run()
