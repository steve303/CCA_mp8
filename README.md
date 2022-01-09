# steps:
## create a container from docker image
`cd dockerImage_mp9`
`docker build -t mp9 .` (this builds the image, whose name is "mp9", don't forget the . at the end of command)
`docker run -it mp9 /bin/bash`  (create an instance or container of the image, mp9)

## load dataset 
 Download the gbook file ( http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-1gram-20120701-a.gz ), unzip it into our current directory (around 1.8g), rename it to "gbooks" (This is important!) , and write a function to load it in an RDD & DataFrame. Print your DataFrame's schema. NOTE: Your programs should always assume "gbooks " file is in the current directory! 
Sample Output of 'MP3\_SQLite.py'
~~~sh
Opened database successfully
Table created successfully
ID =  1
NAME =  Paul
ADDRESS =  California
SALARY =  20000.0 

ID =  2
NAME =  Allen
ADDRESS =  Texas
SALARY =  15000.0 

ID =  3
NAME =  Teddy
ADDRESS =  Norway
SALARY =  20000.0 

ID =  4
NAME =  Mark
ADDRESS =  Rich-Mond 
SALARY =  65000.0 

Records created successfully
Total number of rows updated : 5
Total number of rows deleted : 6
~~~


