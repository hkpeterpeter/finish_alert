import os
def say(msg = "Finish", voice = "Moira"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
