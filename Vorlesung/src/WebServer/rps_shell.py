#!/usr/bin/env python3

import random, sys

def computer_choice_get():
  choices = ['rock', 'paper', 'scissors']
  return choices[random.randint(0, 2)]

def eval_winner(player_choice, computer_choice):
  beats = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}
  if player_choice == computer_choice:
    return 'tie'
  if beats[player_choice] == computer_choice:
    return 'player'
  else:
    return 'computer'

if __name__ == '__main__':
  stat = {'player' : 0, 'computer' : 0, 'tie': 0}
  choices = ['rock','scissors','paper']
  while True:
    pc  = input('make your choice: {} (q to quit): '
                .format('/'.join(choices))).rstrip()
    if pc == 'q':
      break
    if pc in choices:
      cc = computer_choice_get()
      winner = eval_winner(pc, cc)
      stat[winner] += 1
      print('{}: won={}, loose={}, tie={}'
             .format(winner,stat['player'],
                     stat['computer'],stat['tie']))
    else:
      sys.stderr.write('choice "{}" not possible'.format(pc))
