import os
def say(msg = "Sfârșit", voice = "Ioana"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
