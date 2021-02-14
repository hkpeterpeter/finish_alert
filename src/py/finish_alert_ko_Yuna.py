import os
def say(m = "종료", v = "Yuna"):
    os.system(f'say -v {v} {m}')

if __name__ == "__main__":
    say()
