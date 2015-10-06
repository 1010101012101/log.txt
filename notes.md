=====================================================================================
LINUX
=====================================================================================

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

=====================================================================================

Useful commands [with some commonly used options]:
	ls -d							# list directories without showing their contents
	echo -e						# enable the interpretation of backslash characters	
	ls -R							# list directories recursively
	

=====================================================================================

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

=====================================================================================

Use the 'sed' program/filter to make changes to files without launching a text editor. The changes are made right from the command line.
An example:
	- sed -e 's/night/day/'
A common error is to forget to include the trailing forward slash which results in the following error message:
	" sed: -e expression #1, char 14: unterminated `s' command "


=====================================================================================
Configure Auto-startup

The /etc/rc.d/boot.local or /etc/rc.local scripts are Bash scripts that can be edited to include command-line instructions to run desired programs on system startup.



=====================================================================================
Python:
=====================================================================================

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




=====================================
git
=====================================
	Push changes to a remote git repo:
		- git push -u origin master
	
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




=====================================
Life tips
=====================================
 - Listen to smalltalk
 - Get a mentor / coach
 - Define purpose before jumping ship
 - Avoid winers (complainers)

A mentor will push you beyond your imagined capabilities



=====================================
Piano Lessons with Samuel Ajose
=====================================
