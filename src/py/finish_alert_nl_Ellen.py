import os
def say(msg = "einde", voice = "Ellen"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
