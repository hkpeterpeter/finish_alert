import os
def say(msg = "समाप्त", voice = "Lekha"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
