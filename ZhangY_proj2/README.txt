Readme for CS2223 - Project 2  - Ying Zhang
I use PyCharm to run my code
This code read input4.txt, which is required in homework instruction.
To read other file, change the file name in line 27.

Or
simply run:

    python project2.py

with input file:

    python project2.py input.txt

Three test cases

[(55,11),(59,22),(500,555),(999,0)]
test brute force:O(n^2)
The closest distance by brute force: 11.704699910719626
The time use for brute force 3.790855407714844e-05
test recursive:O(nlogn)
The closest distance by recursive: 11.704699910719626
The time use for recursive 0.0005371570587158203

[(55,11),(1000,22),(36,555),(999,0),(2,3),(5,8)]
test brute force:O(n^2)
The closest distance by brute force: 5.830951894845301
The time use for brute force 4.9114227294921875e-05
test recursive:O(nlogn)
The closest distance by recursive: 5.830951894845301
The time use for recursive 6.008148193359375e-05

[(501,0),(5,0),(5,8)]
test brute force:O(n^2)
The closest distance by brute force: 8.0
The time use for brute force 3.504753112792969e-05
test recursive:O(nlogn)
The closest distance by recursive: 8.0
The time use for recursive 1.4066696166992188e-05
