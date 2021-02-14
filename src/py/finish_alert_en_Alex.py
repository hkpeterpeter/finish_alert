import os
def say(m = "Finish", v = "Alex"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()
