import os
def say(m = "loppuun", v = "Satu"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()
