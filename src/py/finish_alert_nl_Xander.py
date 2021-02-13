import os
def say(msg = "einde", voice = "Xander"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
