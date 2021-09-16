As neuroscientists, we are probably all familiar with the Y maze test, a test to evaluate spatial working memory in mice.
To put it simply, the mouse is put in a maze, which unsurprisingly has a Y shape, and the researcher must record the sequence of arm entries during a mouse exploration of the maze. Here's the maze:
![alt text](https://github.com/AlexiaTiberi/Behavior_Code/blob/main/ymaze.png) 

-------------------------------------
In this test, a mouse has performed well if it has alternated between arms - for example if it enters a then b then c, while it is considered to have performed poorly if it does something like "ccbcbc" as a sequence of arm entries. To quantify the performance, we usually report both the total number of entries (to account for general motility) and Spontaneous Alternation% defined as 100 x number of correct alternations/total number of entries. Since I got bored with getting the data by hand (it was enough that I had to watch a mouse for five minutes and record on a piece of paper where the little thing went), I wrote this very easy code to get data from a string of "abc" corresponding to the arm entries in a Ymaze:

------------------------------------------------
In the 2.0 version, you get asked where you want to save your analysis first: just paste in the path from the address bar.
Type n to enter a new pair of animal code/string. 
The program asks to enter the code that identifies the animal 

Ex: Animal code: Cage1_m1_DOB19/02/2020

And the string corresponding to the arm entries

Ex: String: abcbacbabcbacbbacbbabacbacbac

After entering all your data type quit to exit the program. The program outputs a csv file (named "ymazeanalysis") containing the  number of entries, the number of correct alternations and finally the alternation index, together with the given animal code and string.

Python version: 3.7.6
------------------------------------------------
