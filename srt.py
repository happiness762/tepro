movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
["Graham Chapman", ["Michael Palin", "John Cleese",
"Terry Gilliam", "Eric Idle", "Terry Jones"]]]
def lol(list_movues):
	for each_item in list_movues:
		if isinstance(each_item,list):
			lol(list_movues)
print(lol(movies))