import os
def say(m = "koniec", v = "Zosia"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()
