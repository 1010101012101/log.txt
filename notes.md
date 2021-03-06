=====
LINUX
=====

	.		refers to current directory
	..		refers to parent directory


(Refer to the manpage on "grep" for more.)
grep is used for searching through strings/files for matching patterns. There are deprecated versions of grep: egrep and fgrep, the newer invocations for these (on the command line) are:
	grep -E
and
	grep -F
respectively.

Some command line options for invoking grep:
	-c		# show the count of matching strings
	-v		# show non-matching strings instead. Negative search
	-o		# show only matching strings not the entire lines
	-n		# show line numbering for matching lines
	-I		# do not search binary files (NOTE: uppercase "i" not lowercase "L")
	-l		# show file names for files with matching string instead of matching content (NOTE: lowercase "L" not uppercase "i")

To search for all files in a folder, use the '*' wildcard character as file-to-search argument.
	-H		# display filename for file containning matching line
	-d [ACTION] OR --directories=[ACTION] 					# e.g ACTION can be 'recurse' to search directories recursively
	-r OR --recursive													# same as "-d recurse" above

=====================================

Useful commands [with some commonly used options]:
	ls -d							# list directories without showing their contents
	echo -e						# enable the interpretation of backslash characters	
	ls -R							# list directories recursively
	

#  

=====================================

Working with links:
	ln -s /path/to/original/ /path/to/linkName				# create a symbolic (soft) link to the original path/file
	
	ln /path/to/original/ /path/to/linkName				# create a hard link to the original path/file
	

Basic differences between soft and hard links:

	Hard links:
		- Only link to a file not a directory
		- Can not reference a file on a different disk/volume
		- Links will reference a file even if it is moved
		- Links reference inode/physical locations on the disk

	Symbolic (soft) links:
		- Can link to directories
		- Can reference a file/folder on a different hard disk/volume
		- Links remain if the original file is deleted
		- Links will NOT reference the file anymore if it is moved
		- Links reference abstract filenames/directories and NOT physical locations. They are given their own inode

#  

=====================================

Use the 'sed' program/filter to make changes to files without launching a text editor. The changes are made right from the command line.
An example:
	- sed -e 's/night/day/'
A common error is to forget to include the trailing forward slash which results in the following error message:
	" sed: -e expression #1, char 14: unterminated `s' command "


#  

=====================================
Configure Auto-startup

The /etc/rc.d/boot.local or /etc/rc.local scripts are Bash scripts that can be edited to include command-line instructions to run desired programs on system startup.






======
PYTHON
======

'assert' statements are used to test the truethiness of statements:
	if the expression being tested is True, nothing happens, the program continues as normal;
	otherwise, if it evalutes to False, then an AssertionError will be raised

with

	os.rename([oldname], [newname]) :
		- Python inbuilt module: 'os' has a function called 'rename()' that can be used to rename files within a filesystem.


--------------------------------------------------
Specifying encoding for your Python script file
--------------------------------------------------

By default, the Python interpreter assumes that a script file it wants to run will be encoded
in ASCII. However, if you wish to include unicode characters in the script, you should include
a comment line which matches the following regular expression on the first or second line of the script:
		"coding[:=]\s*([-\w.]+)"			# excluding the quotes

Some sample strings which match the above regexp:
	- # -*- coding:utf-8 -*-
	- # encoding= iso-8859-2
	- # this file uses encoding: utf-8


As a mechanism for "defensive programming," try to write assertions (no pun intended) to ensure you're getting the right/expected input/input-range before going ahead to process same.


Testing
-------

"For unit tests, start with testing that it does what it is designed to do. That should be the very first case you write. If part of the design is "it should throw an exception if you pass in junk", test that too since that is part of the design.

Start with that. As you get experience with doing that most basic of testing you'll begin to learn whether or not that is sufficient, and start to see other aspects of your code that need testing."


"You are working on some specific piece of code, and this is exactly what you want to test. This means that you should not be testing library functions, the standard library or your compiler. Also, try to avoid testing the 'world'. This includes: calling external web APIs, some database intensive stuff, etc. Whenever you can try to mock it up (make an object that follows the same interface, but returns static, predefined data)."






