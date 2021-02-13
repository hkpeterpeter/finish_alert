import os
def say(msg = "نهاية", voice = "Maged"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
