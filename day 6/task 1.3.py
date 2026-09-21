def bread():
    print("<//////////>")

def lettuce():
    print("~~~~~~~~~~~~")

def tomato():
    print("O O O O O O")

def ham():
    print("============")

def sandwich(n):
    if type(n) != int:
        print("I can't do this!")
        return

    for _ in range(n):
        bread()
        lettuce()
        tomato()
        ham()
        ham()
        bread()

sandwich(3.14)