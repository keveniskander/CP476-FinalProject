from flask import Flask, render_template, request
from sudoku import *

app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)

@app.route("/")
def index():
    #main render
    print('index test')
    return render_template("sudoku.html")

@app.route("/b/<index_arr>",methods=["GET","POST"])
def process(index_arr):

    if request.method == 'POST': # POST request
        print(request.get_text())  # parse as text
        return 'OK', 200
    else:
        print("gdsdf")
        
        return index_arr


@app.route("/c/",methods=["GET"])
def random():
    board = generateBoard()
    sud = Sudoku(board)
        
    sud.backtracking()
    sud.print_table()
    # print("Randomly generated puzzle")
    sud.hard()
    sud.print_table()
    sud_string = sud.convert()
# print(sud.convert())

    # if __name__ == "__main__":
    #     main()
    app.run(debug=True)
    r = sud_string
    return r
