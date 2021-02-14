import os
def say(m = "finir", v = "Thomas"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()
