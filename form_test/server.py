from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    # we'll talk about the following two lines after we learn a little more about forms
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    # to created.html
    # return render_template("created.html")
    # redirects back to the '/' route
    return redirect('/show')

# this part is for "sessions" - "remember" the information that users input. e.g. name and email
@app.route('/show')
def show_user():
    # create user.html to get data
    return render_template('user.html')
    # dummy way to get data from session
    # return render_template('user.html', name=session['name'], email=session['kpatel@codingdojo.com'])

if __name__=="__main__":
    app.run(debug=True) 
