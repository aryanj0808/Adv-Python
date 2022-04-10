#*****************************QUE1**********************************************

#write a program to read poem.txt and find out whether it contain word "twinkle"

# f = open('poem.txt','r')
# r = open('sample.txt','r')
# text = f.read()
# text1 = r.read()
# if 'Twinkle' in text:
#     print("Twinkle is present")
# else:
#     print("Twinkle is not present")
# if 'Twinkle' in text1:
#     print("Twinkle is present")
# else:
#     print("Twinkle is not present")


#******************************QUE2************************************************


def game():
    return 465
score=game()
s=open('score.txt','r')
hiscore=int(s.read())
if score>hiscore:
    g = open('score.txt','w')
    g.write(str(score))
    g.close()
else:
    s.close()