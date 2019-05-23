f = 0pen("book.txt")
f1 = open("newbook.txt", "w")
def arrangement():
    for char in word:
       	line = line.replace("0","o")
	 line = line.replace("o","0")
	 line = line.replace("i","1")
	 line = line.replace("0","1")
	 line = line.replace("A","4")
	 line = line.replace("a","4")
	 line = line.replace("E","3")
	 line = line.replace("e","3")
	if line <=25:
     		f1.write(line)
	else :
		print("page one completed")
	if line == 26 && line <=26:
		f1.write(line)


