import os
def say(msg = "fine", voice = "Alice"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
