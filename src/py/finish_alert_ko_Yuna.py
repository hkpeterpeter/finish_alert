import os
def say(msg = "종료", voice = "Yuna"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
