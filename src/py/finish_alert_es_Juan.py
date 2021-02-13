import os
def say(msg = "fin", voice = "Juan"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
