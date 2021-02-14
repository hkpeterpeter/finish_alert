import os
def say(m = "einde", v = "Xander"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()
