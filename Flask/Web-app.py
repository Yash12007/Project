from flask import Flask, request, render_template

app = Flask(__name__)

'''
If you want to run this file 
https://replit.com/@Yash12007/Web-application?v=1#main.py 
Run this file on replit.com 
'''

@app.route("/login", methods=["POST", "GET"])

def login():

  if request.method == "POST":

    user = request.form["nm"]

    pas = request.form["pass"]

    return f'<b>Hello {user} your password is {pas}</b>'

  else:

    return 'Fill the login form'

@app.route("/", methods=['GET', 'POST'])

def index():

    htmlc = render_template('Index.html')

    if(request.method == 'POST'):

        # Remember that <input type="text" placeholder="search" id="text_box" name="search"> this tag is important in your .html file

        search = request.form['search']

        if search in render_template('Index.html'):

            return f'<body style="background: black;"><b style="color: cyan; background: black;">Results: {int(search in htmlc)}\nyour search: {search}{htmlc}</b></body>'

        else:

          return f'<body style="background: black;"><b style="color: red; background: black;">Results: {int(search in htmlc)}\nyour search: {search}{htmlc}</b></body>'

    return render_template('Index.html')

app.run(port=8000, debug=True)
