import os
def say(msg = "完結", voice = "Ting-Ting"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
