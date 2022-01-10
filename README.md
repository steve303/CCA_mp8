steps:  
1.  Create a container from docker image (host machine)   

Note, the purpose of the docker container is so that we don't have to install Apache Spark on our "host" machine.  Alternatively you can install Apache Spark on your machine which will take a bit more work.  

First, open up a terminal window and issue the commands below:
`git clone https://github.com/steve303/sparkSQL` - This downloads contents of this repo into your host machine.
`cd dockerImage_mp9`  - This is where the "Dockerfile" resides and contains the information to build the image.  
`docker build -t mp9 .` - This builds the image, whose name is "mp9", don't forget the . at the end of command.  
`docker run -it mp9 /bin/bash`  - This creates an instance, aka "container", of the image, mp9; you should now be running in the environment of the container.  
You should now get a prompt that looks like this: `root@373d63d17f59:/#`.  You are now working from the Docker container via BASH (BourneAgainSHell).  

2.  Load Dataset (container)  
Within the container we need to download the data set.  If you want to work with Python language, change the current directory to `python/` otherwise `java/` directory for java.  For this section, issue the commands below:  
`wget http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-1gram-20120701-a.gz` - Download the gbook file ( http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-1gram-20120701-a.gz ).  
`gzip -d googlebooks-eng-all-1gram-20120701-a.gz` - This will decompress the .gz file.  
`mv googlebooks-eng-all-1gram-20120701-a.gz gbooks` - Rename to "gbooks"; it's a big file 1.8GB.  
NOTE: Your programs should always assume "gbooks " file is in the current directory, in this case either `python/` or `java/`.  

3.  Run example python sparkSQL scripts

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


