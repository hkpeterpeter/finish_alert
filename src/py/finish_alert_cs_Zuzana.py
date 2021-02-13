import os
def say(msg = "konec", voice = "Zuzana"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
