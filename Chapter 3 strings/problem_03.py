# 3. Write a program to detect double space in a string.
name = "prince is a good boy"
print(name.find(".")) # esme double space nhi hai esliye -1 out put aaya 

name = "prince is  a good boy"
print(name.find("  ")) # esme double space 9 step per hai esliye output 9 aaya

name = "prince is a good boy"
print(name.find("boy")) #esme boy 17 step per hai esliye output 27 aaya

