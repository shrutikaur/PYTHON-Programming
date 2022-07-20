name = input("Enter your name: ")
print("Good Afternoon, " + name)

name = input("Enter your name: ")
date = input("Enter today's date: ")
letter = '''
Dear <|NAME|>
You are Selected!
<|DATE|>
'''
print(letter.replace('<|NAME|>', name).replace('<|DATE|>', date))
