import re

words ="'I AM NOT YELLING', she said. Though we knew better. "
new = re.sub('[.,\'A-Za-z]', '', words)

print(new)

# def my_function(x, y):
#     print(x, "'s ", " First time function")
#     print(y,  " is a good person")


# #my_function("Mike", "Dave")


# def print_people(*people):
#     for person in people:
#         print("this person is", person)

# print_people("Nick", "Adam", "Sam", "Dave", "Rick") 



# run = True
# current = 1
# while run:
#     if current == 100:
#         run = False
#     else: 
#         print (current)
#         current += 1