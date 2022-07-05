# fp=open("base.txt","w")
# lines=['this is the first example of the write lines',' //  you can write many lines in the write line']
# fp.writelines(lines)
#
# fp.close()

r=open("base.txt","r")
a=r.readline()
print(a)
b=r.readlines()
print(b)
# r.writelines('lines /n ')
r.close()
