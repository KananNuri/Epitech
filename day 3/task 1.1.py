text = "I am learning Python at Epitech"
print(text)
print(text[0])
print(text[-1])
print(text[4:10])
print(text.lower())

text = "tutu on the tuki-kata"
print(text.replace("tu", "ta"))

text = "Hello World"
position = text.find("a")
print(position)
position = text.find("o")
print(position)

p = "abcdefghij"
print(p[::-2][:5][::-1][3:])

p = "abcdefghij"
step1 = p[::-2]
print (step1)
step2 = step1[:5]
print (step2)
step3 = step2[::-1]
print (step3)
step4 = step3[3:]
print (step4)

text = "I am learning Python at Epitech"
for i in range(10):
    print(text)

print(ord("k"))
print(chr(99))


text = "the CataCat attaCk a Cat"
text = text.lower()
print(text[::-1])
print (text.count("cat")+text.count("tac"))

text = "thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN".lower()
print (text.count("mice")+text.count("ecim")+text.count("garden")+text.count("nedrag")+text.count("cat")+text.count("tac"))