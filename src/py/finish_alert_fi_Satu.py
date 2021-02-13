import os
def say(msg = "loppuun", voice = "Satu"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
