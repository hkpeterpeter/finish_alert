import os
def say(msg = "vége", voice = "Mariska"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
