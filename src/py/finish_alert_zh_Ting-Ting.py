import os
def say(m = "完結", v = "Ting-Ting"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()
