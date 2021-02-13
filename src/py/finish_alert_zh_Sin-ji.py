import os
def say(msg = "完結", voice = "Sin-ji"):
    os.system(f'say -v {voice} {msg}')

if __name__ == "__main__":
    say()
