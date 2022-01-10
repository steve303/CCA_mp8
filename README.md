steps:  
1.  create a container from docker image    

After cloning the repo, issue the commands below:  
`cd dockerImage_mp9`  - This is where the "Dockerfile" resides and contains the information to build the image.  
`docker build -t mp9 .` - This builds the image, whose name is "mp9", don't forget the . at the end of command.  
`docker run -it mp9 /bin/bash`  - This creates an instance, aka "container", of the image, mp9; you should now be running in the environment of the container.  
You should now get a prompt that looks like this: `root@373d63d17f59:/#`.  You are now working from the Docker container via BASH (BourneAgainSHell).  

2.  Load Dataset  
If you want to work with Python, change directory to python otherwise java directory for java.  Download the gbook file ( http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-1gram-20120701-a.gz ).  Use `wget` to download the `.gz` file then decompress using `gzip -d <file_name>`.  Rename to "gbooks"; it's a big file 1.8GB.  NOTE: Your programs should always assume "gbooks " file is in the current directory!


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


