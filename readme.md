##1. Configure the environment

virtualenv is a tool to create isolated Python environments.I've created an environment that has all the packages installed, 
called 'venv'. you can just run command 'source venv/bin/activate' to activate this python environment. Alternatively, you can manually install the package in requirments.txt by executing the command 'PIP install-r requirements.txt'

##2.Configure Mysql
All SQL files are in the mysql folder, please execute these instructions in the database.You also need to change the database username, password, and database name in the 'config.py' 

##3. Use the software locally
Before using recommand function, you need to run 'python ML.py' firstly. 
Enter the root directory of the folder and execute the command “python manager.py runserver-h 0.0.0.0-p 80”, where -h represents the server address and -p can select the service port.
