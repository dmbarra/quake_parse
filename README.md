# quake_parse


The project is a SCRIPT to parse the log of Quake, that reads a file in moving the data to a dictionary.<br>


Install
---

    pip install -r requirements.txt  
    

Tests
---

There is unit tests to validate the logic.<br>
I Used pytest and pytest-mock.


To run the tests just send the command:

    pytest


Run
---

    python runner.py <path>/logs/qgames2.log 
    

How I implemented?
---

I used python to create the script, without any over-engineer.<br>
I started reading the file and printing the information at the console.<br>
I get the tags to start and end the game match, and the group that basic information.<br>
Next step, I add information killers and counters.<br> 
Finish this, I created the summary, just printing the information on terminal


What I can improve?
---

As usual, every code can be improved :) .<br>
I should create tests for the runner.<br>
I choose python, to be easy and fast to write the code.<br>
I did use OO, this is a Script as required, but if you choose another language, you need to change that. <br>
I saw gaps in logic, to validate edge cases, that were not mapped at specification, and I decided to ignore them.<br>
I didn't implement the "PLUS" <i>Generate a report of deaths grouped by death cause for each match.</i> 
That will be simply adding a new dictionary in the same place, where I count the kills, also 
I can save how which player kills another.
Another refactor I would like to implement, was to create constants where I must put all "magic worlds".<br>