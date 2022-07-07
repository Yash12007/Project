# import modules
from flask import Flask, render_template, request

# define value by variable
app = Flask(__name__)

# call function by browser
@app.route("/", methods=['GET', 'POST'])
def home():
    htmlc = render_template('index.html')
    if(request.method == 'POST'):
        # Remember that <input type="text" placeholder="search" id="text_box" name="search"> this tag is important in your .html file
        search = request.form['search']
        if search in render_template('index.html'):
            return f'<body style="background: black;"><b style="color: cyan; background: black;">Results: {int(search in htmlc)}\nyour search: {search}{htmlc}</b></body>'
        else:
            return f'<body style="background: black;"><b style="color: red; background: black;">Results: {int(search in htmlc)}\nyour search: {search}{htmlc}</b></body>'
    return render_template('index.html')

# Run server
app.run(debug=True, port=8000)