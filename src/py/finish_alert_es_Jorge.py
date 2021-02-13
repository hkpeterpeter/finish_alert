import os
def say(msg = "fin", voice = "Jorge"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
