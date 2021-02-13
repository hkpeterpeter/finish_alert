import os
def say(msg = "finir", voice = "Thomas"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
