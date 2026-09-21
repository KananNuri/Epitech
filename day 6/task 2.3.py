import os

def show(path="."):
    for item in os.listdir(path):
        full = os.path.join(path, item)
        print(full)

        if os.path.isdir(full):
            show(full)

show()