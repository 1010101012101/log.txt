#!/usr/bin/python


td_file = "todo.md"		# name of todo file

td_tags = ""			# list todo tags

menu = { \
	1: "View todos", \
	2: "View tags", \
	3: "View todos with tag" \
}						# menu used when running the program



def get_input(msg=""):
	if len(msg)>0:
		print msg
	user_input = raw_input("\n\t>_ ")
	return user_input



def read_todo_file(hide_done=False):
	with open(td_file) as f:
		td_cont = f.readlines()
	
	if hide_done:
		for todo in td_cont:
			if todo.startswith('#'):
				del todo
	return td_cont	



def display_all_todos():
	td_cont = read_todo_file()
	count = 0
	msg = "You have the following todos:\n" if len(td_cont)>0 else "You have no todos."
	print msg
	for line in td_cont:
		count += 1
		if line.find("::") > -1:
			print "\t%d.\t%s" %(count, line.split('::')[1])



def display_all_tags():
	tags = []
	td_cont = read_todo_file()
	count = 0
	msg = "You have the following tags:\n" if len(td_cont)>0 else "You have no tags."
	print msg
	for line in td_cont:
		count += 1
		if line.find("::") > -1:
			tags.extend((line.split('::')[0].split(':')))

	count = 0
	for tag in tags:
		if tag.startswith("#"):
			tag = tag[1:]
		
		if count%5==0:
			print
		print "%s;\t" %tag,
		count += 1



def display_todos_with_tag(tag):
	td_cont = read_todo_file()
	count = 0
	msg = "The folloowing todos matched the 'tag': %s\n" %tag #if len(td_cont)>0 else "No todo matched the tag: '%s'" %tag
	print msg
	for line in td_cont:
		if line.find("::") > -1:
			tags = line.split("::")

			if tags[0].find(tag)>-1:
				count += 1
				print "\t%d.\t%s" %(count, line.split('::')[1])





if __name__ == "__main__":

	print "\n============== Takwas TODO Manager ===============\n"

	while True:
		print "Select an operation"

		for i in range(1,4):
			print "%d.  %s" %(i,menu[i])
		
		option = get_input()

		try:
			option = int(option.strip())
		except ValueError:
			print "\n\t\tYour option is invalid! Try again.\n"


		if option==1:
			display_all_todos()
		elif option==2:
			display_all_tags()
		elif option==3:
			tag = get_input("Enter tag:")
			display_todos_with_tag(tag)

		raw_input("\nHit %s to continue; %s to stop.\n\n" %("[Enter]", "[Ctrl+C]"))