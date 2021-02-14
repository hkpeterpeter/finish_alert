import os
def say(m = "slutt", v = "Nora"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()
