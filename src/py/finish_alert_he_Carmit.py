import os
def say(m = "סוֹף", v = "Carmit"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()
