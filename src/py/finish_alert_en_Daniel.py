import os
def say(msg = "Finish", voice = "Daniel"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
