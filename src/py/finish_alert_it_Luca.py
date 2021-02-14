import os
def say(m = "fine", v = "Luca"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()
