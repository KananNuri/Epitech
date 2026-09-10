text = input("write a text: ").lower()
text = text.encode("utf-8").decode("utf-8")
for letter in set(text):
    print(letter, text.count(letter))
if text.count("e") > text.count("a"):
    print("probably english")
