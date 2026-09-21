def bread():
    print("<//////////>")

def lettuce():
    print("~~~~~~~~~~~~")

def tomato():
    print("O O O O O O")

def ham():
    print("============")

def sandwich(n, veg=False):
    if type(n) != int:
        print("I can't do this!")
        return

    for _ in range(n):
        bread()
        lettuce()
        tomato()

        if veg:
            lettuce()
            tomato()
        else:
            ham()
            ham()

        bread()
sandwich(1, True)
