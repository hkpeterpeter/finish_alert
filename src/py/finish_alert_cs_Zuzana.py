import os
def say(m = "konec", v = "Zuzana"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()
