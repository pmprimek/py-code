# Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>,
<|laptop|>
'''

letter = letter.replace("<|Name|>","prince")
letter = letter.replace("<|Date|>","25/06/2026")
letter = letter.replace("<|laptop|>","macbook pro 2")

print(letter)
