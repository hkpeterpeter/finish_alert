import os
def say(msg = "ende", voice = "Sara"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
