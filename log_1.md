
====================================
Setting up Themes for Ubuntu Unity
====================================
* Install Unity Tweak
* Install Ubuntu Tweak
* Get fonts online and install normally

http://askubuntu.com/questions/520379/where-can-i-find-more-unity-themes

* http://snwh.org/moka/download/
	sudo add-apt-repository ppa:moka/stable
	sudo apt-get update
	#sudo apt-get install orchis-gtk-theme

* https://numixproject.org/
* https://launchpad.net/~noobslab/+archive/ubuntu/themes?field.series_filter=utopic


***Tip***
After adding a "ppa", software from that repository shows up in the Ubuntu Software center.





============================
Setting up Android Studio IDE
============================
Install JDK (Oracle or OpenJDK)

Download Android Studio package - contains installation instructions

Get installation instructions for KVM here:
	- https://help.ubuntu.com/community/KVM/Installation

***I ran into an issue trying to run the IDE whisch worked on my b32bit version of Ubuntu on my newly installed 64bit version. I fixed it by intalling a tool:
	lib32stdc++6	 -	(Full instructions here ---> http://stackoverflow.com/questions/28847151/unable-to-install-android-studio-in-ubuntu)




============================
Update pip
============================
	$ [sudo] pip install --upgrade pip		# 'sudo' might be optional depending on install environment
	
	

============================
Configure system defaults
============================
	sudo update-alternatives --all
	

===================================
Set 'terminator' as default gnome-terminal
===================================
	 $ gsettings set org.gnome.desktop.default-applications.terminal exec 'terminator'
	 $ sudo update-alternatives --config x-terminal-emulator



===================================
 --- > IRC
===================================
	/server [server_address] [server_port]			# Connect to specified server through specified port. [commonly used port is 6667]
	/join #[channel_name]								# Join specified channel. Some channels use '##' as prefix
	/msg NickServ help									# Get list of commands from NickServ (a special IRC nick-service bot)


===================================
Setting Environment Variables
===================================
Use the 'export' command to create an environment variable like so:
	$ export VAR_NAME=path/to/fileORfolder



===================================
Android Studio
===================================
	The Android Studio IDE is run directly from the extracted setup files. You start the IDE by running the "studio.sh" shell script found in its "bin/" directory.



===================================
Git config
===================================
Use the 'git config' command line tool to set/update git configuration variables such as username

Example config command:
	git config --global user.email "you@example.com"
	git config --global user.name "Your Name"

Command options:
	git config --system									# command option for system-wide config
	git config --global									# for user specific git config
	git config												# git config for current git repo

Files:
	/etc/gitconfig											# system-wide git config
	/.gitconfig or ~/.config/git/config				# git file in home directory (user global config)
	.git/config												# config file in git directory of current repository



===================================
gitbox it!
===================================
First I create a local git repo in my desired folder:
	$ git init
Set things as normal. Create a .gitignore file in repo's root directory
See how things are going:
	$ git status
Go to github; create a new repo
Add and commit local changes:
	$ git add
	$ git commit -m "[commit message]"
See how things are going again:
	$ git status
Then push to the online repo with:
	$ git remote add origin [online_repo_url]
	$ git remote -v 			# verify the new remote url
Pull changes from online repo:
	$ git pull origin master
Finally, push changes:
	$ git push origin master




===================================
(Meld) File Diff Comparisons
===================================
Meld is a good GUI tool for comparing text file differences. It can also compare folder differences. To install, use
	$ sudo apt-get install meld




===================================
Bash History
===================================
The ".bash_history" file in my home directory (~) stores command histories, that is, all the commands I type in the terminal are logged in this file.

An easy way to search for specific commands in my command history is to use:
	$ grep -E '[command_or_part_of_command]' ~/bash_history





