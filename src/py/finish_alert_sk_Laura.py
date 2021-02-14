import os
def say(m = "koniec", v = "Laura"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()
