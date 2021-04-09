from flask import Flask, render_template, request
from sudoku import *

# mongo = "mongodb+srv://admin:1234@projects.rorbz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

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
        # print("Error: Keven's Error")
        puzzle_arr = []
    
        index_arr = index_arr.replace(",","")
        for i in range(len(index_arr)):
            puzzle_arr.append(int(index_arr[i]))
        # print("puzzle array:", puzzle_arr)
        sud = Sudoku(puzzle_arr)
        constraints=sud.constraints()
        sud.AC3(constraints)
        sud.AC3_table()
        flag=True
        for i in range (len(sud.table)):
            for j in range(len(sud.table)):
                if (sud.table[i][j].value==0):
                    flag=False
                    break
        if(flag==False):
            sud.backtracking()
        sud_string = sud.convert()
        print('sud_string',sud_string)
        return sud_string

    


@app.route("/c1/",methods=["GET"])
def random2():
    board = generateBoard()
    sud = Sudoku(board)
        
    sud.backtracking()
    sud.print_table()
    # print("Randomly generated puzzle")
    sud.easy()
    sud.print_table()
    sud_string = sud.convert()
# print(sud.convert())

    # if __name__ == "__main__":
    #     main()
    # app.run(debug=True)
    r = sud_string
    return r

@app.route("/c2/",methods=["GET"])
def random1():
    board = generateBoard()
    sud = Sudoku(board)
        
    sud.backtracking()
    sud.print_table()
    # print("Randomly generated puzzle")
    sud.medium()
    sud.print_table()
    sud_string = sud.convert()
# print(sud.convert())

    # if __name__ == "__main__":
    #     main()
    # app.run(debug=True)
    r = sud_string
    return r

@app.route("/c3/",methods=["GET"])
def random3():
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
    # app.run(debug=True)
    r = sud_string
    return r

    
@app.route("/d/<index_arr>",methods=["GET","POST"])
def validate():
    if request.method == 'POST': # POST request
        print(request.get_text())  # parse as text
        return 'OK', 200
    else:
        # print("Error: Keven's Error")
        puzzle_arr = []
    
        index_arr = index_arr.replace(",","")
        for i in range(len(index_arr)):
            puzzle_arr.append(int(index_arr[i]))
        # print("puzzle array:", puzzle_arr)
        sud = Sudoku(puzzle_arr)
        sud_bool = sud.is_valid()
        sud_string = ""
        if sud_bool == True:
            sud_string = '1'
        else:
            sud_string = '0'
        print('sud_string',sud_string)
        return sud_string