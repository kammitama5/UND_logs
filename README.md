# UND_logs

## Final Logs Project

## Objective: Analyze logs given a sql file using Python, VirtualBox and Vagrant.

## Start with the Original Repo: 

You can fork or clone Udacity's Vagrant file for the Project [here](https://github.com/udacity/fullstack-nanodegree-vm) 

- This Project uses:

```
Postgres v 9.5.9
Vagrant 1.9.2
VirtualBox 5.1.6
Python 2
```

- Instructions are defined as ```$ ```, which is a ```bash``` command 
  or ```=>``` which is a ```psql``` command.
  
## Get up and running with VirtualBox and Vagrant

- Go to your command line and find the downloaded file that was cloned

- ```$ cd``` into your vagrant folder. 

- You should see your vagrant file listed.

- Type ```$ vagrant up``` to start Virtualbox and set up vagrant file

- ***Note:*** You may have to turn on Virtualization in your BIOS via rebooting
  and ```enable virtualization```. 
  
- Vagrant may hang a bit, but if it is taking too long and nothing is happening,
  you may want to hit ```Ctrl + C``` and troubleshoot.
  
## Assuming all goes well. 

- ```$ ssh``` into your virtualbox. You should see ```vagrant@vagrant``` as the user.

- ```$ cd``` into where your vagrant file is located. You should see your sql file.

## Setting up your database and making queries

1. ```$ cd``` into where sql file is located

<img src="/md_photos/nd_002.png" width="400">

2. Load data in database using command:

   ```
   psql -d news -f newsdata.sql
   ```
   
  <img src="/md_photos/nd_003.png" width="400"> 
  
3. Use ```=> psql -d news``` to connect to database.

  <img src="/md_photos/nd_004.png" width="300">
  
4. Success! You have imported the sql file and will see this:

  <img src="/md_photos/nd_001.png" width="300">
  
5. Create allviews by typing:  

```
=> create view allviews as (select title, author, count(*) 
as num from articles,log where log.path=CONCAT('/article/',articles.slug)
group by articles.title,articles.author order by num desc)
```
<img src="/md_photos/nd_005.png" width="500">

6. To exit psql, type ```$ Ctrl + D```. This will bring you back to the bash shell.

7. ```$ cd ``` to your vagrant directory, and run the python file.

8. Run python file by typing ```$ python logs.py``` to see run queries
   or pipe them to a text by running
   
   ```$ python logs.py / all > ouptput.txt```.
   
   This will generate a file called ```output.txt``` in the directory where ```logs.py``` 
   is located.
   
 <img src="/md_photos/nd_009.png" width="500">
   
7. Your queries should match the result in output.txt

- Query One 

<img src="/md_photos/nd_006.png" width="400">

- Query Two 

<img src="/md_photos/nd_007.png" width="400">

- Query Three

<img src="/md_photos/nd_008.png" width="500">
   
 
