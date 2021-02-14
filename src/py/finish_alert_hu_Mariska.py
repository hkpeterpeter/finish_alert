import os
def say(m = "vége", v = "Mariska"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()
