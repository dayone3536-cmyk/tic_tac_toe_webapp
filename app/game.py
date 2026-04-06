from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)


board=[" "]*9

@app.route("/")
def board_page():

     return render_template("index.html", board=board)

current_player = "X"
@app.route("/move", methods = ["POST"])
def main():
     global current_player


     if request.method == "POST":
          cell_state = request.form["cell"]
          cell_state = int(cell_state)

     if board[cell_state] == " ":
          board[cell_state] = current_player
     
     else:
          return render_template("restart.html")

     if current_player == "X":
          current_player = "O"

     else:
          current_player = "X"


     winning_combo = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8),(2,4,6)]
     for a,b,c in winning_combo:

          if board[a] == board[b] == board[c] != " ":
                         return f"{board[a]} WON!!"
                    
          elif " " not in board:
                         return "ITS A TIE!!"

     return render_template("index.html",board=board)

@app.route("/restart", methods = ["POST"])
def restarting():
       global board
       board = [" "]*9
       return redirect("/")

