from flask import Flask, render_template, request, session
from rps_shell import computer_choice_get, eval_winner

app = Flask(__name__)
app.secret_key = '2e7478e4933b0d630d87dd464eb24e09fdb66118'

@app.route('/', methods=['GET'])
def rps():
  player_choice = request.args.get('choice')
  if player_choice is None or player_choice == 'reset':
    session['tie'] = 0
    session['cpu'] = 0
    session['me'] = 0
    return render_template('rps_start.html')
  computer_choice = computer_choice_get()
  winner = eval_winner(player_choice, computer_choice)
  if winner == 'tie':
    session['tie'] += 1
  elif winner == 'player':
    session['me'] += 1
  else:
    session['cpu'] += 1
  return render_template('rps.html',
                         winner=winner,
                         player_choice=player_choice,
                         computer_choice=computer_choice,
                         cpu=session['cpu'],
                         me=session['me'],
                         tie=session['tie'])
