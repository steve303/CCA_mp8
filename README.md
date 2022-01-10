## Examples of using pyspark to perform basic operations in spark SQL within a Docker container
Steps:  
1.  Create a container from docker image   
Note, the purpose of the docker container is so that we don't have to install Apache Spark on our "host" machine.  Alternatively you can install Apache Spark on your machine which will take a bit more work.  
First, open up a terminal window and issue the commands below:  
`git clone https://github.com/steve303/sparkSQL` - This downloads contents of this repo into your host machine;  
`cd dockerImage_mp9`  - This is where the "Dockerfile" resides and contains the information to build the image;  
`docker build -t mp9 .` - This builds the image, whose name is "mp9", don't forget the . at the end of command;  
`docker run -it mp9 /bin/bash`  - This creates an instance, aka "container", of the image, mp9; you should now be running in the environment of the container.  
You should now get a prompt that looks like this: root@373d63d17f59:/#.  You are now working from the Docker container via BASH (BourneAgainSHell).  

2.  Load supporting Docs into the container  
Now that we are working from the container, no longer from the host machine (so to speak), we need to download supporting docs.  To do this, we will again clone this repo, this time into our container.  At the root level in your container clone this repo. Issue the command, `git clone https://github.com/steve303/sparkSQL` - This will create a new folder /sparkSQL in your container.  The files we are interested in are in the /sparkSQL/python/ and /sparkSQL/java/ folders.  

4.  Load Dataset into container  
Within the container we need to download the data set.  If you want to work with Python language, change the current directory to /sparkSQL/python/ otherwise /sparkSQL/java/ directory for java.  For this section, issue the commands below:  
`wget http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-1gram-20120701-a.gz` - This downloads the file;  
`gzip -d googlebooks-eng-all-1gram-20120701-a.gz` - This will decompress the .gz file;    
`mv googlebooks-eng-all-1gram-20120701-a gbooks` - This will rename to "gbooks" (it's a big file 1.8GB).  
NOTE: Your programs should always assume "gbooks " file is in the current directory, in this case either /sparkSQL/python/ or /sparkSQL/java/.  

3.  Run example python spark SQL scripts  
Within the /sparkSQL/python/ folder issue the command: `spark-submit <filename>`.  Filename in our case will be i.e., MP3_partA.py.  Note, even though we are running a .py file we do not issue the typical command "python3 filename.py" since we want to use ApacheSpark.  Each file in this folder performs a different task to demonstrate how to perform basic spark SQL tasks.  These are creating the schema, defining a table/RDD, and performing SQL queries.    

4. Run pyspark interactively  
To run interactively type `pyspark` into the terminal.  You can run the commands as in the .py files, i.e. MP3_partA.py, with some minor deviations.  Firstly, you don't need to create an instance of the spark session (sparkContext()); it is created for you and is named "spark".  So use this whenever the instance name is required.  

5. To exit container and restart  
To exit the container type "ctl-d".  To restart the container enter:  
`docker start <container name>` - this restarts the container;  
`docker ps` - this lists all of the docker processes, find your container's process#;  
`docker exec -it <process#> /bin/bash` - this will bring up BASH interface in your container.  

6.  To bring up another instance-container of your image  
`docker run -it <image name> /bin/bash`    

### Resources  
Some contents were sourced from UIUC MCS coursework   
[video demonstration](https://www.dropbox.com/s/i8qhyhnywqw5sno/mp08_sparkSQL.mp4?dl=0)  
[problem statement](https://www.dropbox.com/s/on8xz4hd1cy0tie/03_machine-problem-8-sparksql_instructions.html?dl=0)  
note: links require a password which is the repo name
          

