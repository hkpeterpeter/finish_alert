import os
def say(m = "einde", v = "Ellen"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()
