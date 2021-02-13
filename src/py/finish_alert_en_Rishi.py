import os
def say(msg = "Finish", voice = "Rishi"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
