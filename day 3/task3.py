name = input("What is your name? ")
print(f"Hello {name.capitalize()}, welcome to the Python world!")
mood = input("How are you today? ")
if mood.lower() == "good"or mood.lower() == "fantastic":
    print("That's great to hear! Keep up the positive vibes!")  
else:
    print("I'm sorry to hear that. I hope your day gets better!")
age = input("how old are you? ")
if age.lower() <= "18":
    print("still young")
else:
    print("you need to retire")
