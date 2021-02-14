import os
def say(m = "fin", v = "Paulina"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()
