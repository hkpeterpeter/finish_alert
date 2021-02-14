import os
def say(m = "fine", v = "Alice"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()
