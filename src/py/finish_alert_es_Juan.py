import os
def say(m = "fin", v = "Juan"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()
