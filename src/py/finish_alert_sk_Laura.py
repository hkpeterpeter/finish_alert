import os
def say(msg = "koniec", voice = "Laura"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
