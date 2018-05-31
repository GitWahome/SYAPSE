# SYAPSE
This is a solution to the challenge below:
------------------------------------------------------------------------------------------------

You're looking at the topography of some land (2D only) and wondering how much water it will hold if a bucket of water were poured over the land.
(Visualize a rocky hill sliced down the middle.)

The land is represented as a list, with the value in the list being the height of the land at that point.

For example:
	O is land
	* is water
The list [5, 3, 2, 4, 1, 2] would look like this:

O
O**O
OO*O
OOOO*O
OOOOOO

and hold 4 units of water

Given a list of arbitrary length, how much water will the land hold?
------------------------------------------------------------------------------------------------
# Solution
The functions that facilitate the generation of the trougs and the water level for each trough are in the **-waterLevelGenerator.py-** file.
# Running:
Clone this repo. It should save the two files in a similar level facilitation the importation in **-test.py-**.

In the terminal, navigate to the folder and run the command prompt or your favorite python3 IDE to view solutions:
 
 ```python3 test.py```
  
# Other test cases
You can add new test cases in **-test.py-** as prompted by the comments.
