import os
def say(m = "конец", v = "Yuri"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()