===
GIT
===
	Push changes to a remote git repo:
		- git push -u origin master
	
	Force-push (overwrite) changes to a remote git repo:
		- git push -u [remote_name] [remote_branch]
	
====STUDYING GIT====
- The name of a branch is an alias for the most recent commit on that branch.
- A tag-name alias much like the branch alias names a commit. However, while a branch alias changes everytime a new commit is cheked in to a branch, a tag alias never changes.
- A commit can also be reffered to by its 40-character SHA I hash id -- you usually only have to type 6 to 7 or more characters of this hash id to identify an object.

	git commit	--allow-empty-message								# Allows you to commit without a commit message
	git reset --hard [branch name or hash id of commit]		# '--hard' option means clear all changes currently in my working tree; i.e. take me back to specified commit, clearing everything (every commit) along the way
	git checkout [hash id of commit or branch name] [-f]		# the optional option '-f' has the same function as '--hard' above
	git branch																	# list, create or delete branches
	git show-branch
	git branch [branchname]												# create new branch of development named 'branchname'
	git checkout [branchname]											# switch to named branch of development
	git checkout -b [branchname]										# create and checkout branch in one step
	git rebase -i
	git branch -d [branchname]											# delete a branch making sure if it has been fully merged in HEAD 
	git branch -D [branchname]											# fully delete a branch irrespective of its merge state
	git branch -r																# view list of remote tracking branches; i.e branches on my remote repos
	
	git merge [branchname]												# join changes from branch with 'branchname' with current branch
	
	git log																		# list commits newest to oldest
	git log -p																	# list commits with their diff
	git log --grep="[pattern]"											# list commits whose commit messages contain the given string pattern
	git log --one-line													# show one-liner log summary
	git blame [filename]													# show all lines of file with "filename" and their current commit
	
	git rm --cached [filename]											# safely remove (unstage) file from git repo index, leaving file untouched in working tree
	git rm --cached -r [directoryname]								# same as above, but for directories
	
	git pull																		# fetch and merge changes from a remote repository into the current local branch
	git ls-files --other --ignored --exclude-standard			# list all ignored/untracked files in this repository
	
	git clean -fd 																# delete everything (only git-tracked files) and start all over
	git clean -fdx 															# same as above, but delete everything (include git-ignored files)

A commit is an object which holds a reference to its parent commit(s) back to their original ancestor, thus forming a history. A commit also references a tree object, which in turn could reference one or more tree objects and blobs (blobs hold the contents of our files).
	
[git rebase -i] allows you to "interactively" edit and combine several commits into one. It is a good practice to make frequent local commits and afterwards merge them as one major commit before pushing them anywhere. As a simple rule of thumb, let your workflow be:
		code -> commit -> rewrite
	
If you have a blank folder, git never tracks that. Git tracks 'files' not 'folders'.
	
Every branch maintains the state of its working tree (its files) without interfering with another.
	
The master branch is the default branch Git creates for you. It's where you work by default. As a rule of thumb, don't work on the master branch. Work on a separate branch and then merge your changes in.
	
HEAD refers to the most current commit on the currently checked out branch or to the currently checked out commit if a commit is checked out instead, in which case, it is referred to as a "detached HEAD".
	
A 'remote' is a repository that lives somewhere else. To add a remote to your current local repo, use:
		git remote add [remotename] [remoteurl]		# a typically used name for a remote is 'origin'; remote url name ends with a '.git'
After adding a remote, you should push local changes to the remote repository with:
		git push [remotename] [branch_name_on_remote]
For example, to push to the 'master' branch on a remote repository named 'origin', you use:
		git push origin master
