# Password Management
This is my first project made with MySQL, Tkinter and File Handling. It took me a while to bring this up and running in Tkinter. Given below are steps on how to compile it.

Step 1:- Meet the requirement.
To ensure the program works well, a couple of programs are required. Links will be provided to download them.
MySQL: https://dev.mysql.com/downloads/ 
Note:- The password that you use while making the server is your master password. This password will be used to enter into the database.

Python:-https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe (I used Python 3.7.9 to make this project, anything that is Python 3 will work)

MySQL Connector to Python:-
  1. Go to Command Prompt
  2. Type the following command:- "pip install mysql-connector-python"

Step 2:- Setup the MySQL table
1.Go into MySQL and create the database name it 'y'
2.Copy and Paste the following query into MYSQL:- CREATE TABLE `y`.`password` (user VARCHAR(256), pass VARCHAR(256), Platform VARCHAR(54));

Step 3:- Go to retrival.py, under the get() method, change the password to your master password.

After these steps, you can finally use your password management database.


Options provided in the program.
1.Show Entire Database:- This, as stated, shows the entire database and allows the user to copy multiple user-ids
2.Search Password:-This option helps the user to find a specific user-id
3.Add a user:- This option allows the user to add more users to the database with user-defined passwords
4.Add a user with a computer-generated password: This option allows the user to add more users to the database with passwords that are strong and are easily usable
5.Update a password:- It allows the user to update an existing password with a new password
6.Delete a user-id pair:- It allows the user to delete an existing user-id/password.
