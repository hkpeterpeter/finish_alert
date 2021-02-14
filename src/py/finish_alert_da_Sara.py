import os
def say(m = "ende", v = "Sara"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()
