import os
def say(m = "Sfârșit", v = "Ioana"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()
