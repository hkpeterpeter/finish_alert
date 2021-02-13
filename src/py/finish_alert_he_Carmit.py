import os
def say(msg = "סוֹף", voice = "Carmit"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
