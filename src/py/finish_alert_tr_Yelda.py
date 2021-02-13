import os
def say(msg = "son", voice = "Yelda"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
