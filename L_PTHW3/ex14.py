from sys import argv

script, user_name = argv
prompt = '> '

print(f"hi {user_name}, I'm the {script} script.")
print("I'd like you to ask you a few questions.")
print(f"Fo yo like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer =input(prompt)

print(f"""
Alright, so you said{likes} about liking me.
you live in {lives}. not sure where that is.
and you have a computer {computer} computer. nice.
""")