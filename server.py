from flask import Flask, render_template, request, redirect, session, json
import requests

app = Flask(__name__)
app.secret_key = "unicorns"

@app.route('/') 
def index(): 
    print("-------------------------------------------------------")
    
  
    return render_template("index.html")

@app.route('/battle', methods=["POST"])
def battle():
    
    session['player1'] = request.form['player1']
    session['player2'] = request.form['player2']

    p1 = requests.get('https://api.github.com/users/'+request.form['player1'])
    p2 = requests.get('https://api.github.com/users/'+request.form['player2'])

    p1info = json.loads(p1.text)
    p2info = json.loads(p2.text)

    p1score = p1info['public_repos'] * 12
    p2score = p2info['public_repos'] * 12

    if p1score > p2score:
        session['winnerName'] = session["player1"]
        session['winnerScore'] = p1score
        session['loserName'] = session["player2"]
        session['loserScore'] = p2score
    elif p2score > p1score:
        session['winnerName'] = session["player2"]
        session['winnerScore'] = p2score
        session['loserName'] = session["player1"]
        session['loserScore'] = p1score
    else:
        session['tieScore'] = p1score


    return redirect("/results")


@app.route('/results')
def results():

    
    
    return render_template("results.html")





app.run(debug=True)