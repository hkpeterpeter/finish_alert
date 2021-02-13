import os
def say(msg = "Ende", voice = "Anna"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