The above command has a useful option '-u' that should be used with the first time push, like so (following the previous example):
		git push -u origin master			# the -u option allows tracking of changes on the remote repository

	Here's a typical Git collaboration workflow: First you fork an original repo if given "read access" -- which is what you'd get by default if given access at all. This gives you your own copy of the repository. You treat your fork as your remote repo, and clone it to your local development machine where you can make changes.
	At this point, you work like you would with a regular BitBucket/Github hosted repo. Make changes as usual, branch, fetch and merge (or pull), resolve conflicts -- you know, the whole nine yards.
	If you ever feel like sending (patching) in your changes with the original project you forked from, then you'd need to do some house cleaning (on your local development machine), and push to "your remote" repo.
	What follows is you sending-in a kind of request called a "pull request" (which is essentially a kind of "merge" request) to the original repo. If their author be kind enough to allow thee mess with things a little, then you'll receive an affirmative response, after which the hosting service (BitBucket/Github) pulls and merges your changes with that repo, not automatically of course -- you instruct it to.


	A git rebase is essentially a neater version of a branch merge. So when you've wandered away for some time, and you wish to come back home, you could easily a do a merge. But the sad old memories stay there, right? What if you could you magically have your memories (of your time of wandering away) wiped off. Well, I've got good news -- git rebase would do just that for you. So you come back home, and continue your life like the bad things never happened.


If there are merge conflicts and I just want one version to overwrite the other, I'd do:
		git checkout --ours <path> (this will choose the local changes)
or
		git checkout --theirs <path> (this will choose the remote changes)

then finishing resolving the conflict as usual with:
		git add <path>

then commit with:
		git commit


Git Submodules is a feature that allows you have git repositories be contained in parent git repositories.

To add a child repo. From within the root of the parent repo, do:
	git submodule add [URL_TO_GIT_REPO]
This adds a new config file to the root of the parent directory named ".gitmodules". This file, like ".gitignore" should also be version-controlled. It contains a mapping of the submodul repos to their respective remote repo URLs.

To clone an online repo which contains submodules alognside it s submodules, do:
	git clone --recursive [URL_TO_PARENT_GIT_REPO]











======
Github
======
	
	Github "gists" [gists.github.com] works essantially like some kind of pastebin. Code snippets or specific parts of work or projects can be posted there. The posted content can easily be shared, e.g on IRC








=========
LIFE TIPS
=========
 - Listen to smalltalk
 - Get a mentor / coach
 - Define purpose before jumping ship
 - Avoid winers (complainers)

A mentor will push you beyond your imagined capabilities








=======================
MAILING LIST ETIQUETTES
=======================

I went through a list mailing list proper conduct checklist. This is how I paraphrase the basic rules.

    - Do your research before asking.

    - Keep the message short enough.

    - Don't post code or some log output. (Pastebin it, and post a link to it instead).

    - Don't include attachments in your message. (Host it elsewhere, and post a link to it instead)

    - Don't send HTML formatted email; stick with plain text.

    - Start your messgage under a new subject if the topic is new. If it belongs to a previously existing topic, then post your new message as a "reply" to that existing thread.

    - Use a clear, concise and in-context subject line.

    - Use bottom, interleaved posting instead of top-posting. For bottom-posting, let your reply appear directly below the message you are replying to, and trim off the irrelevant parts of the message. When responding to several messages in one mail, use interleaved posting; put your response to each message below the corresponding message. (Some email softwares would prepend each line of the message you are responding to with a '> ').

    - Avoid cross-posting. Do not CC multiple lists with the same message.

    - Use short messages in your signature. And avoid huge disclaimer messages.

    - Avoid repetitive posting.

    - Be polite, use proper language. Avoid using uppercase letters unnecessarily, so you don't appear to be shouting at your readers.






====
JAVA
====

Learning about Strings

Java implements three basic string types: String, StringBuilder, and StringBuffer. Emphasis is placed on the first two as they are the more commonly used ones.

The most basic difference between the Java String class and the Java String Builder class is the fact that the String class which defines the primitive String datatype is immutable, while StringBuilder is mutable.

Immutability results improves program performance.

Java has a [constant] String pool in which it tracks all the String objects it creates in the program run cycle. If a new String is created by simple assignment to a quoted string of characters, Java looks up the string pool, to reuse any already existing string that matches the new string, otherwise, it creates a new String and adds it to the String pool.



=========
Openshift
=========

Common commands:

	rhc app-stop {app_instance_name}
	rhc app-force-stop {app_instance_name}
	rhc app-start {app_instance_name}
	rhc app-restart {app_instance_name}

	rhc tail {app_instance_name}  # view app logs

	rhc set-env [env_var_name]=[env_var_value]