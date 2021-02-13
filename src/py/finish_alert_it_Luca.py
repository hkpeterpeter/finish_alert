import os
def say(msg = "fine", voice = "Luca"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
