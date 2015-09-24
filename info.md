===================================
SLACK IRC CON INFO
===================================
Host: krohx.irc.slack.com
User: takwas
Pass: ********

    
Ensure that your IRC client is configured with your normal Slack username as your nick.
    
If you are connecting through a raw /server command, your command will be:
    /server krohx.irc.slack.com 6667 [password]
    
If you have a more UI-oriented setup, your:
	IRC server:		krohx.irc.slack.com
	Server password:	********
	Accepted ports:	6667, 6697, and 8000.



===============================================================================
GIT Repos:
===============================================================================
My local git repos:
	- ~/dev/web_dev/flask_web_dev/practice/flask_learn/template_app
	- ~/log_things_I_do
	- ~/dev/python_dev/workspace/python_class
	- ~/niit
	- ~/dev 																														# not hosted on Github yet
	- ~/dev/web_dev/flask_web_dev/proj/krohx_proj/afraisr												# not hosted on Github yet
	- ~/dev/web_dev/flask_web_dev/proj/krohx_proj/router												# not hosted on Github yet
	


alias afraisr="source ~/web_dev/flask/bin/activate && cd ~/web_dev/flask/projects/afraisr"



Always remember these .....

git branch frontend													# create branch called "frontend"
git checkout frontend												# move to branch called "frontend"
# ...make changes to files...
git add .																# add new files and modified files
git commit -m [commit message]								# save current working tree in history
git checkout master												# move to branch called "master"
git merge frontend													# merge in changes from branch called "frontend"
git pull origin 														# Bring changes from bitbucket. This one isn't always compulsory. 
git push -u origin master											# push changes to bitbucket
