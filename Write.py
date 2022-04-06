# f = open('sample1.txt','w')
# f.write("This is sample file")
# f.close()


#note: if we use w mode in existing file this will overlap the content 
#Therefore we use a mode that is append mode this we continue from end of existing file

f = open('sample1.txt','a')
f.write(" I ll append this file")
f.close()