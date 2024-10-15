from connect_four import *

def two_ai_game():
    my_board = make_board()
    while not game_is_over(my_board):
      #The "X" player finds their best move.
      result = minimax(my_board, True, 5, -float("Inf"), float("Inf"), my_evaluate_board)
      print( "X Turn\nX selected ", result[1])
      print(result[1])
      select_space(my_board, result[1], "X")
      print_board(my_board)

      if not game_is_over(my_board):
        #The "O" player finds their best move
        result = minimax(my_board, False, 1, -float("Inf"), float("Inf"), codecademy_evaluate_board)
        print( "O Turn\nO selected ", result[1])
        print(result[1])
        select_space(my_board, result[1], "O")
        print_board(my_board)
    if has_won(my_board, "X"):
        print("X won!")
    elif has_won(my_board, "O"):
        print("O won!")
    else:
        print("It's a tie!")

def random_eval(board):
  return random.randint(-100,100)


def my_evaluate_board(board):
  if has_won(board,"X"):
    return float("Inf") 
  elif has_won(board,"O"):
    return -float("Inf")
  x_two_streaks=0
  o_two_streaks=0
 
  #to the right
  for column in range(len(board)-1):
    for row in range(len(board[0])):
      if board[column][row]=="X" and board[column+1][row]=="X":
        if column==len(board)-3 :
          if board[column+2][row]=="X":
            x_two_streaks+=2
        x_two_streaks+=1
      elif board[column][row]=="O" and board[column+1][row]=="O":
        if column==len(board)-3:
          if board[column+2][row]=="O":
            x_two_streaks+=2
        o_two_streaks+=1
  return x_two_streaks-o_two_streaks
two_ai_game()
