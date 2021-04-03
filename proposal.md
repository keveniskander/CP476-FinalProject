---
title:  'CP476 Project: Sudoku Solver<br>'
authors: Keven Iskander, Carla Castaneda, Nicole Laslavic
date: 2021-03-22
---
## Authors

Keven Iskander, Carla Castaneda, Nicole Laslavic

## Introduction

We will create a dynamic, web application that visualizes a sudoku puzzle solving algorithm. Given a user input, the unsolved sudoku puzzle will be displayed on an html front-end with css styling, then processed through a POST and GET request to a python script that uses artificial intelligence to solve the puzzle and POST the returned puzzle to the user interface. The python algorithm was written by our group members for CP468 – Artificial Intelligence, however, part of it will need to be re-written to accept an HTML form request. All the group members involved in this project were also authors of the Sudoku puzzle solving python script written for CP486. We will use either AJAX framework or Flask framework to make HTTP requests on the server side. Users will be able to interact with the sudoku puzzle in the form of an HTML table, where each element represents a digit within the puzzle.

As an added bonus, we hope to store relevant puzzle information using MongoDB such as the number of puzzles our algorithm has solved in total, number of puzzles our users have solved total, and the top 5 most difficult puzzles it has solved to date.

 
## Problem solving and algorithms

On the client side, we will have a user input form with an HTML table for input. Styling and formatting will also be implemented on the front-end user interface with CSS stylesheets and if we have time, Javascript animations will be included for added visual effects. From the server side, puzzles will be stored and accessed either in JSON format or raw inputs from the HTML form added to arrays within the python script. The number of total puzzles solved will need to be written to a server using SQL queries, and the top 5 most complicated puzzles our algorithm has solved will be stored as JSON files to be requested from the server. 

The sudoku puzzle solving script was implemented using a combination of two well-documented artificial intelligence algorithms, the AC-3 algorithm, and the backtracking algorithm. The AC-3 process involves organizing constraints and evaluating the next best digit to insert without violating the rules of the puzzle. Unfortunately, AC-3 alone cannot always solve the puzzle to completion. That is where backtracking plays its role, by iterating backwards through the puzzle to try and re-insert values to solve the remainder of the puzzle. More information can be found in our repository A [Link Sudoku Script Repository](https://github.com/keveniskander/CP468_A2).

## System Design

![Figure 1](images/System_Design.png){width=600px}

We will use tools such as XAMPP  to locally view our website. For the database portion we will use MongoDB to connect to a database that tracks the number of total solved puzzles completed by users and our solver. On top of that our database will store json files of the top 5 hardest puzzles our sudoku solver has solved. The CGI programming tool we will be working with is AJAX. 

![Figure 2](images/Architectural_Diagram.png){width=600px}

## Milestones & schedule



| Task ID | Description   |  Due date | Lead   |  
| :----:  | :------------ | :-----:   | :------: |  
|  1      | Project research & team up | Day 5 of week 9 | Everyone | 
|  2      | Project proposal | Day 1 of week 10 | Everyone |
|  3      | Start working on front end | Day 3 of week 10 | Carla  |
|  4      | Finish front end | Day 5 of week 10  | Carla  |
|  4      | Work on incorporating database components to front end  | Day 1 of week 11  | Keven  |
|  4      | Start working on incorporating python script containing the AI sudoku code to front end  | Day 3 of week 11  | Nicole  |
|  4      | Finish last meetings goal  | Day 5 of week 11  | Nicole  |
|  4      | Clean up project and get ready for project demonstration | Day 1 of week 12  | Keven  |
|  5      | Project demonstration | Day 5 of week 12 | Everyone  |
|  6      | Project submission | Day 5 of week 13 | Everyone  |


## References

Healey, Andrew. “Talking to Python from JavaScript (and Back Again!).” Healeycodescom Blog 
RSS, 11 Apr. 2019, healeycodes.com/javascript/python/beginners/webdev/2019/04/11/talking-between-languages.html. 

Lee. “How to Code a Sudoku Solver in Python and Flask.” Coding Projects Hub, 23 Jan. 2021, 
codingprojectshub.com/how-to-code-a-sudoku-solver-in-python-and-flask/. 

Laslavic, Iskander, Castaneda, Francis. 2020. CP468_A2. 
https://github.com/keveniskander/CP468_A2. (2021).

