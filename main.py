text = 'File Write Python - Read and  to files with Python'
x = text.split()
lengs_world = len(x[0])
world = str()
print(lengs_world)
for i in x:
	if len(i) >= lengs_world:
		lengs_world = len(i)
		world = i
print(lengs_world)
print('longest word of txt file is', world)
